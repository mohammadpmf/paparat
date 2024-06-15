import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders


def send_mail(send_from, send_to, subject, message, files=[],
              server="localhost", port=587, username='', password='',
              use_tls=True):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename={}'.format(Path(path).name))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

# توضیحات
# اولین ورودی اش اسمی هست که موقع دریافت ایمیل ما میبینیم. میتونه با اکانت ایمیل فرق داشته
# باشه. البته وقتی کامل فارسی می نوشتم ارور میداد. اما وقتی توش از یک حرف انگلیسی استفاده 
# میکردم دیگه گیر نمیداد.
# ورودی دوم، لیستی از اشخاصی که میخوایم بهشون ایمیل ارسال بشه
# ورودی سوم، عنوان ایمیل که میتونه کامل هم فارسی باشه
# ورودی چهارم، متن ایمیل هست که فارسی نوشتم و باز هم کار کرد
# ورودی پنجم، لیستی از فایل هایی که میخوایم به ایمیل ضمیمه شوند
# ورودی ششم، سروری که ایمیل را ارسال می کند
# ورودی هفتم، شماره پورت که 465 گذاشتم ارور میداد. دیفالتش 587 هست که کار میکنه
# ورودی هشتم، یوزر نیم
# ورودی نهم، اپ پسورد.
send_mail("M محمد پورمحمدی فلاح", ['mohammad.pfallah@gmail.com','shookooljooni254@gmail.com'],
        'یک ایمیل با ضمیمه', 'سلام\nاین یک ایمیل تستی است که ببینم چه طور میتوان با پایتون ایمیلی ارسال کرد که ضمیمه هم داشته باشد',
        [
            r'C:\Users\Mohammad\Desktop\Zabt Python\python codes\miscellaneous_codes\sending_email\s90_sending_simple_email.py',
            r'C:\Users\Mohammad\Desktop\Zabt Python\python codes\miscellaneous_codes\sending_email\s91_sending_email_with_attachments.py',
        ],
        'smtp.gmail.com', 587, 'shookooljooni254@gmail.com', 'flpofeulbmzjaehi')
# برای شما معتبر نیست. باید از اکانت جیمیل و اپ پسورد خودتون استفاده کنید
# و فایل ها هم قاعدتا با این آدرس روی سیستم شما نیستند
print("Email with attachments sent successfully!")