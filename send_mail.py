import smtplib
import ssl,os
from dotenv import load_dotenv

load_dotenv()

def send_email(news):    
    # Enlisting Host name and port 
    host = "smtp.gmail.com"
    port = 465
    
    #Sender Info
    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("APP_PASSWORD")
    
    #Receiver Info
    receiver_email = os.getenv("RECEIVER_EMAIL")
    
    # Context
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(host, port,context=context) as server:
            server.login(sender_email,app_password)
            server.sendmail(sender_email,receiver_email,news)
    except Exception as err:
        print(err)