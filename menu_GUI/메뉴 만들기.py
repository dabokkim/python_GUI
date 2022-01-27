#메뉴 만들기
from tkinter import*

root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

def btncmd():
    print('New File')

mymenu = Menu(root)

menu_file = Menu(mymenu, tearoff=0) #tearoff=0 : 하위메뉴의 분리기능을 사용할것인가(디폴트 : false) --사용하지않음
menu_file.add_command(label = "New File", command=btncmd) #서브메뉴, #이벤트처리기로 등록
menu_file.add_command(label = "New Window")  #서브메뉴
menu_file.add_separator() #메뉴 사이의 구분자 설정
menu_file.add_command(label = "Open File")
menu_file.add_separator()
menu_file.add_command(label = "Save All")
menu_file.add_separator()
menu_file.add_command(label = "Exit", command=root.quit)#루트 종료

mymenu.add_cascade(label = "File", menu = menu_file) #메인메뉴

mymenu.add_cascade(label = "Edit")

menu_view = Menu(mymenu, tearoff=0)
menu_view.add_checkbutton(label = "Show minimap")
menu_view.add_checkbutton(label = "Show maxmap")
mymenu.add_cascade(label = "View", menu = menu_view)

root.config(menu = mymenu)

#root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
