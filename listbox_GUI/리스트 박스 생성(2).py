#리스트 박스 생성(2)
from tkinter import*
root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

listbox = Listbox(root, selectmode = "extended", height =5) 
listbox.insert(0, "파이썬")
listbox.insert(1, "C#")
listbox.insert(2, "MySQL")
listbox.insert(END, "자바")
listbox.insert(END, "HTML5")
listbox.pack()

# def btncmd() : 
#     listbox.delete(END) #끝에서 부터 하나씩 삭제


# def btncmd() : 
#     print(listbox.get(0,2)) # 값가져오기


def btncmd() : 
    print("선택한 항목 : ", listbox.curselection()) #선택한 항목 출력
    print("항목개수 : ", listbox.size()) #항목 개수 출력
    

btn = Button(root, text = "선택 항목", command = btncmd)
btn.pack()

#root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
