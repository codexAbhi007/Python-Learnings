import json, requests

r = requests.get('https://jsonplaceholder.typicode.com/posts')

# print(r.text)
# print(type(r.text))
text = r.text
data = json.loads(text)
# print(type(data))
data_final_text = json.dumps(data,indent=2)
data_final = json.loads(data_final_text)

# print(data_final)

for obj in data_final:
    print(obj['body'])
    print()