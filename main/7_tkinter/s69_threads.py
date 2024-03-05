from time import sleep
from threading import Thread
def test(n):
    for i in range(n, -1, -1):
        print(f"Remaining time {i}")
        sleep(1)

th1 = Thread(target=test, args=(10,))
th2 = Thread(target=test, args=(15,))
th3 = Thread(target=test, args=(10,))
th1.start()
th2.start()
th3.start()