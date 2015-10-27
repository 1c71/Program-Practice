
import httplib2


h = httplib2.Http(timeout=5)
# 超时时间是5秒


resp, content = h.request("http://localhost/Output-All-Request-Header.php",
                          "GET",
                          headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.10 Safari/537.11'}
                          )

# print (resp)
print (content)






# tip: 不设置User-Agent的话, 默认的User-Agent是Python-httplib2/0.8 (gzip)
