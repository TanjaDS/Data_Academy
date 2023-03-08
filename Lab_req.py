import requests
import json

if __name__ == '__main__':
    r = requests.get('http://127.0.0.1:5000/user')
    res_dict = r.json()
    for user in res_dict['users']:
        print(user['id'])
    print(res_dict)

