#버튼 동작시키기
from tkinter import*
root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

btn1 = Button(root,text ="버튼인가?")#버튼 만들기
btn1.pack()#버튼 만들기

btn2 = Button(root, padx=20, pady=20, text ="아무튼버튼")
btn2.pack()

btn3 = Button(root,width=10,height=5,text="튼튼", fg="white", bg="powderblue")
btn3.pack()

def btncmd() : #콜백 함수
    print('좋아요를 꾸-욱 눌러주세요')

photo = PhotoImage(file = "jamsuham.png") #버튼에 이미지 삽입
btn4 = Button(root,image=photo, command=btncmd)
btn4.pack()#버튼 만들기

root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
