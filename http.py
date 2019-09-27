import socket
from urllib.parse import urlparse

class http:


    def __init__(self, url, body, headers):  # constructor to add values

        self.port = 80
        self.host = urlparse(url).netloc
        self.body = body
        self.header = headers
        self.count = 0

    def display_msg(self, msg):
        header_l = msg.split('\r\n\r\n')
        str_upper = header_l[0]
        str_lines = str_upper.split('\r\n')
        first_line = str_lines[0].split(' ')
        resp_code = first_line[1]
        print("\nResponse code: ")
        print(resp_code)
        resp_msg = first_line[2]
        print("\nResponse message: ")
        print(resp_msg)
        print("\nHeaders:")
        for line in range(1,len(str_lines)):
            print(str_lines[line])
        print("\nBody:")
        for body_line in range(1, len(header_l)):
            print(header_l[body_line])


    def get(self, request):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))
        client.send(request.encode("utf:8"))
        response = client.recv(4096)
        response = response.decode("utf:8")
        print(str(response))
        client.close()
        self.display_msg(response)


    def post(self, request):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.host, self.port))
            client.send(request.encode("utf-8"))
            response = client.recv(4096)
            response = response.decode("utf-8")
            print("Response: \n\n" + str(response))
            self.display_msg(str(response))
        except:
            print("Error receiving response!")
        finally:
            client.close()


    def post_request(self):
        request = "POST /post HTTP/1.1\r\n" + "Host: " + self.host+"\r\n" + self.header+"\r\n" + self.body
        print("request is as follows :-")
        print(request)
        self.post(request)

    def get_request(self):
        self.count += 1
        request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % self.host
        self.get(request)
















