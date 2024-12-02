import win32api
import random
import time

# for i in range(300):
#     x = random.randint(0, 1920)
#     y = random.randint(0, 1280)
#     time.sleep(0.01)
#     win32api.SetCursorPos((x, y))
    
# for i in range(5):
#     x = random.randint(0, 1920)
#     y = random.randint(0, 1280)
#     time.sleep(1)
#     win32api.SetCursorPos((x, y))

for i in range(30):
    x = random.randint(0, 1920)
    y = random.randint(0, 1280)
    time.sleep(0.1)
    win32api.SetCursorPos((x, y))
