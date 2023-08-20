import smtplib


def send_email(msg):
    sender = 'sender_mail'
    password = 'pass'
    recipient = 'recipient_mail'
    server = smtplib.SMTP('ip_address', 25)
    server.starttls()
    try:
        server.login(sender, password)
        server.sendmail(sender, recipient, f'Subject: Hello, very important message!\n {msg}')
        return 'message sent successfully..'

    except Exception as _ex:
        return f'check your credentials please {_ex}'

def main():
    msg = input('Enter your message please: ')
    send_email(msg=msg)

if __name__ == "__main__":
    main()