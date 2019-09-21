import socket

class http:

    def get(self,host,port):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host,port))

        request = "GET / HTTP/1.0\r\nHost:%s\r\n\r\n" % host
        client.send(request.encode("utf:8"))

        response = client.recv(4096)
        response = response.decode("utf:8")

        print(response)

http().get("www.google.com",80)







