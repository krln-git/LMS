import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("CREATE TABLE users (id INT, org TEXT, course TEXT)")

org_aliases = ['org1']
courses = ['course1']

query = """
SELECT id FROM users
WHERE org IN ( {org_list} )
AND org IN ( {org_list} )
AND course IN ( {course_id_list} )
""".format(
    org_list=','.join(['?'] * len(org_aliases)),
    course_id_list=','.join(['?'] * len(courses))
)

print(query)

try:
    c.execute(query, org_aliases + courses)
    print("Success with single org_aliases!")
except Exception as e:
    print(f"Error single: {e}")

try:
    c.execute(query, org_aliases + org_aliases + courses)
    print("Success with double org_aliases!")
except Exception as e:
    print(f"Error double: {e}")
