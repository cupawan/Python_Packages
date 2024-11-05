import os
import pytz
import logging
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

class SendEmail:
    def __init__(self,is_html = False):
        self.is_html = is_html
        ist = pytz.timezone('Asia/Kolkata')
        self.today = datetime.datetime.today().astimezone(ist).strftime('%d-%m-%y')
        self.send_from = os.environ['SendFrom']
        self.app_password = os.environ['GmailAppPassword']
    
    def send_email(self, send_to, subject, email_body, file_paths = None):
        msg = MIMEMultipart()
        msg['From'] = self.send_from
        msg['To'] = send_to
        msg['Subject'] = f"{self.today} {subject.strip()}"
        if not self.is_html:
            msg.attach(MIMEText(email_body, 'plain'))
        else:            
            msg.attach(MIMEText(email_body, 'html'))
        if file_paths and isinstance(file_paths,list):
            for file_path in file_paths:
                attachment = open(file_path, 'rb')
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= " + file_path.split("/")[-1])
                msg.attach(part)
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(self.send_from, self.app_password)
            server.sendmail(self.send_from, send_to, msg.as_string())
            return {'Status': 'Success'}