import argparse

parser = argparse.ArgumentParser(description='httpc is a curl-like application but supports HTTP protocol only.',
                                epilog='''Use "httpc help [command]" for more information about a command.''')

subparser = parser.add_subparsers()

parserget = subparser.add_parser('get' ,help='get executes a HTTP GET request and prints the response.')
parserget.add_argument('-v', action='store_true', help='Prints the detail of the response such as protocol, status,and headers.')
parserget.add_argument('-H', dest= 'key:value' ,action='store_true', help='''Associates headers to HTTP Request with the format 'key:value'.''')

parserpost = subparser.add_parser('post', help='post executes a HTTP POST request and prints the response.')
parserpost.add_argument('-v', action='store_true', help='Prints the detail of the response such as protocol, status,and headers.')
parserpost.add_argument('-H', dest= 'key:value' ,action='store_true', help='''Associates headers to HTTP Request with the format 'key:value'.''')
parserpost.add_argument('-d', action='store_true',help='string Associates an inline data to the body HTTP POST request.')
parserpost.add_argument('-f', action='store_true', help='Associates the content of a file to the body HTTP POST request')
mainargs = parser.parse_args()

class httpc:

    def __init__(self, mainargs):
        self.mainargs = mainargs

    def start_request(self):
        print("request started")
        print(self.mainargs)


httpc().start_request("okay")









