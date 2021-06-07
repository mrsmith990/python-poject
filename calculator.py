from tkinter import*

def btnClick(number) :
    global operator
    operator=operator + str(number)
    text_Input.set(operator)

def btnClearDisplay () :
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput () :
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal = Tk()
cal.title("calculator")
operator=""
text_Input =StringVar()

txtDisplay = Entry(cal,font=('arial', 20,'bold'), textvariable=text_Input, bd=30,insertwidth=4,
                    bg="greenyellow", justify='left') .grid(columnspan=4)

btn7=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="7", bg="aqua", command=lambda:btnClick(7)) .grid(row=1, column=0)
btn8=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="8", bg="powder blue", command=lambda:btnClick(8)) .grid(row=1, column=1)
btn9=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="9", bg="aqua", command=lambda:btnClick(9)) .grid(row=1, column=2)
Addition=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="+", bg="powder blue", command=lambda:btnClick("+")) .grid(row=1, column=3)
#=====================================================================
btn4=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="4", bg="powder blue", command=lambda:btnClick(4)) .grid(row=2, column=0)
btn5=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="5", bg="aqua", command=lambda:btnClick(5)) .grid(row=2, column=1)
btn6=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="6", bg="powder blue", command=lambda:btnClick(6)) .grid(row=2, column=2)
Substraction=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="-", bg="aqua", command=lambda:btnClick("-")) .grid(row=2, column=3)
#=====================================================================
btn1=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="1", bg="aqua", command=lambda:btnClick(1)) .grid(row=3, column=0)
btn2=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="2", bg="powder blue", command=lambda:btnClick(2)) .grid(row=3, column=1)
btn3=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="3", bg="aqua", command=lambda:btnClick(3)) .grid(row=3, column=2)
Multiply=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="*", bg="powder blue", command=lambda:btnClick("*")) .grid(row=3, column=3)
#=====================================================================
btn0=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="0", bg="powder blue", command=lambda:btnClick(0)) .grid(row=4, column=0)
btnClear=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="C", bg="aqua", command= btnClearDisplay) .grid(row=4, column=1)
btnEquals=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="=", bg="powder blue", command= btnEqualsInput) .grid(row=4, column=2)
Division=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="/", bg="aqua", command=lambda:btnClick("/")) .grid(row=4, column=3)
#======================================================================
btnkoma=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text=",", bg="aqua", command=lambda:btnClick(",")) .grid(row=5, column=0)
btntpoint=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text=".", bg="powder blue", command=lambda:btnClick(".")) .grid(row=5, column=1)
btnpercent=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="%", bg="aqua", command=lambda:btnClick("%")) .grid(row=5, column=2)
btn100=Button(cal,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="100", bg="powder blue", command=lambda:btnClick("100")) .grid(row=5, column=3)


cal.mainloop()