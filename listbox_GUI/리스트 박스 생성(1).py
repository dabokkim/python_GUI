#리스트 박스 생성(1)
from tkinter import*
root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

listbox = Listbox(root, selectmode = "extended", height =5) #single(하나만 선택가능) , extended(여러개 선택가능), height=0 이면 갯수제한없음
listbox.insert(0, "파이썬")
listbox.insert(1, "C#")
listbox.insert(2, "MySQL")
listbox.insert(END, "자바")
listbox.insert(END, "HTML5")
listbox.pack()

#root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
