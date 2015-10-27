
import httplib2

h = httplib2.Http()
resp, content = h.request("http://localhost/Output-All-Request-Header.php")

# print (resp)
print (content)


