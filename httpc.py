from http import http

class httpc:

    def __init__(self, inputlist):
        print("inside constructor")
        self.inputlist = inputlist
        self.headerdict = {}
        self.remove_index = []
        self.host = ""
        self.path = ""

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
        inline_flag = False
        flag_g = False
        flag_p = False
        is_write = False
        output_file = ""
        URL = ""


        for i in range(0,len(self.inputlist)):

            if(self.inputlist[i]=='get'):
                flag_g = True

            elif (self.inputlist[i] == 'post'):
                flag_p = True

        print(self.inputlist)

        if (not flag_p) and flag_g:
            flaggetpost = "get"
            self.inputlist.remove("get")
        elif flag_p and not flag_g:
            flaggetpost = "post"
            self.inputlist.remove("post")
        elif flag_g and flag_p:
            print("\n\n Command contains both get and post. Exiting the program!")
            exit()
        elif not flag_g and not flag_p:
            print("\n\n Command contains neither get nor post. Exiting the program!")
            exit()

        for i in range(0, len(self.inputlist)):
            if (self.inputlist[i] == '-h'):
                self.header_dic(i, self.inputlist)

            if (self.inputlist[i] == '-v'):
                verflag = True
                self.remove_index.append(i)

            if (self.inputlist[i] == '-o'):
                is_write = True
                output_file = self.inputlist[i+1]
                self.remove_index.extend((i,i+1))

            if (flaggetpost =='post' and self.inputlist[i] == '-f'):
                fileflag = True
                fileloc = self.inputlist[i+1]
                self.remove_index.extend((i, i + 1))

            if (flaggetpost =='post' and self.inputlist[i] == '-d'):
                fileflag = False
                inline_flag = True
                #bodyvalue = self.inputlist[i+1]
                self.remove_index.append(i)

        self.remove_index.sort(reverse=True)
        print(self.remove_index)
        for i in self.remove_index:
            self.inputlist.remove(self.inputlist[i])
            print(self.inputlist)

        for i in range(0, len(self.inputlist)):
            string_u = str(self.inputlist[i])
            if string_u.startswith('http://') or string_u.startswith('https://') or string_u.startswith('www.'):
                print("url found")
                URL = string_u
                print("URL is:" + URL)
                self.inputlist.remove(URL)
                break

        if inline_flag:
            string_m = ""
            for i in range(0, len(self.inputlist)):
                string_m += str(self.inputlist[i]) + " "
            print("Body is" + string_m)
            bodyvalue = string_m


        print(self.inputlist)
        print("flaggetpost value: " + flaggetpost)
        print("header dictionary")
        print(self.headerdict)

        if(flaggetpost=='get'):
            print("inside get command")
            header_string = self.create_header(self.headerdict, bodyvalue)
            http(URL, bodyvalue, header_string, verflag, is_write, output_file, flaggetpost).get_request()

        elif(flaggetpost=='post'):
            print("inside post command")
            if fileflag:
                file = open(fileloc, "r")
                bodyvalue = file.read()
                file.close()
            header_string = self.create_header(self.headerdict, bodyvalue)
            http(URL, bodyvalue, header_string, verflag, is_write, output_file, flaggetpost).post_request()

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
                self.remove_index.extend((index, index + 1,index+2))
            else:                                          # --- KEY:VALUE
                split_head = next_val.split(':')
                key = split_head[0].strip()
                value = split_head[1].strip()
                self.headerdict[key] = value
                self.remove_index.extend((index, index + 1))
        else:
            key = next_val.strip()
            if input_list[index+2].strip() == ":":   # ---- KEY : VALUE
                value = input_list[index+3]
                self.remove_index.extend((index, index + 1, index + 2,index+3))
            else:                                       #  ----- KEY :VALUE
                value = input_list[index+2].replace(":", "")
                value = value.strip()
                self.remove_index.extend((index, index + 1, index + 2))
            self.headerdict[key] = value


inputstring = input("Please enter the command:\n")
inputarr = inputstring.split(" ")

if(inputarr[0] == 'httpc'):
    httpc(inputarr[1:]).check_string()