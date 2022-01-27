#메시지 박스 만들기
import tkinter.ttk as ttk
from tkinter import*
import tkinter.messagebox as msgbox

root = Tk() #root객체생성 , Tk앞에 new가 생략됨
root.title("Python GUI")#창 제목 변경
root.geometry("600x400+200+100") #창크기, 위치 조정

def info() :
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn() :
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error() :
    msgbox.showerror("에러", "결제오류가 발생하였습니다.")

def okcancel() :
    res=msgbox.askokcancel("예/아니오", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")
    if res==1:
        print("예")
    elif res==0:
        print("아니오")
Button(root,command = info,text = "알림").pack()
Button(root,command = warn,text = "경고").pack()
Button(root,command = error,text = "에러").pack()
Button(root,command = okcancel,text = "확인/취소").pack()

#root.resizable(False, False)#창크기 조절 불가
root.mainloop() #무한루프로 계속 창을 띄어줌 (메모장 같은기능)
