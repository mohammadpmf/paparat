import os
import getpass
import psutil
print(os.getlogin())
print(getpass.getuser())
print(os.environ.get('USERNAME'))
print(os.environ.get('USER', os.environ.get('USERNAME')))
print(os.path.expanduser('~'))
print(psutil.Process().username())