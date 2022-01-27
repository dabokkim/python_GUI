#텍스트 박스 생성
from tkinter import*
root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

# txt = Text(root, width = 40, height = 20)
# txt.insert(END, "글자를 입력하세요")
# txt.pack()

ent1 = Entry(root, width = 30) #한줄 입력할 때 사용(Entry)
ent1.insert(END, "아이디를 입력하세요")
ent1.pack()
ent2 = Entry(root, width = 30)
ent2.insert(END, "비밀번호를 입력하세요")
ent2.pack()

def btncmd() : 
#     print(ent1.get()) # get() : 입력한 값 가져오기
#     print(ent2.get())
    ent1.delete(0,END)
    ent2.delete(0,END)

btn = Button(root, text = "삭제", command = btncmd)
btn.pack()

#root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
