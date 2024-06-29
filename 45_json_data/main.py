import json

string = '''
{
  "users": [
    {
      "id": 1,
      "name": "Alice",
      "email": "alice@example.com",
      "active": true,
      "roles": ["admin", "user"]
    },
    {
      "id": 2,
      "name": "Bob",
      "email": "bob@example.com",
      "active": false,
      "roles": ["user"]
    },
    {
      "id": 3,
      "name": "Charlie",
      "email": "charlie@example.com",
      "active": true,
      "roles": ["user", "editor"]
    }
  ]
}

'''

data = json.loads(string)
# print(data)
# print(type(data))


data2 = json.loads(string)
for user in data2['users']:
    print(user)
    del user['active']


new_string = json.dumps(data2,indent=2,sort_keys=True)

print(new_string)
