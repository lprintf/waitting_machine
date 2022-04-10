import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import smtp_config


def make_message(
    subject:str="Python SMTP Test",
    content:str="test smtplib...",
    sender:str="lprintf",
    receiver:str="lprintf",
    ):
    message = MIMEText(content, "plain", "utf-8")
    message["Subject"] = Header(subject, "utf-8")
    message["From"] = Header(sender, 'utf-8')
    message["To"] = Header(receiver)
    return message


def send_email(
    smtp_config: smtp_config = smtp_config(),
    message=make_message(),
):
    try:
        smtpObj = smtplib.SMTP(smtp_config.relay_host_name, smtp_config.relay_host_port)
        if smtp_config.relay_auth:
            smtpObj.login(
                smtp_config.relay_auth_username, smtp_config.relay_auth_password
            )
        smtpObj.sendmail(
            smtp_config.sender_address, smtp_config.receivers, message.as_string()
        )
        print("Sent successfully!")
    except smtplib.SMTPException as e:
        print("Failed to send...")
        raise e


if __name__ == "__main__":
    send_email()
    
