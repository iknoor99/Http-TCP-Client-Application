from http import http

class httpc:

    def __init__(self, inputlist):
        print("inside constructor")
        self.inputlist = inputlist
        self.headerdict = {}

    def create_header(self, header, bodyvalue):  # to convert header dictionary to header_string

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

    def check_string(self):
        print("inside check string")
        flaggetpost = ""
        verflag = False
        headerval = ""
        bodyvalue = ""
        fileflag = ""
        fileloc = ""


        for i in range(0,len(self.inputlist)):

            if(self.inputlist[i]=='get'):
                flaggetpost='get'
                break

            elif (self.inputlist[i] == 'post'):
                flaggetpost='post'
                break

        for i in range(0, len(self.inputlist)):
            if (self.inputlist[i] == '-h'):
                self.header_dic(i, self.inputlist)

            if (self.inputlist[i] == '-v'):
                verflag = True

            if (flaggetpost =='post' and self.inputlist[i] == '-f'):
                fileflag = True
                fileloc = self.inputlist[i+1]

            if (flaggetpost =='post' and self.inputlist[i] == '-d'):
                fileflag = False
                bodyvalue = self.inputlist[i+1]

        print("flaggetpost value: " + flaggetpost)
        print("header dictionary")
        print(self.headerdict)

        if(flaggetpost=='get'):
            print("inside get command")
            getobj = http(self.inputlist[-1],headerval, bodyvalue)
            getobj.get_request()

        elif(flaggetpost=='post'):
            print("inside post command")
            if fileflag:
                file = open(fileloc, "r")
                bodyvalue = file.read()
            header_string = self.create_header(self.headerdict, bodyvalue)
            http('http://httpbin.org/post', bodyvalue, header_string).post_request()

    def header_dic(self, index, input_list):
        next_val = input_list[index+1].strip()
        pos = next_val.find(':')
        length = len(next_val) - 1
        if pos >= 0:      # colon is present in the next value
            if pos == length:         # colon is at the end of the value  -- KEY: VALUE
                key = next_val.replace(":", "")
                key = key.strip()
                value = input_list[index+2].strip()
                self.headerdict[key] = value
            else:                                          # --- KEY:VALUE
                split_head = next_val.split(':')
                key = split_head[0].strip()
                value = split_head[1].strip()
                self.headerdict[key] = value
        else:
            key = next_val.strip()
            if input_list[index+2].strip() == ":":   # ---- KEY : VALUE
                value = input_list[index+3]
            else:                                       #  ----- KEY :VALUE
                value = input_list[index+2].replace(":", "")
                value = value.strip()
            self.headerdict[key] = value

inputstring = input("Please enter the command:\n")
inputarr = inputstring.split(" ")

if(inputarr[0] == 'httpc'):
    httpc(inputarr[1:]).check_string()