from tkinter import *
from tkinter import messagebox
import random
import string

# ฟังก์ชั่นสำหรับสุ่มตัวเลข 0-9 และ A-Z รวมกัน
def generate_random():
    all_characters = string.digits + string.ascii_uppercase
    # สุ่มตัวอักษร 4 ตัว (ทั้งตัวเลขและตัวอักษร)
    random_characters = [random.choice(all_characters) for _ in range(4)]
    return random_characters

# ฟังก์ชั่นที่เรียกเมื่อกดปุ่ม
def cmd_click():
    # รับค่าจากการสุ่ม
    characters = generate_random()
    # แสดงผลลัพธ์ใน Entry widgets
    for i in range(4):
        st_characters[i].set(characters[i])
    # ข้อความใน messagebox
    messagebox.showinfo(
        title="ข้อมูลสุ่ม",
        message=f"ตัวอักษรที่สุ่มได้: {' '.join(characters)}"
    )

window = Tk()
window.geometry("800x200")
window.title("Random Character Generator")
window.configure(background='#111111')

# frame
frame = Frame(window, bd='5', relief=GROOVE, padx=10, pady=10, height=200, width=800, bg="pink")

# Label
lbCharacters = Label(frame, text="ตัวอักษรที่สุ่ม", width="20", fg="blue", anchor='w')
lbCharacters.grid(column=0, row=0, sticky='w', padx=5, pady=5)

# Variables
st_characters = [StringVar() for _ in range(4)]

# Entry fields
for i in range(4):
    Entry(frame, bd=3, width=5, textvariable=st_characters[i], state='readonly').grid(column=i+1, row=0, padx=3, pady=5, sticky='w')

# Button
buttonW = Button(frame, text="สุ่ม", width=10, command=cmd_click)
buttonW.grid(column=0, row=1, columnspan=5, padx=3, pady=10, sticky='w')

# Display the frame
frame.pack(padx=10, pady=10)

window.mainloop()
