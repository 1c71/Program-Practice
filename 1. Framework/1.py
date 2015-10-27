# http://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/
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
