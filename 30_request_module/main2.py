import requests

url = "https://jsonplaceholder.typicode.com/posts"

r = requests.get(url)
# print(r)
json_text = r.json()
text = r.text
# print(json_text)

with open('append.txt','a')as f:
    f.write(text)
    print('DONE!')
    

