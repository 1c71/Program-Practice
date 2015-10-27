
'''

要改,下面这些只是个服务器而已,
没法自定义发内容

'''


import socket

HOST = ''
PORT = 8030
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET
# socket.SOCK_STREAM
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
connection, address = listen_socket.accept()
request = connection.recv(1024)
connection.sendall("""HTTP/1.1 200 OK
Content-type: text/html


<html>
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>""")
connection.close()
