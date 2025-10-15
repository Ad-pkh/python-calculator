from tkinter import *

first_no=second_no=None

def get_digit(digit):
    current=result_label["text"]
    new=current+ str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text="")

def get_operator(op):
    global first_no,operator
    first_no=int(result_label["text"])
    operator=op
    result_label.config(text="")

def get_result():
    global first_no,second_no,operator
    second_no=int(result_label["text"])

    if operator=="+":
        result_label.config(text=str(first_no + second_no))
    elif operator=="-":
        result_label.config(text=str(first_no - second_no))
    elif operator=="*":
        result_label.config(text=str(first_no * second_no))
    else:
        if second_no==0:
            result_label.config(text="error")
        else:
            result_label.config(text=str(first_no / second_no))

root=Tk()
root.title("calculator")
root.geometry("300x400")
root.resizable=(0.0)
root.configure(background="black")

result_label=Label(root,text="",bg='black',fg="white")
result_label.grid(row=0,columnspan=5,pady=(50,30),sticky='e')

result_label.config(font=("Vandana",30,"bold"))

btn7=Button(root,text="7",bg="yellow",fg="blue",width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=("Vandana",16,"bold"))

btn8=Button(root,text="8",bg="yellow",fg="blue",width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=("Vandana",16,"bold"))

btn9=Button(root,text="9",bg="yellow",fg="blue",width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=("Vandana",16,"bold"))

btn_divide=Button(root,text="/",bg="yellow",fg="red",width=5,height=2,command=lambda:get_operator("/"))
btn_divide.grid(row=1,column=3)
btn_divide.config(font=("Vandana",16,"bold"))

btn6=Button(root,text="6",bg="yellow",fg="blue",width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=2,column=0)
btn6.config(font=("Vandana",16,"bold"))

btn5=Button(root,text="5",bg="yellow",fg="blue",width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=("Vandana",16,"bold"))

btn4=Button(root,text="4",bg="yellow",fg="blue",width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=2,column=2)
btn4.config(font=("Vandana",16,"bold"))

btn_multiply=Button(root,text="*",bg="yellow",fg="red",width=5,height=2,command=lambda:get_operator("*"))
btn_multiply.grid(row=2,column=3)
btn_multiply.config(font=("Vandana",16,"bold"))

btn3=Button(root,text="3",bg="yellow",fg="blue",width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=3,column=0)
btn3.config(font=("Vandana",16,"bold"))

btn2=Button(root,text="2",bg="yellow",fg="blue",width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=("Vandana",16,"bold"))

btn1=Button(root,text="1",bg="yellow",fg="blue",width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=3,column=2)
btn1.config(font=("Vandana",16,"bold"))

btn_sum=Button(root,text="+",bg="yellow",fg="red",width=5,height=2,command=lambda:get_operator("+"))
btn_sum.grid(row=3,column=3)
btn_sum.config(font=("Vandana",16,"bold"))

btn_clear=Button(root,text="C",bg="yellow",fg="red",width=5,height=2,command=lambda:clear())
btn_clear.grid(row=4,column=0)
btn_clear.config(font=("Vandana",16,"bold"))

btn0=Button(root,text="0",bg="yellow",fg="blue",width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=("Vandana",16,"bold"))

btn_equal=Button(root,text="=",bg="yellow",fg="blue",width=5,height=2,command=get_result)
btn_equal.grid(row=4,column=2)
btn_equal.config(font=("Vandana",16,"bold"))

btn_sub=Button(root,text="-",bg="yellow",fg="red",width=5,height=2,command=lambda:get_operator("-"))
btn_sub.grid(row=4,column=3)
btn_sub.config(font=("Vandana",16,"bold"))

root.mainloop()