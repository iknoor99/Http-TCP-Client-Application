import socket

class http:
    count = 0

    def __init__(self, url, body, headers, is_verbose, is_write, output_file, req_type):  # constructor to add values

        self.port = 80
        self.host = ""
        self.url = url
        self.body = body
        self.header = headers
        self.is_verbose = is_verbose
        self.is_write = is_write
        self.output_file = output_file
        self.reply_header = {}
        self.req_type = req_type
        self.path = ""


    def display_msg(self, msg):
        header_l = msg.split('\r\n\r\n')
        str_upper = header_l[0]
        str_lines = str_upper.split('\r\n')
        first_line = str_lines[0].split(' ')
        resp_code = first_line[1]
        resp_msg = ""
        for j in range(2, len(first_line)):
            resp_msg += first_line[j] + " "
        for line in range(1, len(str_lines)):
            string_h = str(str_lines[line])
            pos = string_h.find(":")
            pos = pos
            key_r = string_h[0:pos].strip()
            pos = pos+1
            length = len(string_h)
            value_r = string_h[pos:length]
            self.reply_header[str(key_r)] = str(value_r).strip()
        #print(self.reply_header)
        resp_num = int(resp_code)
        if (resp_code == "301" or resp_code == "302" or resp_code == "300" or (resp_num > 300 and resp_num < 400)) and self.count <= 5:
            if 'Location' in self.reply_header.keys():
                url_r = self.reply_header['Location']
                #if self.host in url_r:
                if ("http://" in url_r) or ("https://" in url_r) or ("www." in url_r):
                    self.url = url_r
                    self.url_break(self.url)
                else:
                    url_s = self.host + url_r
                    self.url = url_s
                print("Redirecting to new URL:" + str(self.url))
                if self.req_type == "get":
                    self.get_request()
                elif self.req_type == "post":
                    self.post_request()
            else:
                print("There is no Redirecting URL in the Server Response")


        if self.is_write:
            file_o = open(self.output_file, "w")
            for body_line in range(1, len(header_l)):
                file_o.write(header_l[body_line])
            file_o.close()
            if self.is_verbose:
                print("\nOutput:")
                print("\nProtocol: ")
                print(first_line[0])
                print("\nResponse code: ")
                print(resp_code)
                print("\nResponse message: ")
                print(resp_msg)
                print("\nHeaders:")
                for line in range(1, len(str_lines)):
                    print(str_lines[line])
        elif self.is_verbose:
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
            print("\nBody: ")
            for body_line in range(1, len(header_l)):
                print(header_l[body_line])
        else:
            print("\nOutput: \n")
            for body_line in range(1, len(header_l)):
                print(header_l[body_line])


    def get(self, request):
        self.count = self.count + 1
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.host, self.port))
            client.send(request.encode("utf:8"))
            response = client.recv(4096)
            response = response.decode("utf:8")
            #print("Response: \n\n" + str(response))
            self.display_msg(response)
        except OSError as err:
            print(err)
        finally:
            client.close()


    def post(self, request):
        self.count = self.count + 1
        #print("count is" + str(self.count))
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.host, self.port))
            client.send(request.encode("utf-8"))
            response = client.recv(4096)
            response = response.decode("utf-8")
            #print("Response: \n\n" + str(response))
            self.display_msg(str(response))
        except OSError as err:
            print("Error!")
            print(err)
        finally:
            client.close()

    def url_break(self, url):
        #print("In url_break :   " + url)
        if url.startswith('https://'):
            len_u = len(url)
            url = url[8:len_u]
        elif url.startswith('http://'):
            len_u = len(url)
            url = url[7:len_u]
        pos = url.find('/')
        pos1 = url.find('?')
        if pos >=0:
            self.host = url[0:pos]
            #print("Host is  " + self.host)
            self.path = url[pos:len(url)]
            #print("Path is  " + self.path)
        elif pos1 >=0:
            self.host = url[0:pos1]
            #print("Host is  " + self.host)
        else:
            self.host = url[0:len(url)]
            #print("Host is  " + self.host)



    def post_request(self):
        self.url_break(self.url)
        if self.path == "":
            self.path = "/"
        request = "POST " + self.path + " HTTP/1.1\r\n" + "Host: " + self.host+"\r\n" + self.header+"\r\n" + self.body
        #print("request is as follows :-")
        #print(request)
        self.post(request)

    def get_request(self):
        self.url_break(self.url)
        if self.path == "":
            self.path = "/"
        request = "GET " + self.path + " HTTP/1.1\r\n" + "Host: " + self.host+"\r\n" + self.header+"\r\n"
        #print("request is as follows :-")
        #print(request)
        self.get(request)
