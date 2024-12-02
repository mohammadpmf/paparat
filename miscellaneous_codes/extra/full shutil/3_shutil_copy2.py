# فرق کپی ۲ با کپی اینه که یه سری متا دیتا هم مینویسه. مثل تایم استمپ
import shutil
# shutil.copy2('a.py', 'b.py')  # dst can be a folder; use shutil.copy2() to preserve timestamp
# shutil.copy2("C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/25/3.py", "test.py")
# shutil.copy2("C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/25/3.py", "C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/25/3_2.py")
# shutil.copy2("C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/25/3.py", "C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/25/3_2.txt")
# shutil.copy2("C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/25/3.py", "1560") # یه فایلی به اسم ۱۵۶۰ میسازه و داخل اون مینویسه.
# shutil.copy2("C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/25/3.py", "1") # داخل فولدر ۱، یه فایلی به اسم 2.py که اسم فایل مبدا بود میسازه و داخل اون مینویسه. اگه وجود داشته باشه هم که روش مینویسه.
# shutil.copy2("C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/25/3.py", "1/10") # داخل فولدر ۱، میره داخل فولدر ۱۰ و یه فایلی به اسم 2.py میسازه و کدها رو داخل اون مینویسه. اگه وجود داشته باشه هم که روش مینویسه.
# shutil.copy2("C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/25/3.py", "1560/") # چون همچین فولدری وجود نداره ارور میده
# shutil.copy2("C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/25/3.py", "1/50/") # چون همچین فولدری وجود نداره ارور میده
shutil.copy2("C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/25/3.py", "1/50") # چون همچین فولدری وجود نداره ارور میده

