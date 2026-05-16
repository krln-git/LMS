import sqlite3

org_aliases = ['org1', 'org2']
courses = ['course1', 'course2', 'course3']

query = (
    """
    SELECT
        user.`id` AS `user_id`,
        user.`username` AS username,
        user.`email` AS `email`,
        profile.`name` AS `full_name`,
        enrollment.`course_id` AS `course_id`,
        (
            SELECT value
            FROM user_api_userorgtag
            WHERE org IN ( {org_list} )
            AND `key`="email-optin"
            AND `user_id`=user.`id`
            ORDER BY modified DESC
            LIMIT 1
        ) AS `is_opted_in_for_email`,
        (
            SELECT modified
            FROM user_api_userorgtag
            WHERE org IN ( {org_list} )
            AND `key`="email-optin"
            AND `user_id`=user.`id`
            ORDER BY modified DESC
            LIMIT 1
        ) AS `preference_set_datetime`
    FROM
        student_courseenrollment AS enrollment
        LEFT JOIN auth_user AS user ON user.id=enrollment.user_id
        LEFT JOIN auth_userprofile AS profile ON profile.user_id=user.id
    WHERE enrollment.course_id IN ( {course_id_list} )
    """
).format(
    course_id_list=','.join(['%s'] * len(courses)),
    org_list=','.join(['%s'] * len(org_aliases))
)

print(f"Number of %s placeholders: {query.count('%s')}")
print(f"Number of parameters in `org_aliases + org_aliases + courses`: {len(org_aliases + org_aliases + courses)}")
