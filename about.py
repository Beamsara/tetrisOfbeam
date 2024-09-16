from  tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("600x400")
window.title("Welcome to First app")
window.configure(background='#111111')

#frame
frame = Frame(window,bd='5',relief=GROOVE,padx=10,pady=10,height=400,width=400,bg="pink")
#Label
lbName = Label(frame,text="ชื่อ" ,width="10",fg="blue", anchor='w')
lbName2 = Label(frame,text="นามสกุล" ,width="10",fg="blue", anchor='w')
lb3 = Label(frame,text="รหัส",width="10",fg="blue", anchor='w')
lbName.grid(column=0,row=0)
lbName2.grid(column=0,row=1)
lb3.grid(column=0,row=2)
st1=StringVar()
st2=StringVar()
st3=StringVar()
txt1 = Entry(frame, bd = 3,width=20,textvariable=st1).grid(column=1,row=0,padx=3,sticky='w')
txt2 = Entry(frame, bd = 3,width=20,textvariable=st2).grid(column=1,row=1,padx=3,sticky='w')
txt3 = Entry(frame, bd = 3,width=20,textvariable=st3).grid(column=1,row=2,padx=3,sticky='w')

def cmd_click():
    print("Hello",st1.get(),st2.get(),st3.get())
    messagebox.showinfo(title="ข้อมูล", message="ยินดีต้อนรับคุณ : "+st1.get()+" "+st2.get()+"\nหมายเลขของท่านคือ : "+st3.get())
    # messagebox.askquestion(title=None, message="กินข้าวยัง")

buttonW = Button(frame, text="Click", width=10,command=cmd_click)
buttonW.grid(column=1,row=3,padx=3,pady=1, sticky='w')

frame.pack(padx=10,pady=10)





window.mainloop() #วางไว้บรรทัดสุดท้ายเสมอ