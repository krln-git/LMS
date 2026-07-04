"""
Methods for interacting programmatically with the user creator table.
"""


from cms.djangoapps.course_creators.models import CourseCreator
from common.djangoapps.student import auth
from common.djangoapps.student.roles import CourseCreatorRole, OrgContentCreatorRole


def add_user_with_status_unrequested(user):
    """
    Adds a user to the course creator table with status 'unrequested'.

    If the user is already in the table, this method is a no-op
    (state will not be changed).

    If the user is marked as is_staff, this method is a no-op (user
    will not be added to table).
    """
    _add_user(user, CourseCreator.UNREQUESTED)


def add_user_with_status_granted(caller, user):
    """
    Adds a user to the course creator table with status 'granted'.

    If appropriate, this method also adds the user to the course creator group maintained by authz.py.
    Caller must have staff permissions.

    If the user is already in the table, this method is a no-op
    (state will not be changed).

    If the user is marked as is_staff, this method is a no-op (user
    will not be added to table, nor added to authz.py group).
    """
    if _add_user(user, CourseCreator.GRANTED):
        update_course_creator_group(caller, user, True)


def update_course_creator_group(caller, user, add):
    """
    Method for adding and removing users from the creator group.

    Caller must have staff permissions.
    """
    if add:
        auth.add_users(caller, CourseCreatorRole(), user)
    else:
        auth.remove_users(caller, CourseCreatorRole(), user)


def update_org_content_creator_role(caller, user, orgs):
    """
    Method for updating users for OrgContentCreatorRole, this method
    takes care of creating and deleting the role as required.

    Caller must have staff permissions.
    """
    auth.update_org_role(caller, OrgContentCreatorRole, user, orgs)


def get_course_creator_status(user):
    """
    Returns the status for a particular user, or None if user is not in the table.

    Possible return values are:
        'unrequested' = user has not requested course creation rights
        'pending' = user has requested course creation rights
        'granted' = user has been granted course creation rights
        'denied' = user has been denied course creation rights
        None = user does not exist in the table
    """
    # ⚡ Bolt: Use .first() instead of .count() == 0 to avoid COUNT(*) and separate retrieval
    user_entry = CourseCreator.objects.filter(user=user).first()
    if user_entry is None:
        return None
    else:
        # User is defined to be unique, can assume a single entry.
        return user_entry.state


def user_requested_access(user):
    """
    User has requested course creator access.

    This changes the user state to CourseCreator.PENDING, unless the user
    state is already CourseCreator.GRANTED, in which case this method is a no-op.
    """
    user = CourseCreator.objects.get(user=user)
    if user.state != CourseCreator.GRANTED:
        user.state = CourseCreator.PENDING
        user.save()


def _add_user(user, state):
    """
    Adds a user to the course creator table with the specified state.

    Returns True if user was added to table, else False.

    If the user is already in the table, this method is a no-op
    (state will not be changed, method will return False).

    If the user is marked as is_staff, this method is a no-op (False will be returned).
    """
    # ⚡ Bolt: Use .exists() instead of .count() == 0 for efficient existence check
    if not user.is_staff and not CourseCreator.objects.filter(user=user).exists():
        entry = CourseCreator(user=user, state=state)
        entry.save()
        return True

    return False
