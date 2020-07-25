import getpass
import emailDispatcher as ed
import re 

def emailChecker(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):
        return True
    else:
        return False

if __name__ == '__main__':
    try:
        file=open("email.txt","r")
        ReciverList = []
        BadEmailList = []

        senderEmail = "" #sender's Email Address
        password = getpass.getpass(prompt='Password: ')
        subject = input("Subject : ")
        message = input("Message : ")


        for name in file:
            if (name.strip() != ''):
                if (emailChecker(name.strip())):
                    ReciverList.append(name.strip())
                else:
                    BadEmailList.append(name.strip())

        if (len(ReciverList) != 0):
            ed.sendMail(ReciverList,senderEmail,password,subject,message)
            print("Sent Successfully")
        if (len(BadEmailList) != 0):
            if (len(ReciverList) == 0):
                print("No valid Address in the File.")
            else:
                print("There were Some wrong Emails!")
                for list in BadEmailList:
                    print(list)
        if (len(ReciverList) == 0 and len(BadEmailList) == 0):
            print("File is empty")
    except FileNotFoundError:
        print("No such file or directory!")

