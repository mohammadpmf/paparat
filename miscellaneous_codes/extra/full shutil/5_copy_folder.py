import shutil
source_dir = "25"
destination_dir = "25_2"
destination_dir2 = r"C:\Users\Mohammad\Desktop\New folder\test"
# shutil.copytree(source_dir, destination_dir) # اگه فولدر مقصد وجود نداشته باشه میسازه. اگه باشه ارور میده. اگر سیستم عامل هم اجازه دسترسی نده ارور میده.
shutil.copytree(source_dir, destination_dir2)
