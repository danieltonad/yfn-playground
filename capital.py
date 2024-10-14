import http.client, json
from requests import Session


HOST = "https://api-capital.backend-capital.com"

with Session() as session:
  
  # ping
  # res = session.get(f"{HOST}/api/v1/time")
  # print(res.text)



  # gen key
  # headers = {
  #   'X-CAP-API-KEY': 'ohPOsfVU6kQlmL5x'
  # }
  # res = session.get(f"{HOST}/api/v1/session/encryptionKey", headers=headers)
  # print(res.text)


  # new session
  payload = json.dumps({
    "identifier": "daposodipo@gmail.com",
    "password": "Kikimusampa2022@"
  })
  headers = {
    'X-CAP-API-KEY': 'ohPOsfVU6kQlmL5x',
    'Content-Type': 'application/json'
  }
  res = session.post(f"{HOST}/api/v1/session", headers=headers, data=payload)
  header: dict = res.headers
  CST = header.get("CST")
  X_SECURITY_TOKEN = header.get("X-SECURITY-TOKEN")
  


  # session
  # headers = {
  #   'X-SECURITY-TOKEN': X_SECURITY_TOKEN,
  #   'CST': CST
  # }
  # res = session.get(f"{HOST}/api/v1/session", headers=headers)
  # print(res.text)

  # mkt
  headers = {
    'X-SECURITY-TOKEN': X_SECURITY_TOKEN,
    'CST': CST
  }
  res = session.get(f"{HOST}/api/v1/markets", headers=headers)
  print(res.text)
