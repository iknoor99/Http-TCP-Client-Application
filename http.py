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

    def post(selfself,host,port):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host,port))

        request = "POST / HTTP/1.1\r\nHost:%s\r\n\r\n" % host

        headers = """\
        POST /auth HTTP/1.1\r
        Content-Type: {content_type}\r
        Content-Length: {content_length}\r
        Host: {host}\r
        Connection: close\r
        \r\n"""

        header_bytes = headers.format(
            content_type=" text/html",
            content_length=3000,
            host=str(host) + ":" + str(port)
        )

        request1=request+header_bytes

        client.send(request1.encode("utf:8"))

        response = client.recv(4096)
        response = response.decode("utf:8")

        print(response)

http().post("www.google.com",80)








