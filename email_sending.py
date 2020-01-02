import smtplib ,webbrowser
import getpass

def get_mail():
    servicesAvailable = ['hotmail','gmail','yahoo','outlook']
    while True:
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




print('Wellcome you can send an E-mail through this program ')
print('Please enter your E-mail and password :')
e_mail ,serviceProvider = get_mail()
print("your service Provider is "+serviceProvider)
password = getpass.getpass(prompt = "Enter your password here :",stream=None)

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
            print( "1.) you typed wrong username or password")
            print("2) you are using Gmail there is an option in gmail 'allow less security")
            print("DO you want us to open a webpage from where you can enable this option ")
            enter = input("yes or no ? ")
            if enter == "yes":
                webbrowser.open("https://myaccount.google.com/lesssecureapps")
            else:
                print("we won't open webpage for you ")
            
            print("Please retype your e-mail and password also ")
            e_mail,serviceProvider = get_mail()
            password = getpass.getpass(prompt = "Enter your password here :",stream=None)
            continue
        else:
            print('Login unsuccessfull , most possible you typed wrong username or password : ')
            print( " please retype your e-mail address or password")
            e_mail,serviceProvider = get_mail()
            password = getpass.getpass(prompt = "Enter your password here :",stream=None)
            continue
    else:
        print("login successfull")
        break

print("Please type receiver's E-mail address  ")
receiverAddress,receiverSP = get_mail()
print("please type subject and message ")
Subject = input("Subject: ")
Message = input("Message: ")
connection.sendmail(e_mail,receiverAddress,("Subject: " +str(Subject)+"\n\n"+str(Message)))
print("E-mail send successfully")
connection.quit()