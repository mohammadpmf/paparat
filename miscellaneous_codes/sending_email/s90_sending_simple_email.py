import smtplib, ssl
sender_email = "shookooljooni254@gmail.com" # برای شما معتبر نیست. باید از اکانت جیمیل خودتون استفاده کنید
password = "flpofeulbmzjaehi" # برای شما معتبر نیست. باید از اپ پسورد خودتون استفاده کنید
receiver_email = ["mohammad.pfallah@gmail.com", "shookooljooni254@gmail.com"]
message = "Subject: Hi there\nThis message is sent from Python.\nبا تشکر\nمحمد پورمحمدی فلاح".encode('utf-8')
smtp_server = "smtp.gmail.com"
port = 465  # For SSL
# port = 587  # For starttls
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print('Email Sent!!!')
    
# server = smtplib.SMTP_SSL(smtp_server, port, context=context)
# server.login(sender_email, password)
# server.sendmail(sender_email, receiver_email, message)
# server.close()
# print('Email Sent!!!')

# f = open('test.txt', 'w')
# f.write('salam')
# f.close()
# with open('test.txt', 'w') as f:
#     f.write('salam')