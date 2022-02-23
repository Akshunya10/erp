import json
import requests


ENDPOINT = 'http://127.0.0.1:8000/api/finance/po/'

CUSTOM_ENDPOINT = 'http://127.0.0.1:8000/api/auth/'

AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/jwt/'

# REFRESH_AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/jwt/refresh/'


headers = {
        'Content-Type':'application/json',
        # 'Authorization': 'JWT ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTg3ODE4OTc2LCJlbWFpbCI6InZpa2FzQGFkbWluLmNvbSIsIm9yaWdfaWF0IjoxNTg3ODE4Njc2fQ.Je8hBnzTrOS-18p8QksgG4g2nWO0NZRdNaKWARWBEhM',
}

data = {
    "username": "BillGates",
    "password": "gates@123"
}

r = requests.post(CUSTOM_ENDPOINT,data=json.dumps(data) ,headers = headers ) # 

token = r.json()['token']

print(token)


headers2 = {
        # 'Content-Type':'application/json',
        'Authorization': 'JWT ' + token
}

data2 = {
        "from_company": "amazon",
        "vendor_name": "jeffery",
        "PO_Number": "PO123",
        "PO_Date": "2020-04-21",
        "Total": 0.0,
        # "user": 3,
        "vendor": "jeffffffffff"
}

r = requests.put(ENDPOINT + str(3) + '/' ,data=data2 ,headers = headers2 ) # 


print(r.text)









# ENDPOINT = 'http://127.0.0.1:8000/api/auth/register/'

# CUSTOM_ENDPOINT = 'http://127.0.0.1:8000/api/auth/'

# AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/jwt/'

# # REFRESH_AUTH_ENDPOINT = 'http://127.0.0.1:8000/api/auth/jwt/refresh/'


# headers = {
#         'Content-Type':'application/json',
#         # 'Authorization': 'JWT ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTg3ODE4OTc2LCJlbWFpbCI6InZpa2FzQGFkbWluLmNvbSIsIm9yaWdfaWF0IjoxNTg3ODE4Njc2fQ.Je8hBnzTrOS-18p8QksgG4g2nWO0NZRdNaKWARWBEhM',
# }

# data = {
#     "username": "vishal110",
#     "email": "vish@vv.com",
#     "password": "kumar@110",
#     "password2": "kumar@110"
# }

# r = requests.post(ENDPOINT,data=json.dumps(data) ,headers = headers ) # 

# token = r.json()

# print(token)





# headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'JWT ' + token,
# }

# data = {"first_name": "shubam",
#         "last_name": "yadav",
#         "email_id": "shub@leanvia.com",
#         "dob": "2020-04-18",
#         "contact": "123456",
#         "address_1": "sector 20",
#         "address_2": "phase2",
#         "city": "chd",
#         "state": "chandigarh",
#         "country": "India",
#         "zip_code": "160001",
#         "govt_id": "passport",
#         "id_no": "pass122223",
#         # "employee_id": "",
#         "p_id1": "twitter",
#         "p_id2": "https://www.google.com/twitterrrrrrr",
#         "company_code": "lean tech",
#         "position": "staff",
#         "username": 2,

#         }

# json_data = json.dumps(data)

# post_response = requests.post(ENDPOINT, data = json_data, headers= headers)

# print(post_response.text)




# refresh_data = {
#         'token':token
# }
# new_r = requests.post(AUTH_ENDPOINT + 'refresh/',data=json.dumps(refresh_data),headers = headers )

# new_token = new_r.json()['token']

# print(new_token)




# data = {"first_name": "deepak",
#         "last_name": "singh",
#         "email_id": "singh@leanvia.com",
#         "dob": "2020-04-18",
#         "contact": "123456",
#         "address_1": "sector 20",
#         "address_2": "phase2",
#         "city": "chd",
#         "state": "chandigarh",
#         "country": "India",
#         "zip_code": "160001",
#         "govt_id": "passport",
#         "id_no": "pass12333",
#         "employee_id": "lete000005",
#         "p_id1": "twitter",
#         "p_id2": "https://www.google.com/twitterrr",
#         # "upload_documents": null,
#         "company_code": "lean tech",
#         "position": "staff",
#         # "staff": true,
#         # "admin": false,
#         # "hr": false,
#         # "manager": false,
#         # "active": false,
#         "username": 2}


# post_data = json.dumps(data)

# post_headers = {'content-type':'application/json'}

# post_response = requests.put(ENDPOINT, data= post_data , headers = post_headers)
# print(post_response.text)