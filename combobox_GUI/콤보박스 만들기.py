#콤보박스 만들기
import tkinter.ttk as ttk
from tkinter import*

root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

dateVal = [str(i) + "일" for i in range(1,32)] #1~31까지의 i를 str(i)에 대입

combobox = ttk.Combobox(root, height=5, values = dateVal, state= "readonly")
combobox.current(0)
combobox.pack()
combobox.set("카드 결제일")

def btncmd() :
    print(combobox.get() + '를 선택하셨습니다.')

btn = Button(root, text = "날짜", command = btncmd)
btn.pack()

#root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
