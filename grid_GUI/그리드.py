#그리드
import tkinter.ttk as ttk
from tkinter import*
import tkinter.messagebox as msgbox

root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

Button(root, text="F16").grid(row=0,column=0) # grid() : 격자형식으로 버튼배치
Button(root, text="F17").grid(row=0,column=1)
Button(root, text="F18").grid(row=0,column=2)
Button(root, text="F19").grid(row=0,column=3)

Button(root, text = "clear", width = 10, height = 5).grid(row=1, column=0)
Button(root, text = "=", width = 10, height = 5).grid(row=1, column=1)
Button(root, text = "/", width = 10, height = 5).grid(row=1, column=2)
Button(root, text = "*", width = 10, height = 5).grid(row=1, column=3)

Button(root, text = "7", width = 10, height = 5).grid(row=2, column=0)
Button(root, text = "8", width = 10, height = 5).grid(row=2, column=1)
Button(root, text = "9", width = 10, height = 5).grid(row=2, column=2)
Button(root, text = "-", width = 10, height = 5).grid(row=2, column=3)

Button(root, text = "4", width = 10, height = 5).grid(row=3, column=0)
Button(root, text = "5", width = 10, height = 5).grid(row=3, column=1)
Button(root, text = "6", width = 10, height = 5).grid(row=3, column=2)
Button(root, text = "+", width = 10, height = 5).grid(row=3, column=3)

Button(root, text = "1", width = 10, height = 5).grid(row=4, column=0)
Button(root, text = "2", width = 10, height = 5).grid(row=4, column=1)
Button(root, text = "3", width = 10, height = 5).grid(row=4, column=2)
Button(root, text = "enter", width = 10, height = 5).grid(row=4, column=3)

#root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
