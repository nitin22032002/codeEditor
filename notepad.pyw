import random
import shutil
import os
from tkinter import *
import tkinter.messagebox as msg
import tkinter.filedialog as file
from PIL import Image,ImageTk
import keyboard
import pyautogui as pg
import subprocess as sub

root=Tk()
a=""
path=""
frame1=Image.open("notepad.jpg")
frame1=ImageTk.PhotoImage(frame1)
root.wm_iconphoto(False,frame1)
root.title("Advance Notepad")
root.minsize(600,400)
root.geometry("500x500")
b="yes"
def ren():
    global path,root1,option,propath,trail
    try:
        a.close()
    except Exception as e:
        pass
    try:
        g.destroy()
        b1.destroy()
        h = path[::-1]
        slash = h.index("/")
        h1 = (h[slash:])[::-1]
        os.rename(path, h1+var.get())
        i=option.index(path[path.rfind("/")+1:])
        option.append(var.get())
        path=h1+var.get()
        propath.append(path)
        trail[i].destroy()
        trail.pop(i)
        propath.pop(i)
        option.pop(i)
        givelabel()
        addpro(var.get())
        root1.destroy()
    except Exception as e:
        root1.destroy()
def alertwindow(name,func):
    global b1,g,var,root1
    root1=Tk()
    var=StringVar(root1)
    g = Entry(root1, textvariable=var)
    g.place(x=10,y=10)
    b1=Button(root1,text=name,bg='orange',borderwidth=5,command=func)
    b1.place(x=10,y=50)
    root1.mainloop()
    return root1
def showfile():
    global path
    with open(str(path),"r") as f1:
        mainf=f1.readlines()
        f1.close()
    return "".join(mainf)
def newfile():
    global a,b,path
    try:
        mainf=open(path,"r")
        data=mainf.read().rstrip("\n")
        mainf.close()
        mainf=data
    except:
        mainf=""
    b='yes'
    if (mainf!="" and path=="") or mainf!=str(maintext.get(1.0,END)).rstrip("\n"):
        alertmessage = msg.askquestion("Alert", "Current File not save data is lost if new file create! you want to continue")
        if(alertmessage!="yes"):
            save()
    maintext.delete(1.0,END)
    path=""
    currentpath.config(text=f"Current Project:*new", border=2, borderwidth=1,bg='grey',fg='white')
    a=""
propath=[]
def save():
    global a,path,propath
    try:
        if path=="":
            files = [('All Files', '*.*'),
                     ('Python Files', '*.py'),
                     ('C Files','*.c'),
                     ('C++ files','*.cpp'),
                     ('Html Files','*.html'),
                     ('Java Script Files','*.js'),
                     ('Java files','*java'),
                     ('Text Document', '*.txt')]
            a = file.asksaveasfile(filetypes=files, defaultextension=files)
        if a!=None and a!="":
            path=str(a).split("'")
            path=str(path[1])
            givelabel()
        with open(str(path),"w") as f:
            f.write(maintext.get(1.0,END))
            f.close()
        if(b=="no"):
            a.close()
            a=""
    except Exception as e:
        a=""
def saveas():
    global path,a
    path=""
    save()
tryobject=2
def openfile():
    global path
    try:
        mainf=open(path,'r')
        data=mainf.read().rstrip("\n")
        mainf.close()
        mainf=data
    except:
        mainf=""
    if (str(maintext.get(1.0,END)).rstrip("\n")!="" and path=="") or mainf!=(str(maintext.get(1.0,END))).rstrip("\n") and tryobject!=1 :
        alertmessage = msg.askquestion("Alert",
                                       "Current File not save data is lost if new file open ! you want to continue")
        if (alertmessage != "yes"):
            save()
    try:
        global path1
        if tryobject!=1:
            path1=file.askopenfilename()
        else:
            path1=path
        with open(path1,"r") as f2:
            text=f2.readlines()
            f2.close()
        maintext.delete(1.0,END)
        for i in range(0,len(text)):
            maintext.insert(float(i+1),str(text[i]))
        path=path1
        givelabel()
    except Exception as e:
        try:
            with open(path1, "rb") as f2:
                text = f2.readlines()
                f2.close()
            maintext.delete(1.0, END)
            for i in range(0, len(text)):
                maintext.insert(float(i + 1), text[i])
            path = path1
            givelabel()
        except:
            pass
def givelabel():
    global path,propath
    currentpath.config(text=f"Current Project:{path}", border=2, borderwidth=2, bg='grey',
                        fg='white')
    if (path not in propath):
        option.append(path[path.rfind("/") + 1:])
        propath.append(path)
        addpro(path[path.rfind("/") + 1:])
def rename():
    global root1
    root1=alertwindow("rename",ren)
def refresh():
    global tryobject
    tryobject=1
    openfile()
    tryobject=2
def delete():
    global path,trail
    try:
        a.close()
    except:
        pass
    try:
        i = option.index(path[path.rfind("/") + 1:])
        os.remove(path)
        maintext.delete(1.0,END)
        path=""
        trail[i].destroy()
        trail.pop(i)
        currentpath.config(text=f"Current Project:*new", border=2, borderwidth=1, bg='grey', fg='white')
    except Exception as e:
        pass
def exitfun():
    global path
    check = list("\n")
    try:
        mainf = showfile()
    except:
        mainf = "\n"
    if (mainf!="\n" and path =="") or mainf != maintext.get(1.0, END):
        alertmessage = msg.askquestion("Alert",
                                       "Current File not save data is lost if new file create! you want to continue")
        if (alertmessage != "yes"):
            save()
    root.quit()
def about():
    pg.alert("It is IDE use to write code in any language it is develop by Er.NITIN GUPTA")
def help():
    pg.alert("contact with whatsapp boot which solve you problem no. 7890005676")
def alert():
    pg.alert('It is alert bell')
def copy():
    pg.hotkey('ctrl','a')
    pg.hotkey('ctrl','c')
    keyboard.release("ctrl")
def paste():
    pg.hotkey('ctrl', 'v')
    keyboard.release("ctrl")
def cut():
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'x')
    keyboard.release("ctrl")
def undo():
    pg.hotkey('ctrl', 'z')
    keyboard.release("ctrl")
def redo():
    pg.hotkey('ctrl', 'y')
    keyboard.release("ctrl")
import time
varcheck=0
def Run():
    global path,varcheck,intelegent
    var=1
    if(intelegent%2!=0):
        intelegent+=1
        var=0
    try:
        a.close()
    except Exception as e:
        pass
    try:
        filename = path[path.rfind("/")+1:path.rfind(".")]
        extention = path[path.rfind(".") + 1:]
        directory = path[:path.rfind("/")]
        varcheck += 1
        # if extention=="c" or extention=="cpp":
        if (path.endswith(".c") or path.endswith(".cpp")):
            os.chdir(f"{directory}")
            os.startfile("cmd.exe")
            time.sleep(1)
            # pg.press("enter")
            if path.endswith(".c"):
                    keyboard.write(f'gcc \"{filename}.{extention}\" -o \"{filename}\"')
            else:
                    keyboard.write(f'g++ \"{filename}.{extention}\" -o \"{filename}\"')
            time.sleep(1)
            pg.press("enter")
            keyboard.write(f'.\\\"{filename}.exe\"')
            pg.press('enter')
        elif extention == "py":
            os.startfile("cmd.exe")
            time.sleep(1)
            tem = f"C:\python3.7\python.exe \"{path}\""
            keyboard.write(tem)
            pg.press('enter')
        elif extention == "html":
            os.startfile(path)
        elif extention == "java":
            pg.alert("Currently java compilor is not install in advance notepad !")
        else:
            pg.alert("It is not compilable file no compilor there which compile this type of file !")
        varcheck += 1
        # closecmd()
    except Exception as e:
        print(e)
        pg.alert("This file can't run")
    finally:
        if(a==0):
            intelegent+=1
def runinconsole():
    global path,a,varcheck
    try:
        mainf = open(path, "r")
        data = mainf.read().rstrip("\n")
        mainf.close()
        mainf = data
    except:
        mainf = ""
    if (mainf != "" and path == "") or mainf != str(maintext.get(1.0, END)).rstrip("\n"):
        alertmessage = msg.askquestion("Alert",
                                       "Current file is not save please save you want to save")
        if (alertmessage != "yes"):
            save()
            Run()
    else:
        Run()
trail=[]
def creategit():
    global path, a,trail
    try:
        mainf = showfile().replace("\n", "")
    except:
        mainf = "\n"
    if (mainf != "\n" and path == "") or mainf != str(maintext.get(1.0, END)).replace("\n", ""):
        alertmessage = msg.askquestion("Alert",
                                       "Current File not save data is lost if new file create! you want to continue")
        if (alertmessage != "yes"):
            save()
    try:
        a.close()
    except Exception as e:
        pass
    try:
        h = path[::-1]
        slash = h.index("/")
        dot = h.index(".")
        extention = (h[0:dot])[::-1]
        pg.alert("Process of your file connect with git start it might take 30sec-1min")
        h1 = (h[slash + 1:])[::-1]
        filename = (h[dot + 1:slash])[::-1]
        p=os.getcwd()
        os.chdir(h1)
        maintain("git init")
        maintain(f'git add "{filename}.{extention}"')
        maintain(f'git commit -m "{filename}"')
        os.chdir(p)
        pg.alert("Your file successfully connected with git")
        i = option.index(path[path.rfind("/") + 1:])
        trail[i].config(fg="white")
    except:
        pg.alert("It is not valid file")
def openpro(event):
    global option,propath,path,subproject
    try:
        textwidget=event.widget.cget('text')
        path=propath[option.index(textwidget)]
        maintext.delete(1.0,END)
        with open(path,"r") as f:
            op=f.readlines()
        for i in range(len(op)):
            maintext.insert(float(i+1),op[i])
        givelabel()
    except:
        pass
option=[]
def addpro(item):
    global subproject,trail
    subproject = Button(frame1, text=f"{item}", font="comicsansms 10 bold", border=2, borderwidth=1, bg='grey',
                        fg='red')
    subproject.bind("<Button-1>", openpro)
    subproject.pack(pady=3)
    trail.append(subproject)
def addOnline(url,name):
    global path
    try:
        a.close()
    except Exception as e:
        print(e)
    try:
        h = path[::-1]
        slash = h.index("/")
        dot = h.index(".")
        extention = (h[0:dot])[::-1]
        h1 = (h[slash + 1:])[::-1]
        filename = (h[dot + 1:slash])[::-1]
        tem=url.rfind("/")
        tem=url[tem+1:url.rfind(".git")]
        pg.alert(f"process of your file upload on {name} is start it might take 2-3 minute")
        p=os.getcwd()
        os.chdir(h1)
        maintain(f'git remote add origin "{url}"')
        maintain(f'git clone "{url}"')
        try:
            os.chdir(h1+f"/{tem}")
        except:
            os.startfile("cmd.exe")
            time.sleep(2)
            keyboard.write(f'git remote add origin "{url}"')
            keyboard.press("enter")
            time.sleep(3)
            keyboard.write(f'git clone "{url}"')
            keyboard.press('enter')
            time.sleep(13)
            os.chdir(h1+f"/{tem}")
        shutil.copy(path, f"{h1}/{filename}copy.{extention}")
        shutil.move(f"{h1}/{filename}copy.{extention}", f"{h1}/{tem}/{filename}copy.{extention}")
        time.sleep(1)
        maintain(f'git add "{filename}copy.{extention}"')
        maintain("git status")
        maintain(f'git commit -m "{filename}"')
        maintain("git status")
        maintain("git push -u origin master")
        os.chdir(h1)
        os.startfile("cmd.exe")
        time.sleep(3)
        pg.write(f"Rmdir /s {tem}")
        pg.press("enter")
        pg.write("y")
        pg.press("enter")
        closecmd()
        os.chdir(p)
        pg.alert(f"Your file success fully uploaded on {name} !")
    except Exception as e:
        print(e)
        closecmd()
        pg.alert("It is not valid file")
def onlinerepositry(url,name):
    global path, a
    try:
        mainf = open(path, "r")
        data = mainf.read().rstrip("\n")
        mainf.close()
        mainf = data
    except:
        mainf = ""
    if (mainf != "" and path == "") or mainf != str(maintext.get(1.0, END)).rstrip("\n"):
        alertmessage = msg.askquestion("Alert",
                                       "You file is not save please save it ! you want to save")
        if (alertmessage != "yes"):
            save()
            addOnline(url,name)
    else:
        addOnline(url,name)
def closecmd():
    try:
        os.system("TASKKILL /F /IM cmd.exe")
    except:
        pass
def github():
    onlinerepositry("https://github.com/nitin22032002/notepad.git","Git Hub")
def bitbucket():
    onlinerepositry("https://Nitin2203@bitbucket.org/Nitin2203/notepad.git","Bit bucket")
def take():
    global root1
    if(var.get()!=""):
        onlinerepositry(str(var.get()),"Other repositry")
    else:
        root1.destroy()
def other():
    alertwindow("Other repositry",take)
def maintain(cmd):
    a = sub.Popen(cmd, shell=True, stdout=sub.PIPE, stderr=sub.PIPE)
    b = a.wait()
    ans,err=a.communicate()
autotem=0
tem=""
def opencmd():
    os.startfile("cmd.exe")
def auto():
    global autotem,tem
    autotem+=1
    save()
    keyboard.on_press(sa)
intelegent=0
mytag=""
def htmlintelegence(data):
    global mytag
    htmltag = "<area> <base> <br> <col> <embed> <hr> <img> <input> <link> <meta> <param> <source> <track> <wbr> <command> <keygen> <menuitem>"
    htmltag = htmltag.split()
    validhtml = "<h1>,<h2>,<h3>,<h4>,<h5>,<h6>,<div>,<span>,<p>,<sub>,sup>,<i>,<b>,<s>,<u>,<body>,<html>,<head>,<title>"
    validhtml = validhtml.split(",") + htmltag
    if (data == "<" and path.endswith(".html")):
        mytag += data
    elif (data == "space" and mytag.startswith("<") and not mytag.endswith(" ")) or (
            len(data) == 1 and (data.isdigit() or data.isalpha()) and mytag.startswith("<") and not mytag.endswith(
            " ")):
        if (data == "space"):
            data = " "
        mytag += data
    elif (data == "backspace" and mytag != ""):
        mytag = mytag[:-1]
    elif (data == ">" and path.endswith(".html") and mytag != ""):
        if (mytag[-1] == " "):
            mytag = (list(mytag[:-1] + ">"))
        else:
            mytag = (list(mytag + ">"))
        if("".join(mytag) not in validhtml):
            pg.alert("This html tag is not valid")
        else:
         if ("".join(mytag) not in htmltag):
            mytag.insert(1, "/")
            keyboard.write(mytag)
        mytag = ""
        if (autotem % 2 != 0):
            save()
    if (varcheck % 2 == 0 and intelegent % 2 != 0):
        if (keyboard.is_pressed(['shift', "!"]) and path.endswith(".html")):
            try:
                maintext.delete(1.0, END)
                teme = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<title>Title</title>\n</head>\n<body>\n<h1>Wlecome in Nitin Nodepad</h1>\n</body>\n</html>"
                teme = teme.split("\n")
                for i in range(len(teme)):
                    maintext.insert(float(i + 1), teme[i] + "\n")
                keyboard.release("shift")
                maintext.delete(maintext.search("!", 10.0, END), 12.0)
                if (autotem % 2 != 0):
                    save()
            except Exception as e:
                print(e)
def intelegentcy(key):
    global intelegent
    l = {"{": "}", "[": "]", "(": ")", '"': '"', "'": "'"}
    key = str(key)
    # it give key that press
    data = key[key.find("(") + 1:key.rfind(" ")]
    # it is use to save when ctrl+s press
    if (keyboard.is_pressed(["ctrl", "s"])):
        save()
    elif(keyboard.is_pressed(['ctrl','d'])):
        keyboard.press('enter')
        keyboard.release('enter')
        keyboard.write('@')
        time.sleep(0.01)
        i=maintext.search('@',1.0,END)
        keyboard.press('backspace')
        if(i==""):
            pass
        else:
            a=maintext.get(float(float(i)-1),float(i))
            maintext.insert(float(i),a[:-1])
    # it is use to intelegence
    else:
        if(intelegent%2!=0):
            htmlintelegence(data)
        if(data in l and intelegent%2!=0):
            keyboard.release("shift")
            keyboard.write(f"{l[data]}")
            keyboard.press('left')
            if (autotem % 2 != 0):
                time.sleep(.2)
                save()
            keyboard.release("shift")
def sa(key):
    global autotem,tem
    if(autotem%2!=0):
        save()
def openchr():
    try:
        os.startfile("chrome.exe")
    except:
        pg.alert("Google Chrome Not in Your system")
def opencal():
    try:
        os.startfile("msedge.exe")
    except:
        pg.alert("Microsoft edge Not in your system")
def openfmg():
    try:
        os.startfile("powershell.exe")
    except:
        pg.alert("Window Powershell not in your system")
def intelegenty():
    global intelegent
    intelegent+=1
def font1():
    global var,root1
    try:
        maintext.config(font=f"comicsansms {var.get()} bold")
    except:
        pass
    root1.destroy()
def color1():
    global var, root1
    try:
        maintext.config(foreground=f"{var.get()}",insertbackground=f"{var.get()}")
    except:
        pass
    root1.destroy()
def fieldcolor1():
    global var, root1
    try:
        maintext.config(background=f"{var.get()}")
    except:
        pass
    root1.destroy()
def sidecolor1():
    global var, root1
    try:
        frame1.config(background=f"{var.get()}")
    except:
        pass
    root1.destroy()
def font():
    alertwindow("Font Size",font1)
def color():
    alertwindow("Text Color",color1)
def fieldcolor():
    alertwindow("Field Color",fieldcolor1)
def sidecolor():
    alertwindow("Side Window Color", sidecolor1)
def move():
    global path
    try:
        if(path!=""):
            a=file.asksaveasfilename()
            os.rename(path,a)
            path=a
    except:
        pass
def duply():
    import random
    global path
    if(path!=""):
        try:
            with open(path,"r") as f:
                t="".join(f.readlines())
            try:
                x=file.asksaveasfilename()
            except:
                x=path[:path.rfind(".")]+str(random.randint(1,10000))+path[path.rfind("."):]
            with open(x,"w") as f:
                f.write(t)
        except:
            with open(path,"rb") as f:
                t=f.readlines()
            x=file.asksaveasfilename()
            if(x==""):
                x=path[:path.rfind(".")]+str(random.randint(1,10000))+path[path.rfind("."):]
            with open(x,"wb") as f:
                for item in t:
                    f.write(item)
keyboard.on_press(intelegentcy)
frame1=Frame(root,border=5,width=10,bg="black")
frame1.pack(side=LEFT,fill=Y)
currentpath=Label(frame1,font="comicsansms 10 bold")
currentpath.pack(side=TOP,pady=5)
scroly=Scrollbar(root)
scroly.pack(fill=Y,side=RIGHT)
maintext=Text(root,undo=True,width=10000,height=10000,background="white",insertbackground="black",font="comicsansms 17 bold",yscrollcommand=scroly.set)
scroly.config(command=maintext.yview)
maintext.pack()
mainmenu1=Menu(root,font="comicsansms 10 bold")
submenu1=Menu(mainmenu1,tearoff=0,font="comicsansms 10 bold")
submenu1.add_command(label="New File",command=newfile)
submenu1.add_command(label="Open",command=openfile)
submenu1.add_command(label="Save",command=save)
submenu1.add_command(label="Save as",command=saveas)
submenu1.add_command(label="Rename",command=rename)
submenu1.add_command(label="Move Project",command=move)
submenu1.add_command(label="Duplicate the project",command=duply)
submenu1.add_command(label="Delete",command=delete)
submenu1.add_command(label="Exit",command=exitfun)
submenu2=Menu(mainmenu1,tearoff=0,font="comicsansms 10 bold")
submenu2.add_command(label="Copy",command=copy)
submenu2.add_command(label="Paste",command=paste)
submenu2.add_command(label="Cut",command=cut)
submenu2.add_checkbutton(label="Auto save",command=auto)
submenu2.add_checkbutton(label="Auto complete",command=intelegenty)
submenu2.add_command(label="Refresh",command=refresh)
submenu2.add_command(label="Undo",command=undo)
submenu2.add_command(label="Redo",command=redo)
submenu3=Menu(mainmenu1,tearoff=0,font="comicsansms 10 bold")
submenu3.add_command(label="Run Program",command=runinconsole)
submenu4=Menu(mainmenu1,tearoff=0,font="comicsansms 10 bold")
submenu4.add_command(label="Git repositry",command=creategit)
submenu4.add_command(label="Git Hub",command=github)
submenu4.add_command(label="Bit bucket",command=bitbucket)
submenu4.add_command(label="On other repositry",command=other)
submenu5=Menu(mainmenu1,tearoff=0,font="comicsansms 10 bold")
submenu5.add_command(label="About",command=about)
submenu5.add_command(label="contact",command=help)
submenu5.add_command(label="Alert",command=alert)
submenu6=Menu(mainmenu1,tearoff=0,font='comicsansms 10 bold')
submenu7=Menu(mainmenu1,tearoff=0,font='comicsansms 10 bold')
submenu7.add_cascade(label="Font size",command=font)
submenu7.add_cascade(label="font color",command=color)
submenu7.add_cascade(label="textfield color",command=fieldcolor)
submenu7.add_cascade(label="SideBar color",command=sidecolor)
submenu6.add_cascade(label="Termnal",command=opencmd)
submenu6.add_cascade(label="Google",command=openchr)
submenu6.add_cascade(label="New Microsoft Edge",command=opencal)
submenu6.add_cascade(label="Window Power Shell",command=openfmg)
mainmenu1.add_cascade(label="File",menu=submenu1)
mainmenu1.add_cascade(label="Edit",menu=submenu2)
mainmenu1.add_cascade(label="Run",menu=submenu3)
mainmenu1.add_cascade(label="Repositry git/Online",menu=submenu4)
mainmenu1.add_cascade(label="Open Required Application",menu=submenu6)
mainmenu1.add_cascade(label="Settings",menu=submenu7)
mainmenu1.add_cascade(label="Help",menu=submenu5)
root.config(menu=mainmenu1)
root.mainloop()
