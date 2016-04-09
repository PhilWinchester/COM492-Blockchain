'''
    Phil and Tom's COM492 Blockchain Research
    User file
'''

import hashlib
import uuid


class User:
    def __init__(self):
        self.is_user = True
        self.us_name = ""
        self.us_pass = ""
        self.user_ID = 0
        self.user_pass = ""
        self.user_private_key = ""
        self.user_public_key = ''

        self.us_text = open("userNames.txt","r+",encoding="utf-8")
        self.us_text = self.us_text.read()
        self.split_text = self.us_text.split()
        self.pass_text = open("userPasswords.txt","r+",encoding="utf-8")
        self.pass_text = self.pass_text.read()
        self.split_ptext = self.pass_text.split()

    def sign_in(self):
        # print(self.split_text)
        # print(self.split_ptext)

        self.us_name = input("Enter your username: ")
        if self.us_text.find(self.us_name) == -1:
            print("not in")
            self.split_text.append(self.us_name)
            self.user_ID = len(self.split_text)
            print("We don't have you in our servers. We'll make you a user after you enter "
                  "a password")
            self.user_pass = input("Enter your new password: ")
            self.split_ptext.append(self.user_pass)

            # update to have all passwords hashed and check against that user input password

            self.user_private_key = self.hash_password(self.us_pass)
            self.user_public_key = self.generate_public_key()

        else:
            self.user_ID = self.split_text.index(self.us_name)
            self.user_pass = self.split_ptext[self.user_ID]
            self.us_pass = input("Enter your password: ")
            self.user_private_key = self.hash_password(self.us_pass)
            self.user_public_key = self.generate_public_key()

        print("You are logged in as " + str(self.us_name))
        print("You are the " + str(self.user_ID + 1) + "th user")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return self.user_ID

    def hash_password(self, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    def generate_public_key(self):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + self.user_private_key.encode()).hexdigest() + ':' + salt

    def handshake(self):
        print("Generate Handshake b/w users to")

