import socket
from urllib.parse import urlparse

class http:
    count = 0

    def __init__(self, url, body, headers, is_verbose, is_write, output_file, req_type):  # constructor to add values

        self.port = 80
        self.host = urlparse(url).netloc
        self.url = url
        print("Host is " + self.host)
        self.body = body
        self.header = headers
        self.count = 0
        self.is_verbose = is_verbose
        self.is_write = is_write
        self.output_file = output_file
        self.reply_header = {}
        self.req_type = req_type

    def display_msg(self, msg):
        header_l = msg.split('\r\n\r\n')
        str_upper = header_l[0]
        str_lines = str_upper.split('\r\n')
        first_line = str_lines[0].split(' ')
        resp_code = first_line[1]
        resp_msg = first_line[2]
        for line in range(1, len(str_lines)):
            string_h = str(str_lines[line])
            #print("string is---        " + string_h)
            pos = string_h.find(":")
            pos = pos
            key_r = string_h[0:pos].strip()
            pos = pos+1
            length = len(string_h)
            value_r = string_h[pos:length]
            #print("In map  " + str(key_r) + "-" + str(value_r))
            self.reply_header[str(key_r)] = str(value_r).strip()
        print(self.reply_header)
        if (resp_code == "301" or resp_code == "302" or resp_code == "300") and self.count <= 5:

            url_r = self.reply_header['Location']
            #url_redirect = urlparse(url_r)
            #self.host = url_redirect.netloc
            self.host = url_r
            print("Redirecting to new URL:" + str(url_r))
            if self.req_type == "get":
                self.get_request()
            elif self.req_type == "post":
                self.post_request()

        if self.is_verbose:
            print("\nOutput:")
            print("\nProtocol: ")
            print(first_line[0])
            print("\nResponse code: ")
            print(resp_code)
            print("\nResponse message: ")
            print(resp_msg)
            print("\nHeaders:")
            for line in range(1,len(str_lines)):
                print(str_lines[line])
        elif self.is_write:
            file_o = open(self.output_file, "w")
            for body_line in range(1, len(header_l)):
                file_o.write(header_l[body_line])
            file_o.close()
        else:
            for body_line in range(1, len(header_l)):
                print(header_l[body_line])


    def get(self, request):
        self.count = self.count + 1
        #try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))
        client.send(request.encode("utf:8"))
        response = client.recv(4096)
        response = response.decode("utf:8")
        print("Response: \n\n" + str(response))
        self.display_msg(response)
        #except OSError as err:
            #print(err)
        #finally:
        client.close()


    def post(self, request):
        self.count = self.count + 1
        print("count is" + str(self.count))
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.host, self.port))
            client.send(request.encode("utf-8"))
            response = client.recv(4096)
            response = response.decode("utf-8")
            print("Response: \n\n" + str(response))
            self.display_msg(str(response))
        except OSError as err:
            print("Error!")
            print(err)
        finally:
            client.close()


    def post_request(self):
        request = "POST /post HTTP/1.1\r\n" + "Host: " + self.host+"\r\n" + self.header+"\r\n" + self.body
        print("request is as follows :-")
        print(request)
        self.post(request)

    def get_request(self):
        request = "GET / HTTP/1.1\r\n" + "Host: " + self.host+"\r\n" + self.header+"\r\n"
        print("request is as follows :-")
        print(request)
        self.get(request)
















