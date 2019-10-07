import requests
url='https://mail.protonmail.com/login'
values={'username':'mdsalmanansari','password':'abcd'}
r=requests.post(url,data=values)
print("scuccess")
r=requests.post(url='https://mail.protonmail.com/logout')
print(r.content)