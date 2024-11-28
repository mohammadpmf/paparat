n=int(input("Enter n: "))
# if n==0:
#     # raise AssertionError("n نباید ۰ باشد")
#     # raise ImportError("هر پیامی که دوست داریم")
#     raise ZeroDivisionError("n can not be 0")
if n<10 or n>100:
    raise ValueError("n باید در محدوده ۱۰ تا ۱۰۰ باشد.")
print(100/n)
