import smtplib ,webbrowser
import getpass
from tkinter import *
from tkinter import filedialog
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
Exit=False
def get_mail():
    servicesAvailable = ['hotmail','gmail','yahoo','outlook']
    while True:
        print("---------------------------------------")
        mail_id = input("Enter  E-mail address here : ")
        if '@' in mail_id and '.com' in mail_id:
            symbol_pos = mail_id.find("@")
            dotcom_pos = mail_id.find(".com")
            sp = mail_id[symbol_pos+1:dotcom_pos]
            if sp in servicesAvailable:
                return mail_id ,sp
                break
            else:
                print("we don't provide service for "+sp)
                print("we provide service only  for : hotmail/gmail/yahoo/outlook")

        else:
            print("invalid E-mail retype again ")
            continue


def set_smtp_domain(serviceProvider):
    if serviceProvider == 'gmail':
        return "smtp.gmail.com"
    elif serviceProvider == "outlook" or serviceProvider =='hotmail':
        return "smtp-mail.outlook.com"
    elif serviceProvider == 'yahoo':
        return "smtp.mail.yahoo.com"
def file_dailog_box():
    root= Tk()
    root.withdraw()
    file_name = filedialog.askopenfilenames(initialdir="/home/",title = "Selec a file")
    if file_name is not None:
        print("Your file path is : "+file_name[0])
        attachemt = open(file_name[0],"rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachemt).read())
        encoders.encode_base64(p) 
        p.add_header('Content-Disposition',"attachment; file_name= %s" % file_name)
        msg.attach(p)
        text = msg.as_string()
        connection.sendmail(e_mail,receiverAddress,text)
        print("E-mail send successfully")
        connection.quit()
        

    else:
        print("User need select a file here ")




print('Wellcome you can send an E-mail through this program ')
print('Please enter your E-mail and password :')
e_mail ,serviceProvider = get_mail()
print("your service Provider is "+serviceProvider)
print("-----------------------------------------")
password = getpass.getpass(prompt = "Enter your password here :")

while True:
    try:
        smtpDomain = set_smtp_domain(serviceProvider)
        connection = smtplib.SMTP(smtpDomain,587)
        connection.ehlo()
        connection.starttls()
        connection.login(e_mail,password)
    except:
        if serviceProvider == 'gmail':
            print('Login unsuccessfull , there are two possible reasons : ')
            print("1.) you typed wrong username or password")
            print("2.) you are using Gmail there is an option in gmail 'allow less security")
            print("DO you want us to open a webpage from where you can enable this option ")
            print("------------------------------------------------------------------------")
            enter = input("yes or no ? ")
            if enter == "yes":
                webbrowser.open("https://myaccount.google.com/lesssecureapps")
            else:
                print("we won't open webpage for you ")
            
            print("Please retype your e-mail and password also ")
            e_mail,serviceProvider = get_mail()
            password = getpass.getpass(prompt = "Enter your password here :")
            continue
        else:
            print('Login unsuccessfull , most possible you typed wrong username or password : ')
            print( " please retype your e-mail address or password")
            print("-----------------------------------------------")
            e_mail,serviceProvider = get_mail()
            password = getpass.getpass(prompt = "Enter your password here :")
            continue
    else:
        print("login successfull")
        break

print("Please type receiver's E-mail address  ")
receiverAddress,receiverSP = get_mail()
print("please type subject and message ")
msg = MIMEMultipart()
msg['FROM'] = e_mail
msg['TO'] = receiverAddress
msg['Subject'] = input("Subject: ")
Body = input("Enter the body of mail ")
msg.attach(MIMEText(Body,'plain'))
print("If you want send a file(yes/no)")
print("--------------------------------")


while True:
    try:
        enter=input("enter your choice here ")
        if enter == "yes":
            file_dailog_box()
            break
        elif enter == "no":
            text = msg.as_string()
            connection.sendmail(e_mail,receiverAddress,text)
            print("E-mail send successfully")
            connection.quit()
            break
        else:
            print("please enter correct input")
    except ValueError:
        print("Invalid Choice. ")