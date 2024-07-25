# DevNote


---
first_name: Aakash
last_name: Soni
email: aakash.soni@yopmail.com
mob_number: 9800001234
pwd: Aakash1212


---
Demo:

-) User Registration with 
  - invalid email id
  - existing email id
  - alpha in mob_number 
  - missing password

-) User Access About page with 
  - without login

-) User Activate link with 
  - invalid 
  - valid link

-) User Access About page with 
  - with login cred


-> Register Page:
http://localhost:8000/users/register/

-> Activation Page:
http://localhost:8000/users/activation/?email=aas@gmail.com&activation_slug=fa8097ea-b1da-43d8-b04a-7395697e3e6a_x

-> Login Page:
http://localhost:8000/users/login/

-> About Page:
http://localhost:8000/users/about/


```
(venv) ashishsondagar@../auth_dj$ pwd
/Users/ashishsondagar/Documents/code/others/auth_dj

(venv) ashishsondagar@../auth_dj$ python3 cafe_mgmt/utils/send_email.py
Failed to send email: (421, b'Domain sandbox9788fd2d07244b52aedb93860dbd216b.mailgun.org is not allowed to send: Free accounts are for test purposes only. Please upgrade or add the address to authorized recipients in Account Settings.')

(venv) ashishsondagar@../auth_dj$
```