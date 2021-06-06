from django.test import TestCase
import requests

r = requests.post('http://localhost:8080/api/auth/login/', {
  "username": "vivekascoder",
  "password": "123"
})

print(r.status_code)
print(r.json())