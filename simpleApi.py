# PART OF ZDBYTE
# IN DEVELOPING
# GITHUB https://github.com/mahditmx
# MADE BY MAHDITMX
# http://database.pythonanywhere.com/

import request
import ZDbyte # FOR END TO END ENCRYPTION (optional)

class simpleApi:
    api_key = ""
    username = ""
    api_url = "http://database.pythonanywhere.com/api/"
    end_to_end_encryption = False
    encryption_key = ""
    def host_url(self,new_url):
        self.api_url = new_url


    def login(self,api_key,username,end_to_end_encryption=False,encryption_key=""):
        """`end-to-end encryption` is method for risky file"""
        self.end_to_end_encryption = end_to_end_encryption
        self.encryption_key = encryption_key
        self.api_key = api_key
        self.username = username
    def login_cheak(self):
        api_url = self.api_url + "/cheak_permissions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
        }

        response = requests.get(api_url, headers=headers)
        return response

    def file_list(self):

        api_url = self.api_url + "/file_list"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
        }

        response = requests.get(api_url, headers=headers)
        return response

    def create_file(self,fileName,format):

        api_url = self.api_url + "/create_file"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
            "filename":fileName,
            "format" : format
        }

        response = requests.get(api_url, headers=headers)
        return response

    def write_file(self,fileName,text,use_encryption=False):
        if self.end_to_end_encryption == True:
            if self.encryption_key != "":
                if use_encryption == True:
                    text = lock_text(self.encryption_key,text)
            else:
                return "encryption_key not set!"
        api_url = self.api_url + "/write_file"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
            "filename":fileName,
            "text":text
        }


        response = requests.get(api_url, headers=headers)
        return response


    def read_file(self,fileName,use_encryption=False):



        api_url = self.api_url + "/read_file"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
            "filename":fileName
        }


        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = eval(response.text)["text"]
            if self.end_to_end_encryption == True:
                if self.encryption_key != "":
                    if use_encryption == True:
                        data = unlock_text(self.encryption_key,data)
                        response = [response,data]
                        return response
                    else:
                        response = [response,data]
                        return response
                else:
                    return "encryption_key not set!"
            else:
                response = [response,data]
                return response

        response = [response,response.status_code]
        return response

    def remove_file(self,fileName):

        api_url = self.api_url + "/rm_file"


        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Username": self.username,
            "filename":fileName
        }


        response = requests.get(api_url, headers=headers)
        return response
