import smtplib
from email.mime.text import MIMEText
import os
import util

if __name__ == "__main__":
    f = open(util.get_target_file_from_argv1(), 'r', encoding='utf-8')
    msg_from = f.readline().split("=")[-1].strip()
    msg_to = f.readline().split("=")[-1].strip()
    passwd = f.readline().split("=")[-1].strip()
    subject = f.readline().split("=")[-1].strip()
    f.readline()
    content = ""
    for line in f.readlines():
        content += line

    msg = MIMEText(content, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = msg_from
    msg["To"] = msg_to

    try:
        s = smtplib.SMTP_SSL("smtp.163.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print("发送失败")
    finally:
        s.quit()
