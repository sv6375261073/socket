from socket import *
from _thread import *
from tkinter import *
s=socket(AF_INET,SOCK_STREAM)
host="192.168.43.45"
port=7777
s.connect((host,port))
window=Tk()
window.title("Shivam")
window.geometry("400x400")
name=Label(window,text="Shivam",bg="red",font = "Verdana 30 bold",fg="blue")
name.place(relx=0,rely=0,relwidth=1,relheight=0.1)
entry=Entry(window,width="40")
entry.place(relx=0,rely=0.9,relwidth=0.8,relheight=0.1)
text1=""
def clicked():
    global text1
    message=entry.get()
    s.send(message.encode('utf-8'))
    entry.delete(0,END)
    text1=text1+"\n"+"                                    Shivam:"+message
    l=Label(window,text=text1,bg="green",font = "Verdana 10",fg="silver")
    l.place(relx=0,rely=0.1,relwidth=1,relheight=0.8)
btn=Button(window,text="send",bg="green",fg="white",width=8,height=1,command=clicked)
btn.place(relx=0.8,rely=0.9,relwidth=0.2,relheight=0.1)
def recvThread(s):
    while True:
        global text1
        text1=text1+"\n"+s.recv(1024).decode('utf-8')
        out=Label(window,text=text1,bg="green",font = "Verdana 8",fg="white")
        out.place(relx=0,rely=0.1,relwidth=1,relheight=0.8)
start_new_thread(recvThread,(s,))
window.mainloop()
