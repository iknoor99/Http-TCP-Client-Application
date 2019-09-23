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

        request = "POST /post HTTP/1.1\r\nHost: %s" % host

        create_header = {'User-Agent': 'Concordia-HTTP/1.0',
              'Content-Type': 'application/json',
              'Content-Length': '14'
              }

        start = "\r\n"

        for key,value in create_header.items():
            start += key + ": " + value
            start +="\r\n"

        payload = request+start+"\r\n{Assignment:1}"

        client.send(payload.encode("utf-8"))

        response = client.recv(4096)
        response = response.decode("utf-8")

        print(response)

http().post("httpbin.org",80)









