from tkinter import *

root = Tk()
root.title("혼공 GUI 연습")
root.geometry("400x200")

root.mainloop()

from tkinter import *
root = Tk()
root.geometry("300x100")

Label1 = Label(root, text="혼공 SQL은")
Label2 = Label(root, text="쉽습니다.", font=("궁서체",30), bg="blue", fg="yellow")

Label1.pack()
Label2.pack()

root.mainloop()

# 버튼 클릭 이벤트
from tkinter import *
from tkinter import messagebox

def clickButton():
    messagebox.showinfo("버튼 클릭", '버튼을 눌렀습니다.')

root.geometry("200x200")

Button1 = Button(root, text="여기를 클릭하세요.", fg="red", bg="yellow", command=clickButton)

Button1.pack(expand=1)
# expand=1은 화면 중간에 출력

root.mainloop()

# 버튼 정렬
from tkinter import *
root = Tk()

Button1 = Button(root, text="bTN1")
Button2 = Button(root, text="bTN2")
Button3 = Button(root, text="bTN3")

Button1.pack(side=LEFT)
Button2.pack(side=LEFT)
Button3.pack(side=LEFT)

root.mainloop()

# 위젯 사이에 버튼 
from tkinter import *
root = Tk()

Button1 = Button(root, text="bTN1")
Button2 = Button(root, text="bTN2")
Button3 = Button(root, text="bTN3")

Button1.pack(side=TOP, fill=X, padx=10, pady=10)
Button2.pack(side=TOP, fill=X, padx=10, pady=10)
Button3.pack(side=TOP, fill=X, padx=10, pady=10)

root.mainloop()

# 예시

from tkinter import *

root = Tk()
root.title("EDIT BOX")
root.geometry("200x200")

upFrame = Frame(root)
upFrame.pack()

downFrame = Frame(root)
downFrame.pack()

editBox = Entry(upFrame, width=10)
editBox.pack(padx=20, pady=20)

listBox=Listbox(downFrame, bg="yellow")
listBox.pack()

listBox.insert(END, "하나")
listBox.insert(END, "둘")
listBox.insert(END, "셋")

root.mainloop()
