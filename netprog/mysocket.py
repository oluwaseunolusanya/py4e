import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("data.pr4e.org", 80))
request = "GET http://data.pr4e.org/romeo-full.txt HTTP/1.0\r\n\r\n".encode()
mysocket.send(request)

while True:
    response = mysocket.recv(512)
    if (len(response) < 1):
        break
    print(response.decode())
mysocket.close()