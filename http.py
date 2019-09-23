import socket

class http:

    def get(self,host,port):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host,port))

        request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
        client.send(request.encode("utf:8"))

        response = client.recv(4096)
        response = response.decode("utf:8")

        print(response)

    def post(self,host,port):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host,port))

        request = "POST / HTTP/1.1\r\nHost:%s\r\n\r\n" % host

        #message = "POST /auth HTTP/1.1\r\n"
        #parameters = "userName=Ganesh&password=pass\r\n"

        contentLength = "Content-Length: " + str(len(request))
        contentType = "Content-Type: application/x-www-form-urlencoded\r\n"

        finalMessage = request + contentLength + contentType + "\r\n"

        client.send(finalMessage.encode("utf:8"))

        response = client.recv(4096)
        response = response.decode("utf:8")

        print(response)

http().post("www.google.com",80)









