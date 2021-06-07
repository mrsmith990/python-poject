from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("SYSTEM KASIR WARUNG TIGA SAUDAR")

text_Input = StringVar()
operator=""

Tops = Frame(root, width = 1600 ,height =50,bg="aqua", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 800,height = 700,bg="aqua", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width = 300 ,height = 700,bg="aqua", relief=SUNKEN)
f2.pack(side=RIGHT)
#=============time======================
localtime=time.asctime(time.localtime(time.time()))
#=============info=====================
lblinfo = Label(Tops, font=('arial' ,50, 'bold') ,text="WARUNG TIGA SAUDARA",fg="Steel Blue", bd=10, anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=('arial' ,10, 'bold') ,text="menyediakan berbagai sea food :",fg="Steel Blue", bd=10, anchor='w')
lblinfo.grid(row=3,column=0)
lblinfo = Label(Tops, font=('arial' ,20, 'bold') ,text=localtime ,fg="Steel Blue", bd=10, anchor='w')
lblinfo.grid(row=2,column=0)
#===========================calculator=================
def btnClick(numbers) :
    global operator
    operator = operator + str(numbers)
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

def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF =float(Fries.get())
    CoD = float(Drinks.get())
    CoFilet = float(Filet.get())
    CoBurger =float(Burger.get())
    CoChicken =float(Chicken.get())
    CoChese_burger =float(Chese_burger.get())

    CostofFries = CoF * 20000
    CostofDrinks = CoD * 10000
    CostofFilet =CoFilet * 15000
    CostofBurger =CoBurger * 25000
    CostofChicken =CoChicken * 20000
    CostosChese_burger =CoChese_burger * 20000
    
    CostofMeal = "Rp", str('%2f' % (CostofFries + CostofDrinks +  CostofFilet + CostofBurger + CostofChicken + CostosChese_burger))
    PayTax = ((CostofFries + CostofDrinks +  CostofFilet + CostofBurger + CostofChicken + CostosChese_burger) * 550)
    TotalCost = (CostofFries + CostofDrinks +  CostofFilet + CostofBurger + CostofChicken + CostosChese_burger)
    
    Ser_Charge = ((CostofFries + CostofDrinks +  CostofFilet + CostofBurger + CostofChicken + CostosChese_burger)/99)
    
    Service = "Rp", str('%2f' % Ser_Charge)
    OverALLCost = "Rp", str('%2f' % ( PayTax + TotalCost + Ser_Charge))
    PaidTax = "Rp", str('%2f' % PayTax)
    
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    Subtotal.set(CostofMeal)
    Total.set(OverALLCost)

def qExit() :
    root.destroy()

def Reset() :
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken.set("")
    Chese_burger.set("")

txtDisplay = Entry(f2,font=('arial', 20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                    bg="powder blue", justify='right' )
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16, pady=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=2,column=0)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="7", bg="aqua", command=lambda:btnClick(7)) .grid(row=1, column=0)
btn8=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="8", bg="powder blue", command=lambda:btnClick(8)) .grid(row=1, column=1)
btn9=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="9", bg="aqua", command=lambda:btnClick(9)) .grid(row=1, column=2)
Addition=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="+", bg="powder blue", command=lambda:btnClick("+")) .grid(row=1, column=3)
#=====================================================================
btn4=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="4", bg="powder blue", command=lambda:btnClick(4)) .grid(row=2, column=0)
btn5=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="5", bg="aqua", command=lambda:btnClick(5)) .grid(row=2, column=1)
btn6=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="6", bg="powder blue", command=lambda:btnClick(6)) .grid(row=2, column=2)
Substraction=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="-", bg="aqua", command=lambda:btnClick("-")) .grid(row=2, column=3)
#=====================================================================
btn1=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="1", bg="aqua", command=lambda:btnClick(1)) .grid(row=3, column=0)
btn2=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="2", bg="powder blue", command=lambda:btnClick(2)) .grid(row=3, column=1)
btn3=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="3", bg="aqua", command=lambda:btnClick(3)) .grid(row=3, column=2)
Multiply=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="*", bg="powder blue", command=lambda:btnClick("*")) .grid(row=3, column=3)
#=====================================================================
btn0=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="0", bg="powder blue", command=lambda:btnClick(0)) .grid(row=4, column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="C", bg="aqua", command= btnClearDisplay) .grid(row=4, column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="=", bg="powder blue", command= btnEqualsInput) .grid(row=4, column=2)
Division=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="/", bg="aqua", command=lambda:btnClick("/")) .grid(row=4, column=3)
#======================================================================
btnkoma=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text=",", bg="aqua", command=lambda:btnClick(",")) .grid(row=5, column=0)
btntpoint=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text=".", bg="powder blue", command=lambda:btnClick(".")) .grid(row=5, column=1)
btnpercent=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 20,'bold'), 
            text="%", bg="aqua", command=lambda:btnClick("%")) .grid(row=5, column=2)
btn100=Button(f2,padx=16,pady=16,bd=8, fg="black" ,font=('arial', 10,'bold'), 
            text="100", bg="powder blue", command=lambda:btnClick("100")) .grid(row=5, column=3)

#==========================================restaurant=====================================================
rand= StringVar()
Fries= StringVar()
Burger=StringVar()
Filet=StringVar()
Subtotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Chicken=StringVar()
Chese_burger=StringVar()

lblRefrence = Label(f1,font=('arial', 16, 'bold'), text="Refrensi", bd=16, anchor='w')
lblRefrence.grid(row=0, column=0)
txtRefrence=Entry(f1,font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=8,
                    bg="powder blue", justify = 'right')
txtRefrence.grid(row=0, column=1)

lblFries = Label(f1,font=('arial', 16, 'bold'), text="Kari Rajungan", bd=16, anchor='w')
lblFries.grid(row=1, column=0)
txtFries=Entry(f1,font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=8,
                    bg="powder blue", justify = 'right')
txtFries.grid(row=1, column=1)

lblBurger = Label(f1,font=('arial', 16, 'bold'), text="Sate Ayam", bd=16, anchor='w')
lblBurger.grid(row=2, column=0)
txtBurger=Entry(f1,font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=8,
                    bg="powder blue", justify = 'right')
txtBurger.grid(row=2, column=1)

lblFilet = Label(f1,font=('arial', 16, 'bold'), text="Rajungan Bumbu Merah", bd=16, anchor='w')
lblFilet.grid(row=3, column=0)
txtFilet=Entry(f1,font=('arial', 16, 'bold'), textvariable=Filet, bd=10, insertwidth=8,
                    bg="powder blue", justify = 'right')
txtFilet.grid(row=3, column=1)

lblChicken = Label(f1,font=('arial', 16, 'bold'), text="Ayam Bakar", bd=16, anchor='w')
lblChicken.grid(row=4, column=0)
txtChicken=Entry(f1,font=('arial', 16, 'bold'), textvariable=Chicken, bd=10, insertwidth=8,
                    bg="powder blue", justify = 'right')
txtChicken.grid(row=4, column=1)

lblAyam = Label(f1,font=('arial', 16, 'bold'), text="Ayam Goreng Kremes", bd=16, anchor='w')
lblAyam.grid(row=5, column=0)
txtAyam=Entry(f1,font=('arial', 16, 'bold'), textvariable=Chese_burger, bd=10, insertwidth=8,
                    bg="powder blue", justify = 'right')
txtAyam.grid(row=5, column=1)
#=====================================restaurant2==================================
lblDrinks = Label(f1,font=('arial', 16, 'bold'), text="Minuman", bd=16, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1,font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=8,
                    bg="White", justify = 'right')
txtDrinks.grid(row=0, column=3)

lblCost = Label(f1,font=('arial', 16, 'bold'), text="biaya makan", bd=16, anchor='w')
lblCost.grid(row=1, column=2)
txtCost=Entry(f1,font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=8,
                    bg="White", justify = 'right')
txtCost.grid(row=1, column=3)

lblService = Label(f1,font=('arial', 16, 'bold'), text="Service_Charge", bd=16, anchor='w')
lblService.grid(row=2, column=2)
txtService = Entry(f1,font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=8,
                    bg="White", justify = 'right')
txtService.grid(row=2, column=3)

lblTax = Label(f1,font=('arial', 16, 'bold'), text="pajak", bd=16, anchor='w')
lblTax.grid(row=3, column=2)
txtTax=Entry(f1,font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=8,
                    bg="White", justify = 'right')
txtTax.grid(row=3, column=3)

lblSubtotal = Label(f1,font=('arial', 16, 'bold'), text="Sub total", bd=16, anchor='w')
lblSubtotal.grid(row=4, column=2)
txtSubtotal=Entry(f1,font=('arial', 16, 'bold'), textvariable=Subtotal, bd=10, insertwidth=8,
                    bg="White", justify = 'right')
txtSubtotal.grid(row=4, column=3)

lblTotalCost = Label(f1,font=('arial', 16, 'bold'), text="Total", bd=16, anchor='w')
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1,font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=8,
                    bg="White", justify = 'right')
txtTotalCost.grid(row=5, column=3)
#============================================================================================
btnTotal=Button(f1,padx=16,pady=8, bd=16, fg="Black",font=('aial', 16,'bold'), width=10,
                text="Total", bg="powder blue", command= Ref).grid(row=7, column=1)
btnReset=Button(f1,padx=16,pady=8, bd=16, fg="Black",font=('aial', 16,'bold'), width=10,
                text="Reset", bg="powder blue", command= Reset).grid(row=7, column=2)
btnExit=Button(f1,padx=16,pady=8, bd=16, fg="Black",font=('aial', 16,'bold'), width=10,
                text="Exit", bg="powder blue", command= qExit).grid(row=7, column=3)

root.mainloop()
