#Extract data from Rest API
import requests,json
resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()
print(len(users))

users_json=[]
for user in users:
    users_json.append({
        'uid':user['id'],
        'uname':user['username'],
        'city':user['address']['city'],
        'company':user['company']['name']
    })
print(len(users_json))
print(users_json)
fp1=open('user.json','w')
json.dump(users_json,fp1)
fp1.close()
print("New Data file created")