#프로그래스바 만들기(time.sleep()함수 적용)
import tkinter.ttk as ttk
from tkinter import*
import time

root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

p_var = DoubleVar()
progressbar1 = ttk.Progressbar(root, maximum = 100, length=150, variable=p_var)
progressbar1.pack()

def btnStart() :
    for i in range(1,101) :
        time.sleep(0.01) #0.01초 만큼 딜레이를 줌
        p_var.set(i)
        progressbar1.update()
#         print(p_var.get())
    
btn1 = Button(root, text = "시작", command = btnStart)
btn1.pack()

#root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
