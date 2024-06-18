import ghasedakpack
import random

sms = ghasedakpack.Ghasedak("")
my_number_1 = ''
my_number_2 = ''
line_number = ''
good_line_number_for_sending_otp = '' # مال خودم رو که میذارم، شانسی از این شماره یا 20008580 میفرسته که شماره ۳۰۰۰ اوکی هست. ولی ۲۰۰۰ داغانه یه بار تقریبا ۲۰ دقیقه طول کشید تا بفرسته که خب دیگه یکبار رمز به درد بخوری نیست.
template_name_in_ghasedak_me_site = ''
n=random.randint(10000, 99999)
answer = sms.verification({'receptor': my_number_2, 'linenumber': good_line_number_for_sending_otp,'type': '1', 'template': template_name_in_ghasedak_me_site, 'param1': n})
if answer:
    v_code = int(input("Enter verification code: "))
    if v_code == n:
        print('Welcome')
    else:
        print('Verification code is invalid')
