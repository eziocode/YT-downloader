#Mini project about Youtube Downloader
#libraries/

from tkinter import *
from pytube import YouTube
from tkinter import messagebox as mb
import webbrowser as wb

#customizing tkinter

root=Tk()
root.iconbitmap('yt.ico')
root.geometry('1366x768')
root.state('zoomed')
root.title('RADAK YOUTUBE DOWNLOADER')

#Background image

img=PhotoImage(file='yt.png')

#I used canvas for transparency

c = Canvas(root ,width=1366,height=768)
c.pack(fill='both',expand=True)

#for background image centered

c.create_image(0,0,image=img,anchor='nw')

#for text

c.create_text(700,100,text='YOUTUBE DOWNLOADER✨',fill='red',font=('Tahoma Bold',24),anchor=N)
c.create_text(700,190,text='Paste Link Here ⬇',fill='red',font=('Tahoma Bold',24),anchor=N)

#for entry box

link = StringVar()

link_enter = Entry(root, width = 50,textvariable = link,fg = 'blue',bg = 'light grey').place(relx=0.5, rely=0.4, anchor=CENTER)

#function for download and messagebox feature

def hddownload():
    try:
        url = YouTube(str(link.get()))
    
    except:
        mb.showerror('OOPS',"Please,Enter a valid input❌")
    
    else:
        video = url.streams.get_highest_resolution()
        video = video.download()
        mb.showinfo('Yes!',"Download Completed✔")


def sddownload():
    try:
        url = YouTube(str(link.get()))
    
    except:
        mb.showerror('OOPS',"Please,Enter a valid input❌")
    
    else:
        video = url.streams.first()
        video = video.download()
        mb.showinfo('Yes!',"Download Completed✔")

def readme1():
    return mb.showinfo('Info','Project By 🐱‍🏍 \n Aswin Kumar \n Karthikeyan \n Abiruban \n Durkesh \n Richard')
     
def web():
    return wb.open('https://github.com/eziocode/eziocode')

#for buttons

butn = PhotoImage(file='wd.png')
butn1 = PhotoImage(file='sd.png')
readme = PhotoImage(file='readme.png')
giti =  PhotoImage(file='git.png')

button1 = Button(root,image=butn,borderwidth=0,bg="#d6a59e",command=hddownload)
button2 = Button(root,image=butn1,borderwidth=0,bg="#d09b95",command=sddownload)

button = c.create_window(850,270,anchor='nw',window=button1)
button_ = c.create_window(900,305,anchor='nw',window=button2)

read_text = c.create_text(1250,590,text='Readme ✌',font=('arial bold',12),fill='grey')

info = c.create_window(1250,605, anchor='nw',window=Button(root,image=readme,borderwidth=0,bg='#adb0b5',command=readme1))

git = c.create_window(1250,650,anchor='nw',window=Button(root,image=giti,borderwidth=0,bg='#adb0b5',command=web))

#to start

root.mainloop()





'''''
 ▄████▄   ▒█████  ▓█████▄ ▓█████     ▄▄▄▄ ▓██   ██▓   ▓█████ ▒███████▒ ██▓ ▒█████  
▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀    ▓█████▄▒██  ██▒   ▓█   ▀ ▒ ▒ ▒ ▄▀░▓██▒▒██▒  ██▒
▒▓█    ▄ ▒██░  ██▒░██   █▌▒███      ▒██▒ ▄██▒██ ██░   ▒███   ░ ▒ ▄▀▒░ ▒██▒▒██░  ██▒
▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄    ▒██░█▀  ░ ▐██▓░   ▒▓█  ▄   ▄▀▒   ░░██░▒██   ██░
▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒   ░▓█  ▀█▓░ ██▒▓░   ░▒████▒▒███████▒░██░░ ████▓▒░
░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░   ░▒▓███▀▒ ██▒▒▒    ░░ ▒░ ░░▒▒ ▓░▒░▒░▓  ░ ▒░▒░▒░ 
  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░   ▒░▒   ░▓██ ░▒░     ░ ░  ░░░▒ ▒ ░ ▒ ▒ ░  ░ ▒ ▒░ 
░        ░ ░ ░ ▒   ░ ░  ░    ░       ░    ░▒ ▒ ░░        ░   ░ ░ ░ ░ ░ ▒ ░░ ░ ░ ▒  
░ ░          ░ ░     ░       ░  ░    ░     ░ ░           ░  ░  ░ ░     ░      ░ ░  
░                  ░                      ░░ ░               ░                     '''