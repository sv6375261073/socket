from socket import *
from _thread import *
from tkinter import *
s=socket(AF_INET,SOCK_STREAM)
host="192.168.43.45"
port=7777
s.bind((host,port))
s.listen(50)
window=Tk()
window.title("Meri Sruti baby")
window.geometry("400x400")
name=Label(window,text="Sruti",bg="red",font = "Verdana 30 bold",fg="blue")
name.place(relx=0,rely=0,relwidth=1,relheight=0.1)
entry=Entry(window,width="40")
entry.place(relx=0,rely=0.9,relwidth=0.8,relheight=0.1)
session=[]
text1=""
def clicked():
    global text1
    message="scuti: "+entry.get()
    for c in session:
        c.send(message.encode('utf-8'))
        text1=text1+"\n"+"                             Scuti:"+message
        out=Label(window,text=text1,bg="green",font = "Verdana 8",fg="silver")
        out.place(relx=0,rely=0.1,relwidth=1,relheight=0.8) 
    entry.delete(0,END)
btn=Button(window,text="send",bg="green",fg="white",width=8,height=1,command=clicked)
btn.place(relx=0.8,rely=0.9,relwidth=0.2,relheight=0.1)
def recvThread(c,ad):
    while True:
        global text1
        text1=text1+"\n"+"Shivam:"+c.recv(1024).decode('utf-8')
        out=Label(window,text=text1,bg="green",font = "Verdana 10",fg="white")
        out.place(relx=0,rely=0.1,relwidth=1,relheight=0.8)
def mainThread(s):
    while True:
        c,ad=s.accept()
        session.append(c)
        start_new_thread(recvThread(c,ad))
start_new_thread(mainThread,(s,))
window.mainloop()
