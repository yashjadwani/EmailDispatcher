import smtplib
import socket
import ssl

userName = "" #Your username
context = ssl.create_default_context()
def sendMail(toList, sendermail, password, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com',  587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sendermail,password)
        for recivermail in toList:
            content = 'From: {}<{}>\nTo: <{}>\nSubject: {}\n\n{}'.format(userName, sendermail, recivermail, subject, message)
            server.sendmail(sendermail, recivermail, content)
        server.close()
    except socket.gaierror:
        print("Please Check Your Internet Connection")
        exit()
    except smtplib.SMTPAuthenticationError:
        print("The username and/or password you entered is Incorrect.")
        exit()
    except Exception as e:
        print(e)
        exit()
