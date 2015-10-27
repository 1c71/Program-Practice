
import urllib2


req = urllib2.Request('http://localhost/Output-All-Request-Header.php')
#req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.10 Safari/537.11')
# 创建一个request对象


response = urllib2.urlopen(req)
# 利用这个对象去发请求


content = response.read()
print content
# 读取内容并输出



# ---- ---- ---- ---- ---- ---- ---- ---- ---- 
# 默认User-Agent是: Python-urllib/2.7

