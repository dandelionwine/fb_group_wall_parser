import fb
import sql
import amz
import re
import facebook



sql.create_database()

for i in fb.group_ids:
    fb.search_rsps(i)

# for i in fb.group_ids:
#     fb.check_fb(i)

# for i in sql.get_links():
#     if fb.find_facebook(i[0]) == True:
#         try:
#             if amz.check(i[0]) == True:
#                 sql.set_free(i[0])
#             else:
#                 sql.set_unfree(i[0])
#         except Exception:
#             pass
#     else:
#         if amz.check(i[0]) == True:
#             sql.set_free(i[0])
#         elif amz.check(i[0]) == False:
#             sql.set_unfree(i[0])

sql.transfer_database()
