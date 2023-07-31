import smtplib


def send_email(msg):
    sender = 'rtln@anorbank.local'
    password = 'M0ibDuhPSP'
    recipient = 'botir.islamov@anorbank.uz'
    server = smtplib.SMTP('192.168.133.107', 25)
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