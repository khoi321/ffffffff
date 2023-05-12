gui = Tk()
WA=gui.winfo_screenwidth()
MA=gui.winfo_screenheight()
gui.geometry('1028x700+%d+%d' %(WA/2-1000/2-30, MA/2-700/2-30))
gui.title('Auto Reg Tiktok By Nguyễn Nhật Sang - Website Bán Tool : NnsSoftware.Vn')
gui.iconbitmap('img\\tt.ico')
gui.resizable(False,False)
gui.rowconfigure(0, weight=1)
gui.columnconfigure(0,weight=1)
#
gruopBasic = LabelFrame(gui, text='Setting Basic')
gruopInfoTool = LabelFrame(gui, text='Thông tin')
gruopOutPut = LabelFrame(gui)
#
#====================================
view=Treeview(gruopOutPut, columns=('#', 'id','pass','mail', 'ip', 'trangthai'), show='headings')
view.place(x=1, y=1, width=990, height=509)
view.heading('#', text='#')
view.heading('id', text='User Tik Tok')
view.heading('pass', text='Mật khẩu')
view.heading('mail', text='Hotmail')
view.heading('ip', text='IP')
view.heading('trangthai', text='Trạng thái')

view.column('#', width=60, minwidth=60)
view.column('id', width=170, minwidth=170)
view.column('pass', width=170, minwidth=170)
view.column('mail', width=170, minwidth=170)
view.column('ip', width=150, minwidth=150)
view.column('trangthai', width=250, minwidth=250)
yscoll=Scrollbar(gruopOutPut, orient=VERTICAL, command=view.yview)
yscoll.pack(side=RIGHT, fill='y')
# xscoll=Scrollbar(gruopOutPut, orient=HORIZONTAL, command=view.xview)
# xscoll.pack(side=BOTTOM, fill='x')
view.configure(yscrollcommand=yscoll.set)
#====================================


_ip=json.loads(open('config/proxy.json', mode="r", encoding="utf-8-sig").read())
def settingInfo():
    configReg = json.loads(open("config/config.json", mode="r", encoding="utf-8-sig").read())
    def threadOut():
        popIf.destroy()
    popIf=Toplevel(gui)
    WA=gui.winfo_screenwidth()
    popIf.iconbitmap('img\\tt.ico')
    MA=gui.winfo_screenheight()
    popIf.geometry('400x300+%d+%d' %(WA/2-415/2-30, MA/2-335/2-30))
    #popIfww.geometry('455x275')
    popIf.title('Cài đặt Change Thông Tin')
    popIf.resizable(False, False)
    lb1 = LabelFrame(popIf)
    lb1.place(x = 15, y =15, height=220, width=365)
    lb1.config(background="#808080")
    def save():
        data={'folderAvt': f"{var.get()}", 'status': f"{varAvt.get()}"}
        pp=open('config/config.json', 'w+')
        with pp as outfile:
            json.dump(data, outfile, indent=2)
        popIf.destroy()
        messagebox.showinfo('Thông báo', 'Lưu setting thành công')
    def addFolder():
        filename = filedialog.askdirectory(
            title='Chọn File',
            initialdir='/Downloads')
        var.set(filename)
        


    #AVT
    var = StringVar()
    var.set(configReg['folderAvt'])
    varAvt=StringVar()
    avtArray=[
        '',
        'On',
        'Off',
    ]
    varAvt.set(configReg['status'])
    setAvt=OptionMenu(lb1, varAvt, *avtArray)
    setAvt.config(width=10)
    setAvt.place(x=100, y=14)
    avtText = Label(lb1, text="Đăng Avatar: ",fg="#00FF00", bg="#808080", font=("Segeo UI", 10, 'normal'))
    buttonFd = Button(lb1, width=10, text="File Ảnh", command=addFolder)
    fileText = Entry(lb1, width=40, textvariable=var)
    fileText.config(state=DISABLED)
    
    fileText.place(x=92, y = 49, height=25)
    avtText.place(x = 7, y = 15)
    buttonFd.place(x= 7, y = 50)

    buttonSaveMail = Button(popIf, text="Lưu", bg="#808080", command=save)
    buttonSaveMail.place(x = 90, y = 245, width=100, height=35)
    buttonSaveMail = Button(popIf, text="Thoát", bg="#808080", command=threadOut)
    buttonSaveMail.place(x = 210, y = 245, width=100, height=35)

#
gruopBasic.place(x = 5, y = 10, width=760, height=100)
gruopInfoTool.place(x = 770, y = 10,width=250,height=100)
gruopOutPut.place(x = 5, y = 120,width=1015,height=520)
#

def settingProxy():
    _ip=json.loads(open('config/proxy.json', mode="r", encoding="utf-8-sig").read())
    ww=Toplevel(gui)
    WA=gui.winfo_screenwidth()
    ww.iconbitmap('img\\tt.ico')
    MA=gui.winfo_screenheight()
    ww.geometry('455x275+%d+%d' %(WA/2-450/2-1, MA/2-400/2-1))
    # ww.geometry('455x275')
    ww.title('Cài đặt Fake IP')
    ww.resizable(False, False)
    lbl_proxy=LabelFrame(ww, text='Fake IP', font=('Segeo UI', 10))
    lbl_proxy.config(bg="#C0C0C0")

    lbl_proxy.place(x=5,y=5, width=445, height=200)
    def change_proxy(envent):
        hh=loai_proxy.get()
        if hh == 'HMA VPN':
            api_key.config(state=DISABLED)
        if hh == 'No Proxy':
            api_key.config(state=DISABLED)
        else:
            api_key.config(state=NORMAL)
    threadPro = StringVar()
    threadPro.set(_ip['thread'])
    def save_proxy():
        okNha = []
        for x in api_key.get(1.0, END).split('\n'):
            okNha.append(x)
        data={'loai': f"{loai_proxy.get()}",'thread': threadPro.get(), 'api-key': f"{','.join(okNha)}"}
        pp=open('config/proxy.json', 'w+')
        with pp as outfile:
            json.dump(data, outfile, indent=2)
        ww.destroy()
        messagebox.showinfo('Thông báo', 'Lưu setting thành công')
    loai_proxy=StringVar()
    proxy_str=[
        '',
        'No Proxy',
        'Shoplike Proxy',
        'TM Proxy',
        'Sproxy'
    ]
    luongProxy = Spinbox(lbl_proxy, from_=1, to=100,textvariable=threadPro, width=5)
    textProxy = Label(lbl_proxy, text="Luồng/Api: ")
    luongProxy
    loai_proxy.set(_ip['loai'])
    proxy=OptionMenu(lbl_proxy, loai_proxy, *proxy_str, command=change_proxy)
    proxy.config(width=15)
    proxy.place(x=5, y=5)
    textProxy.place(x = 220, y = 5)
    luongProxy.place(x=300, y=5)

    lbl_api=LabelFrame(lbl_proxy, text='Api key', font=('Segeo UI', 10))
    lbl_api.place(x=3, y=40, width=436, height=120)
    api_key=Text(lbl_api)
    api_key.place(x=3,y=3,  width=440, height=90)
    if loai_proxy.get() == "No Proxy":
        api_key.config(state=DISABLED)
    else:
        for x in _ip['api-key'].split(","):
            api_key.insert(END, f"{x}\n")
    sv_proxy=Button(ww, text="Lưu", bg="#BF00BF", command=save_proxy)
    sv_proxy.place(x=455/2-70, y=215, width=120, height=50)

def changeLoaiPass(event):
    if loaiPass.get() == 'Ngẫu nhiên':
        _password.config(state=DISABLED)
    else:
        _password.config(state=NORMAL)
#GRUOP BASIC
textThread = Label(gruopBasic, text='Thread:', font=('Segeo UI', 11, 'normal'))
luongReg = Spinbox(gruopBasic, from_=1, to=100, width=5)
timeCode = Spinbox(gruopBasic, from_=1, to=300, width=5)
textTimeCode = Label(gruopBasic, text="Delay đợi code:", font=('Segeo UI', 10, 'normal'))
textDelayReg = Label(gruopBasic, text="Delay reg:", font=('Segeo UI', 10, 'normal'))
delayReg = Spinbox(gruopBasic, from_=0, to=300, width=5)
textPass = Label(gruopBasic, text="Mật khẩu:", font=('Segeo UI', 10, 'normal'))

loaiPass=StringVar()
listLoai=[
    '',
    'Ngẫu nhiên',
    'Tự đặt'
]
loaiPass.set(listLoai[1])
loaiPassword=OptionMenu(gruopBasic, loaiPass, *listLoai, command=changeLoaiPass)
loaiPassword.config(width=11)
loaiPassword.place(x=70, y=45)
_password = Entry(gruopBasic, width=20, state=DISABLED)
_password.place(x = 185, y = 48)
#
#
textThread.place(x = 5, y = 1)
luongReg.place(x=65,y=5)
textTimeCode.place(x=120, y = 1)
timeCode.place(x = 220, y = 3)
textDelayReg.place(x=290, y=1)
delayReg.place(x=360, y = 3)
textPass.place(x=6, y = 45)
#
def test():
    textUserName['text'] = f"{userWeb}"
    textUserName.config(fg='green')
    _textHsd['text'] = f"{hsdWeb} Ngày"
    _textHsd.config(fg='green')

#GRUOP INFO TOOL
#
textUser = Label(gruopInfoTool, text="UN BY", font=('Segeo UI', 10, 'normal'))
textUserName = Label(gruopInfoTool, text="Nguyễn Nhật Sang", font=('Segeo UI', 11, 'normal'))
textHsd = Label(gruopInfoTool, text="ZALO:", font=('Segeo UI', 10, 'normal'))
_textHsd= Label(gruopInfoTool, text="0843452969", font=('Segeo UI', 10, 'normal'))
#
#
textUser.place(x=10 , y = 10)
textUserName.place(x=90 , y = 5)
textHsd.place(x=10 , y = 40)
_textHsd.place(x=63 , y = 40)
threading.Thread(target=test).start()

stop = threading.Event()
def stop_reg():
    try:
        for z in luồng_s:
            stop.set()
            z.join()
    except:
        buttonStart.config(state=NORMAL)
        buttonStop.config(state=NORMAL)
def stopReg():
    buttonStop.config(state=DISABLED)
    sti=threading.Thread(target=stop_reg)
    sti.start()

    
buttonStart = Button(gui, text='Bắt Đầu', command=run, font=('Segeo UI', 12, 'normal'))
buttonStop = Button(gui, text='Dừng',command=stopReg, font=('Segeo UI', 12, 'normal'))
buttonAddMail = Button(gui, text='Thêm Mail', command=addMail, font=('Segeo UI', 12, 'normal'))
buttonProxy = Button(gui, text='Fake IP', command=settingProxy, font=('Segeo UI', 12, 'normal'))
buttonSetingInfo = Button(gui, text='Change Info', command=settingInfo, font=('Segeo UI', 12, 'normal'))
buttonStart.place(x = 5, y = 647, width=100, height=40)
buttonStop.place(x = 120, y = 647, width=100, height=40)
buttonAddMail.place(x = 240, y = 647, width=100, height=40)
buttonProxy.place(x = 360, y = 647, width=100, height=40)
buttonSetingInfo.place(x = 480, y = 647, width=100, height=40)
gui.mainloop()