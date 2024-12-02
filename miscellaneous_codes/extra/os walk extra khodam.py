import os
print ('-------------------------------- Start --------------------------------')
for (root,dirs,files) in os.walk(r"C:\Users\Mohammad\Desktop\Zabt Python\python codes\main", topdown=True):
    print (root)  # type(root) -> str
    print (dirs)  # type(dirs) -> list
    print (files) # type(root) -> list
    print ('-------------------------------- Middle --------------------------------')
print ('-------------------------------- End --------------------------------')
