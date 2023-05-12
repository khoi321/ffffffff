import hashlib
import json
import os
import subprocess
import sys
import threading
from tkinter import Button, Label, Tk, messagebox
from bs4 import BeautifulSoup as bs
import imaplib,requests,re,time,random
import pyperclip


def Outlook(mail,password,dv,delay):
    try:  
        msrvr = imaplib.IMAP4_SSL('outlook.office365.com', 993)
        msrvr.login(mail, password)
        homthu = ['junk','inbox']
        for x in range(int(delay)):
            print(f"delay {x}")
            for hom in homthu:
                stat,cnt = msrvr.select(hom)
                try:
                    stat,dta = msrvr.fetch(cnt[0], '(BODY[TEXT])')
                    soup = bs(dta[0][1], "html.parser").find_all('p')
                    tinnhan =''
                    for tn in soup:
                        tinnhan += tn.text
                    try:
                        code = re.findall('[0-9]+', tinnhan.split('TikTok:')[1])[0]
                    except:
                        code = None
                    data_out = {'TinNhan':tinnhan.replace('\n',' ').replace('=\r','').replace('  ','').replace('\r',''),'OTP':code}
                except:
                    data_out = {'TinNhan':None,'OTP':None}
                if dv in str(data_out):
                    try:
                        msrvr.store(cnt[0], '+FLAGS', '\\Deleted')
                    except:
                        pass
                    data_out = data_out
                    return data_out
                else:
                    data_out = {'TinNhan':None,'OTP':None}
            time.sleep(1)
            # try:
            #     msrvr.expunge()
            #     msrvr.close()
            #     msrvr.logout()
            # except:
            #     pass
    except Exception as e:
        if 'LOGIN failed' in str(e):
            data_out = {'TinNhan':e,'OTP':False}
        else:
            data_out = {'TinNhan':e,'OTP':None}
    return data_out

def runnow(l,delay):
    time.sleep(3)
    acc = str(l)
    mail,password = (acc.strip()).split('|')
    tn = Outlook(mail,password,'TikTok',delay)
    if tn['OTP'] == False:
        
        print(acc.strip(),'=> Mail Die')
        return False
    elif tn['OTP'] == None:
        return None
    else:
        return tn['OTP']


class Username:
    def __init__(self):
        self.namee = requests.get(f'https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/{random.choice(["female","male"])}?count=2').json()['data'][0]['name']

    def name(self):
        self.full_name=self.namee
        return self.full_name

    def rem(self, nameFull):
        _name = str(nameFull).split(' ')
        if len(_name) == 3:
            _user = f"{_name[1]} {_name[2]}"
        else:
            _user = f"{_name[0]} {_name[1]}"
        s1=u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
        s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
        s = ''
        for c in _user:
            if c in s1:
                s += s0[s1.index(c)]
            else:
                s += c
        print(s)
        return s


    def get(self, ten):
        name = ten
        name_1 = self.rem(name)
        s=name_1
        print(s)
        chu=[]
        for x in range(random.randint(2,5)):
            tech=random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'])
            chu.append(tech)
        for x in range(random.randint(1,2)):
            number = str(random.randint(10,100))
            chu.append(number)
        username=s+''.join(chu)
        namene = ''
        for x in username:
            if x == "Ð":
                namene += "D"
            elif x== 'đ':
                namene += "d"
            else:
                namene += x
        print("đ" in namene, "Đ" in namene)
        print(namene)
        if " " in namene:
            return namene.replace(" ", "")  
        else:
            return namene

def Connect(typepr, api_key):
    if typepr == 'TM Proxy':
            js={
                "api_key": api_key,
                "sign": "string",
                "id_location": 0
            }
            while(True):
                a=requests.post('https://tmproxy.com/api/proxy/get-new-proxy', json=js).json()
                if a['code']==0:
                    return {'status': "success", 'http': a['data']['https']}
                elif a['code']==5:
                    b=requests.post('https://tmproxy.com/api/proxy/get-current-proxy', json={'api_key': api_key}).json()
                    if b['data']['timeout'] >= 300:
                        return {'status': "success", 'http': b['data']['https']}
                    else:
                        giay=str(a['message']).split('after ')[1].split(' sec')[0]
                        for x in range(int(giay)+2, 0, -1):
                            time.sleep(1)
                else:
                    return {'status': "error", 'mess': a['message']}

    elif typepr == "Shoplike Proxy":
        requests.get(f"http://proxy.shoplike.vn/Api/getNewProxy?access_token={api_key}").json()
        getNewProxy = requests.get(f"http://proxy.shoplike.vn/Api/getCurrentProxy?access_token={api_key}").json()
        if getNewProxy['status'] == "success":
            return {'status': "success", 'http': getNewProxy['data']['proxy']}
        else:
            return {'status': "error", 'mess': getNewProxy['mess']}

    elif typepr == "Sproxy":
        proxy = api_key
        ip = api_key.split(":")[0]
        print(f"http://{ip}:22222/api/v1/status?proxy={proxy}")
        GetStatus = requests.get(f"http://{ip}:22222/api/v1/status?proxy={proxy}").json()
        print(GetStatus)
        if "data" in GetStatus:
            requests.get(f"http://{ip}:22222/api/v1/reset?proxy={proxy}").json()
        else:
            return {'status': "error", 'mess': "port Proxy Khoong Ton Tai"}
        time.sleep(12)
        proxyy={
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }
        for i in range(5):
            try:
                ip=requests.get('http://api.myip.com',proxies=proxyy, timeout=5).json()['ip']
                d = {'status': "success", 'http': proxy}
                break
            except:
                d = {'status': "error", 'mess': "Lỗi xác định"}
        return d



def get_id_win():
    checmk_cmd = subprocess.check_output('wmic csproduct get uuid,name').decode('utf-8')
    a = checmk_cmd.split("\n")[1].split("  ")
    _id = f"{a[0]}|{a[1]}"
    if ' ' in _id:
        _id = _id.replace(' ', '')
    _app = hashlib.md5(bytes(str(_id), 'utf-8-sig')).hexdigest()
    __app = 'AZSOFT-'+str(_app[0:15])
    print(__app)
    return __app

def get_pw():
    số_kí_tự_in_chuỗi = random.randint(7,14)
    kí_tự_số = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    kiTuDacBiet = ['@', '#','!','&']
    chuHoa = ['A','B','C','D','E','G','H','J','U','I','O','P','K','T','Q','W','Y','L','M','Z']
    kí_tự_chữ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    set_chuỗi = kí_tự_số + kí_tự_chữ + chuHoa + kiTuDacBiet
    random_số = random.choice(kí_tự_số)
    random_chữ = random.choice(kí_tự_chữ)
    ghép = random_số + random_chữ
    for x in range(số_kí_tự_in_chuỗi):
        ghép = ghép + random.choice(set_chuỗi)
        import array
        ghép_list = array.array('u', ghép)
        random.shuffle(ghép_list)
    password = ""
    for x in ghép_list:
            password = password + x
    return password+'Ab1@'

if os.path.exists('config')==False:
    os.mkdir('config')
pathProxy='config/proxy.json'
if os.path.exists(pathProxy) == False:
    open(pathProxy, "w+")
    data={"loai": "No Proxy", "api-key": ""}
    _p=open('config/proxy.json', 'w+')
    with _p as outf:
        json.dump(data, outf, indent=3)

if os.path.exists("config/config.json") == False:
    open(pathProxy, "w+")
    data={"folderAvt": ""}
    _p=open('config/config.json', 'w+')
    with _p as outf:
            json.dump(data, outf, indent=3)


    win=Tk()
    win.title('Kích hoạt key')
    WA=win.winfo_screenwidth()
    win.iconbitmap('config\\CVEMNGU.ico')
    MA=win.winfo_screenheight()
    win.geometry('320x100+%d+%d' %(WA/2-450/2-1, MA/2-400/2-1))
    win.resizable(False,False)
    Label(win, text=f"ID Device: {id_win}").pack(padx=50, pady=25)
    def cop():
        pyperclip.copy(id_win)
        messagebox.showinfo('Thông báo', 'Copy ID Device Success')
    a=Button(win, text="Confirm", command=chay).place(x=90, y=65)
    Button(win, text="Copy ID", command=cop).place(x=165, y=65)
    win.mainloop()
# while(True):
#     ko = Connect("Shoplike Proxy", "e781f53322f163ffebde31850d2d8a12")
#     if ko['status'] == "success":
#         print(ko['http'])
#         break
#     else:
#         print(ko['mess'])
#         time.sleep(1)