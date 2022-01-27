#라디오박스 생성
from tkinter import*
root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

Label(root, text="햄버거를 선택하세요").pack()
burger_var = StringVar()
btn_burger1 = Radiobutton(root, text = "불고기버거", value = "불고기버거", variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text = "치즈버거", value = "치즈버거", variable=burger_var)
btn_burger3 = Radiobutton(root, text = "더블버거", value = "더블버거", variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

def btncmd() :
    print(burger_var.get() + '를 선택하셨습니다.')

btn = Button(root, text = "확인", command = btncmd)
btn.pack()


#root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
