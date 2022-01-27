#라디오박스 생성
from tkinter import*
root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

chkclick1 = IntVar()
chkclick2 = IntVar()
chkbox1 = Checkbutton(root, text="오늘 하루 그만보기", variable = chkclick1)
chkbox1.pack()
chkbox2 = Checkbutton(root, text="일주일동안 그만보기", variable = chkclick2)
chkbox2.pack()
chkbox1.select() #초기화시 체크박스 자동선택
chkbox2.deselect() #초기화시 체크 되어있다면 자동해제

def btncmd() : 
    print("체크 상태 : ", chkclick1.get())
    print("체크 상태 : ", chkclick2.get())
    
btn = Button(root, text = "확인", command = btncmd)
btn.pack()


#root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
