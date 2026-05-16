org_list = ['org1', 'org2']
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
            AND `key`=\"email-optin\"
            AND `user_id`=user.`id`
            ORDER BY modified DESC
            LIMIT 1
        ) AS `is_opted_in_for_email`,
        (
            SELECT modified
            FROM user_api_userorgtag
            WHERE org IN ( {org_list} )
            AND `key`=\"email-optin\"
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
    org_list=','.join(['%s'] * len(org_list)),
    course_id_list=','.join(['%s'] * 1)
)

print(f"Number of %s in query: {query.count('%s')}")
