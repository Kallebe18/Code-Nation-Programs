import requests
import json

url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU-TOKEN"

answer = {"answer": open("answer.json","r")}

r = requests.post(url, files=answer)
print(r.content)
