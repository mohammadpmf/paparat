import ghasedakpack
sms = ghasedakpack.Ghasedak("")
message = 'این اس ام اس از پایتون ارسال شده است. لغو۱۱'
my_number_1 = ''
my_number_2 = ''
line_number = ''
answer = sms.send({'message': message, 'receptor' : my_number_1, 'linenumber': line_number})
# answer = sms.bulk2({'message': message, 'receptor' : f'{my_number_1},{my_number_2}', 'linenumber': line_number})