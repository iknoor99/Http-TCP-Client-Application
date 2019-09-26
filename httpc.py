import argparse
from http import http

parser = argparse.ArgumentParser(description='httpc is a curl-like application but supports HTTP protocol only.',
                                 epilog='''Use "httpc help [command]" for more information about a command.''')

subparser = parser.add_subparsers(dest='start')

parserget = subparser.add_parser('get',help='get executes a HTTP GET request and prints the response.')
parserget.add_argument('-v', action='store_true', help='Prints the detail of the response such as protocol, status,and headers.')
parserget.add_argument('-H', action='store_true', help='''Associates headers to HTTP Request with the format 'key:value'.''')

parserpost = subparser.add_parser('post',help='post executes a HTTP POST request and prints the response.')
parserpost.add_argument('-v', action='store_true', help='Prints the detail of the response such as protocol, status,and headers.')
parserpost.add_argument('-H', action='store_true', help='''Associates headers to HTTP Request with the format 'key:value'.''')
parserpost.add_argument('-d', help='string Associates an inline data to the body HTTP POST request.')
parserpost.add_argument('-f', action='store_true', help='Associates the content of a file to the body HTTP POST request')

parser.add_argument('URL')

mainargs = parser.parse_args()

print(mainargs.v)
print(mainargs.H)
print(mainargs.d)

class httpc:

    def __init__(self, mainargs):
        self.mainargs = mainargs

    def create_header(self,header,bodyvalue):  # to convert header dictionary to header_string

        header_string = ""
        if "Content-Type" in header:
            pass
        else:
            header["Content-Type"] = "application/json"
        if "Content-Length" in header:
            pass
        else:
            header["Content-Length"] = str(len(bodyvalue))

        for key, value in header.items():
            header_string = header_string + key + ": " + value + "\r\n"
        return header_string

    def start_request(self):
        print("request started")

        if self.mainargs.start =='get':
            print("request for get")

            if self.mainargs.v: # for checking verbose
                print("it is verbose")

            if self.mainargs.H:
                pass

            getobj = http(self.mainargs.URL, '', '')
            getobj.get_request()

        elif self.mainargs.start =='post':

            print("request for post")
            headdata={'User-Agent': 'Concordia-HTTP/1.0'}
            inlinedata=""
            maindict = {}

            if self.mainargs.H is not None:
                pass

            if self.mainargs.d is not None: # for inline data
                print("it is inline")

                for dic in [headdata, self.mainargs.d]:
                    maindict.update(dic)

                inlinedata=self.mainargs.d

            elif self.mainargs.f:
                print("it is file")

            finalheader=self.create_header(maindict,inlinedata)
            print("finalheader:-"+finalheader)
            print("inlinedata:-"+inlinedata)
            postobj = http(self.mainargs.URL, finalheader, inlinedata)
            postobj.post_request()

        else:
            print("check your request")

httpc(mainargs).start_request()









