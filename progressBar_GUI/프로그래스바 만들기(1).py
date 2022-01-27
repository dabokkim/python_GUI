#프로그래스바 만들기
import tkinter.ttk as ttk
from tkinter import*

root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

progressbar1 = ttk.Progressbar(root, maximum = 100, mode = "indeterminate")
progressbar1.pack()
progressbar2 = ttk.Progressbar(root, maximum = 100, mode = "determinate")
progressbar2.pack()

def btnStart() :
    progressbar1.start(10)
    progressbar2.start(10)
    

btn1 = Button(root, text = "시작", command = btnStart)
btn1.pack()

def btnStop() :
    progressbar1.stop()
    progressbar2.stop()
    

btn2 = Button(root, text = "정지", command = btnStop)
btn2.pack()

#root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
