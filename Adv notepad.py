import shutil
import os
from tkinter import *
import tkinter.messagebox as msg
import tkinter.filedialog as file
from PIL import Image,ImageTk
import pyautogui as pg
root=Tk()
a=""
path=""
frame1=Image.open("notepad.jpg")
frame1=ImageTk.PhotoImage(frame1)
root.wm_iconphoto(False,frame1)
root.title("Advance Notepad")
root.minsize(500,400)
root.geometry("500x500")
b="yes"
def ren():
    global path
    print(var.get())
    try:
        a.close()
    except Exception as e:
        print(e)
    os.rename(path, var.get())
    g.destroy()
    b1.destroy()
    h = path[::-1]
    print(h)
    slash = h.index("/")
    # dot = h.index(".")
    h1 = (h[slash:])[::-1]
    path=h1+var.get()
    print(path)
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
        mainf=showfile()
    except:
        mainf="\n"
    b='yes'
    if (mainf!="\n" and path=="") or mainf!=maintext.get(1.0,END):
        alertmessage = msg.askquestion("Alert", "Current File not save data is lost if new file create! you want to continue")
        if(alertmessage!="yes"):
            save()
    maintext.delete(1.0,END)
    path=""
    a=""
def save():
    global a,path
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
            print(a)
        if a!=None and a!="":
            path=str(a).split("'")
            path=str(path[1])
            print(path)
        with open(str(path),"w") as f:
            f.write(maintext.get(1.0,END))
            f.close()
        if(b=="no"):
            a.close()
            a=""
    except Exception as e:
        a=""
        print(e,path)
def saveas():
    global path,a
    path=""
    save()
tryobject=2
def openfile():
    global path
    try:
        mainf=showfile().replace("\n","")
    except:
        mainf=""
    if (str(maintext.get(1.0,END)).replace("\n","")!="" and path=="") or mainf!=(str(maintext.get(1.0,END))).replace("\n","") and tryobject!=1 :
        newfile()
    try:
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
    except Exception as e:
        print(e)
def rename():
    global root1
    root1=alertwindow("rename",ren)
def refresh():
    global tryobject
    tryobject=1
    openfile()
def delete():
    global path
    try:
        a.close()
    except:
        pass
    try:
        os.remove(path)
        maintext.delete(1.0,END)
        path=""
    except Exception as e:
        print(e)
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
    pg.mouseDown()
    pg.mouseUp()
def paste():
    pg.hotkey('ctrl', 'v')
    pg.mouseDown()
    pg.mouseUp()
def cut():
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'x')
def undo():
    pg.hotkey('ctrl', 'z')
    pg.keyUp('ctrl')
def redo():
    pg.hotkey('ctrl', 'y')
    pg.keyUp('ctrl')
import time
def runinconsole():
    global path,a
    try:
        mainf = showfile().replace("\n","")
    except:
        mainf = "\n"
    print(mainf,maintext.get(1.0,END),sep="\n")
    if (mainf != "\n" and path == "") or mainf != str(maintext.get(1.0, END)).replace("\n",""):
        alertmessage = msg.askquestion("Alert",
                                       "Current File not save data is lost if new file create! you want to continue")
        if (alertmessage != "yes"):
            save()
    try:
        a.close()
    except Exception as e:
        print(e)
    try:
        h=path[::-1]
        print(h)
        slash=h.index("/")
        dot=h.index(".")
        extention=(h[0:dot])[::-1]
        h1 = (h[slash + 1:])[::-1]
        filename = (h[dot + 1:slash])[::-1]
        print(filename, h1, path)
        if extention=="c" or extention=="cpp":
            os.startfile("C:\Windows\system32\cmd.exe")
            time.sleep(1)
            pg.write('cd "' + h1+'"')
            pg.press("enter")
            if extention=="c":
                pg.write('gcc "'+filename+'".'+extention+' -o "'+filename+'"')
            else:
                pg.write('g++ "'+filename+'".'+extention+' -o "'+filename+'"')
            pg.press('enter')
            time.sleep(1)
            pg.write('.\\"'+filename+'.exe"')
            pg.press('enter')
        elif extention=="py":
            os.startfile("C:\Windows\system32\cmd.exe")
            time.sleep(1)
            tem='C:\python3.7\python.exe "'+path+'"'
            pg.write(tem)
            pg.press('enter')
        elif extention=="html":
            os.startfile(path)
        elif extention=="java":
            pg.alert("Currently java compilor is not install in advance notepad !")
        else:
            pg.alert("It is not compilable file no compilor there which compile this type of file !")
    except Exception as e:
        pg.alert("This file can't run")
        print(e)
def creategit():
    global path, a
    try:
        mainf = showfile().replace("\n", "")
    except:
        mainf = "\n"
    print(mainf, maintext.get(1.0, END), sep="\n")
    if (mainf != "\n" and path == "") or mainf != str(maintext.get(1.0, END)).replace("\n", ""):
        alertmessage = msg.askquestion("Alert",
                                       "Current File not save data is lost if new file create! you want to continue")
        if (alertmessage != "yes"):
            save()
    try:
        a.close()
    except Exception as e:
        print(e)
    try:
        h = path[::-1]
        print(h)
        slash = h.index("/")
        dot = h.index(".")
        extention = (h[0:dot])[::-1]
        h1 = (h[slash + 1:])[::-1]
        filename = (h[dot + 1:slash])[::-1]
        print(filename, h1, path)
        os.startfile("C:\Windows\system32\cmd.exe")
        time.sleep(3)
        pg.write('cd "' + h1+'"')
        pg.press("enter")
        pg.write("git init")
        pg.press("enter")
        pg.write("git status")
        pg.press("enter")
        pg.write(f'git add "{filename}.{extention}"')
        pg.press("enter")
        pg.write("git status")
        pg.press("enter")
        pg.write(f'git commit -m "{filename}"')
        pg.press("enter")
        pg.write("git status")
        pg.press("enter")
        closecmd()
    except:
        closecmd()
        pg.alert("It is not valid file")
def onlinerepositry(url,name):
    global path, a
    try:
        mainf = showfile().replace("\n", "")
    except:
        mainf = "\n"
    print(mainf, maintext.get(1.0, END), sep="\n")
    if (mainf != "\n" and path == "") or mainf != str(maintext.get(1.0, END)).replace("\n", ""):
        alertmessage = msg.askquestion("Alert",
                                       "Current File not save data is lost if new file create! you want to continue")
        if (alertmessage != "yes"):
            save()
    try:
        a.close()
    except Exception as e:
        print(e)
    try:
        h = path[::-1]
        print(h)
        slash = h.index("/")
        dot = h.index(".")
        extention = (h[0:dot])[::-1]
        h1 = (h[slash + 1:])[::-1]
        filename = (h[dot + 1:slash])[::-1]
        print(filename, h1, path)
        tem=url.rfind("/")
        tem=url[tem+1:url.rfind(".git")]
        print(tem)
        os.startfile("C:\Windows\system32\cmd.exe")
        time.sleep(1)
        pg.write('cd "' + h1+'"')
        pg.press("enter")
        pg.write(f'git remote add origin master "{url}"')
        pg.press("enter")
        pg.write(f'git clone "{url}"')
        pg.press("enter")
        time.sleep(13)
        pg.write(f"cd {tem}")
        pg.press("enter")
        shutil.copy(path, f"{h1}/{filename}copy.{extention}")
        shutil.move(f"{h1}/{filename}copy.{extention}", f"{h1}/{tem}/{filename}copy.{extention}")
        time.sleep(1)
        pg.write(f'git add "{filename}copy.{extention}"')
        pg.press("enter")
        pg.write("git status")
        pg.press("enter")
        pg.write(f'git commit -m "{filename}"')
        pg.press("enter")
        pg.write("git status")
        pg.press("enter")
        pg.write("git push -u origin master")
        pg.press("enter")
        time.sleep(15)
        pg.write("cd..")
        pg.press("enter")
        p=os.getcwd()
        os.chdir(h1)
        while(tem in os.listdir()):
            pg.write(f"Rmdir /s {tem}")
            pg.press("enter")
            pg.write("y")
            pg.press("enter")
        closecmd()
        os.chdir(p)
        maintext.delete(1.0,END)
        path=""
        pg.alert(f"Your file success fully uploaded on {name} now new file is here !")
    except Exception as e:
        print(e)
        closecmd()
        pg.alert("It is not valid file")
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
    onlinerepositry(var.get(),"Other repositry")
def other():
    alertwindow("Other repositry",take)
scroly=Scrollbar(root)
scroly.pack(side=RIGHT,fill=Y)
maintext=Text(root,undo=True,width=170,height=100,background="white",insertbackground="orange",yscrollcommand=scroly.set)
scroly.config(command=maintext.yview)
maintext.pack()
mainmenu1=Menu(root,font="comicsansms 10 bold")
submenu1=Menu(mainmenu1,tearoff=0,font="comicsansms 10 bold")
submenu1.add_command(label="New File",command=newfile)
submenu1.add_command(label="Open",command=openfile)
submenu1.add_command(label="Save",command=save)
submenu1.add_command(label="Save as",command=saveas)
submenu1.add_command(label="Rename",command=rename)
submenu1.add_command(label="Delete",command=delete)
submenu1.add_command(label="Exit",command=exitfun)
submenu2=Menu(mainmenu1,tearoff=0,font="comicsansms 10 bold")
submenu2.add_command(label="Copy",command=copy)
submenu2.add_command(label="Paste",command=paste)
submenu2.add_command(label="Cut",command=cut)
submenu2.add_command(label="Refresh",command=refresh)
submenu2.add_command(label="Undo",command=undo)
submenu2.add_command(label="Redo",command=redo)
submenu3=Menu(mainmenu1,tearoff=0,font="comicsansms 10 bold")
submenu3.add_command(label="Run in Terminal",command=runinconsole)
submenu4=Menu(mainmenu1,tearoff=0,font="comicsansms 10 bold")
submenu4.add_command(label="Git repositry",command=creategit)
submenu4.add_command(label="Git Hub",command=github)
submenu4.add_command(label="Bit bucket",command=bitbucket)
submenu4.add_command(label="On other repositry",command=other)
submenu5=Menu(mainmenu1,tearoff=0,font="comicsansms 10 bold")
submenu5.add_command(label="About",command=about)
submenu5.add_command(label="contact",command=help)
submenu5.add_command(label="Alert",command=alert)
mainmenu1.add_cascade(label="File",menu=submenu1)
mainmenu1.add_cascade(label="Edit",menu=submenu2)
mainmenu1.add_cascade(label="Run",menu=submenu3)
mainmenu1.add_cascade(label="Repositry git/github",menu=submenu4)
mainmenu1.add_cascade(label="Help",menu=submenu5)
root.config(menu=mainmenu1)
root.mainloop()

