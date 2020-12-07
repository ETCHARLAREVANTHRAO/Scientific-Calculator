# IMPORTING REQUIRED MODULES #
from tkinter import * # IMPORT EVERYTHING FROM TKINTER MODULE
import tkinter.messagebox # IMPORTING MESSAGE BOX
import math as m # IMPORTING MATH MODULE

# CREATING GUI APPLICATION WINDOW #
root = Tk()
font = ('Times', 24,'bold italic') # FONT NAME, SIZE AND SHAPE
root.title("Scientific Calculator") # TITLE OF WINDOW
root.geometry("466x600") # WIDTH AND HEIGHT
root.resizable(width=False, height=False) # STOP RESIZING

# CREATING FRAME FOR CALCULATOR #
calci = Frame(root)
calci.configure(background="gray35") # BACKGROUND OF FRAME
calci.grid() # PACK IN GRID(TABLE LIKE STRUCTURE)
display = Entry(calci, font=font, bg="gray56",bd=30, width=25, justify=RIGHT) # CREATE ENTRY WIDGET
display.grid(row=0, column=0, columnspan=4, pady=1, padx=3)

# ADDING FUNCTION TO THE BUTTON #
def click_fun(event):
    b= event.widget
    text = b["text"] # TEXT ON THE BUTTON WILL BE TAKEN
    data = display.get() # TEXT WILL BE STORED IN VARIABLE DATA
    ans =''
    if text =='^':
        display.insert(END,"**") # IN PLACE OF '^' '**'IS IMPLEMENTED
        return
    if text == '=': # GIVE THE RESULT OF THE EQUATION
        try:
            answ = eval(data) # EVALUTE WHATEVER TYPED ON THE SCREEN
            display.delete(0,END) # DELETE THE DATA PREVIOUS ONE
            display.insert(0,answ) # ANS IS INSERTED
        except Exception as e:
            display.delete(0,END)
            display.insert(0,e) # THE ERROR WILL BE DISPLAYED

        return
    display.insert(END,text)
    if text == 'sqrt':
        ans = str(m.sqrt(float(data)))
        display.delete(0, END)
        display.insert(0, ans)
    elif text =="rad":
        ans = str(m.radians(float(data)))
        display.delete(0, END)
        display.insert(0, ans)
    elif text == 'sin':
        ans = str(m.sin(m.radians(float(data))))
        display.delete(0, END)
        display.insert(0, ans)
    elif text == 'deg':
        ans = str(m.degrees(float(data)))
        display.delete(0, END)
        display.insert(0, ans)
    elif text == 'cos':
        ans = str(m.cos(m.radians(float(data))))
        display.delete(0, END)
        display.insert(0, ans)
    elif text == 'tan':
        ans = str(m.tan(m.radians(float(data))))
        display.delete(0, END)
        display.insert(0, ans)
    elif text == 'fact':
        ans = str(m.factorial(int(data)))
        display.delete(0, END)
        display.insert(0, ans)
    elif text == 'sinh':
        ans = str(m.sinh(int(data)))
        display.delete(0, END)
        display.insert(0, ans)
    elif text == 'cosh':
        ans = str(m.cosh(float(data)))
        display.delete(0, END)
        display.insert(0, ans)
    elif text == 'tanh':
        ans = str(m.tanh(float(data)))
        display.delete(0, END)
        display.insert(0, ans)
    elif text == 'pi':
        ans = str(float(m.pi) *float(data))
        display.delete(0, END)
        display.insert(0, ans)
    elif text == 'log':
        ans = str(float(m.log10(float(data))))
        display.delete(0, END)
        display.insert(0, ans)
    elif text== 'ln':
        ans = str(float(m.log(float(data))))
        display.delete(0, END)
        display.insert(0, ans)
    elif text=='log2':
        ans = str(float(m.log2(float(data))))
        display.delete(0, END)
        display.insert(0, ans)
    elif text == 'e':
        ans = str(float(m.e) * float(data))
        display.delete(0, END)
        display.insert(0, ans)

# BACKWARD KEY IT DELETES THE LAST LETTER #
def clear():
    data = display.get()
    legth= len(data)-1
    display.delete(legth,END)
# CLEAR ALL #
def allclear():
    display.delete(0,END)

# LOOP TO CREATE BUTTONS FROM 1-9 #
numbers = "789456123"
i = 0
button =[]
for j in range(2, 5):
    for k in range(3):
        button.append(Button(calci, width= 3, height=2, font=font,bg="gray17",fg="cyan", bd=4, text=numbers[i]))
        button[i].grid(row=j, column=k, pady=1)
        button[i].bind('<Button-1>',click_fun)
        i +=1

# OTHER BUTTONS WITH THEIR FUNCTIONS #
btnClear = Button(calci, text= "C",width=4, height=1, font=font, bd=4,
                  bg="orange",command=clear).grid(row=1, column=0, pady=1)
AllClear =Button(calci, text= "CE",width=6, height=1, font=font, bd=4,
                 bg="red",command=allclear).grid(row=1, column=1, pady=1)
pwr = Button(calci, text= "^",width= 4, height=1, font=font, bd=4,bg="slateblue")
pwr.bind("<Button-1>",click_fun) # Bind widget to add funtion when pressed
pwr.grid(row=1, column=2, pady=1)
plus = Button(calci, text= "+",width= 4, height=1, font=font, bd=4, bg="blue")
plus.bind('<Button>',click_fun)
plus.grid(row=1, column=3, pady=1)

minus =Button(calci, text= "-",width= 4, height=1, font=font, bg="blue",bd=4)
minus.bind('<Button-1>',click_fun)
minus.grid(row=2, column=3, pady=1)
multi = Button(calci, text= "*",width= 4, height=1, font=font, bd=4,bg="blue")
multi.bind('<Button-1>',click_fun)
multi.grid(row=3, column=3, pady=1)
div = Button(calci, text= "/",width=4, height=1, font=font, bd=4, bg="blue")
div.bind('<Button-1>',click_fun)
div.grid(row=4, column=3, pady=1)
dot =Button(calci, text= ".",width=3, height=1, font=font, bd=4,bg="magenta")
dot.bind('<Button-1>',click_fun)
dot.grid(row=5, column=0, pady=1)
zero = Button(calci, text= "0",width= 3, height=2,bg="gray12",fg="cyan", font=font, bd=4)
zero.bind('<Button-1>',click_fun)
zero.grid(row=5, column=1, pady=1)
sqrt =Button(calci, text= "sqrt",width= 3, height=1, font=font, bd=4,bg="magenta")
sqrt.bind("<Button-1>",click_fun)
sqrt.grid(row=5, column=2, pady=1)
equal = Button(calci, text= "=",width= 5, height=1, font=font, bd=4,bg="green2")
equal.bind("<Button-1>",click_fun)
equal.grid(row=5, column=3, pady=1)
#================================================#
sin = Button(calci, text= "sin",width= 4, height=1, fg="green2", font=font, bd=4, bg="gray36")
sin.bind("<Button-1>",click_fun)
sin.grid(row=1, column=4, pady=1)
cos = Button(calci, text= "cos",width= 4, height=1,fg="green2", font=font, bd=4,bg="thistle")
cos.bind("<Button-1>",click_fun)
cos.grid(row=2, column=4, pady=1)
tan = Button(calci, text= "tan",width= 4, height=1, font=font,fg="green2", bd=4,bg="DarkOrchid")
tan.bind("<Button-1>",click_fun)
tan.grid(row=3, column=4, pady=1)
deg = Button(calci, text= "deg",width= 4, height=1, font=font, bd=4,fg="green2",bg="VioletRed")
deg.bind("<Button-1>",click_fun)
deg.grid(row=4, column=4, pady=1)
fact = Button(calci, text= "fact",width= 4, height=1, font=font,fg="green2", bd=4,bg="cyan")
fact.bind("<Button-1>",click_fun)
fact.grid(row=5, column=4, pady=1)
rad = Button(calci, text= "rad",width= 4, height=1, font=font, bd=4,bg="Hotpink")
rad.bind("<Button-1>",click_fun)
rad.grid(row=1, column=5, pady=1, padx=20)
sinh =Button(calci, text= "sinh",width=4, height=1, font=font, bd=4,bg="DarkOrange")
sinh.bind("<Button-1>",click_fun)
sinh.grid(row=2, column=5, pady=1)
cosh = Button(calci, text= "cosh",width= 4, height=1, font=font, bd=4,bg="tomato")
cosh.bind("<Button-1>",click_fun)
cosh.grid(row=3, column=5, pady=1)
tanh = Button(calci, text= "tanh",width= 4, height=1, font=font, bd=4,bg="wheat")
tanh.bind("<Button-1>",click_fun)
tanh.grid(row=4, column=5, pady=1)
ex = Button(calci, text= "e",width= 4, height=1, font=font, bd=4,bg="tan")
ex.bind("<Button-1>",click_fun)
ex.grid(row=5, column=5, pady=1)
pi = Button(calci, text= "pi",width=4, height=1, font=font, bd=4,bg="ivory2")
pi.bind("<Button-1>",click_fun)
pi.grid(row=1, column=6, pady=1, padx=10)
log= Button(calci, text= "log",width= 4, height=1, font=font, bd=4,bg="sienna")
log.bind("<Button-1>",click_fun)
log.grid(row=2, column=6, pady=1)
ln = Button(calci, text= "ln",width=4, height=1, font=font, bd=4,bg="goldenrod")
ln.bind("<Button-1>",click_fun)
ln.grid(row=3, column=6, pady=1)
log2= Button(calci, text= "log2",width=4, height=1, font=font, bd=4,bg="yellow")
log2.bind("<Button-1>",click_fun)
log2.grid(row=4, column=6, pady=1)
comm= Button(calci, text= ",",width=4, height=1, font=font, bd=4,bg="coral")
comm.bind("<Button-1>",click_fun)
comm.grid(row=5, column=6, pady=1)

# QUIT FUNCTION TO QUIT FROM WINDOW #
def iQuit():
    iQuit = tkinter.messagebox.askyesno("Scientific Calculator",
                " Confirm if you want to exit from calculator?")
    if iQuit >0:
        root.destroy()
        return
# FUNCTION TO OPEN SCIENTIFIC CALCULATOR
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("780x660")
# FUNCTION TO OPEN STANDARD CALCULATOR
def Standard():
    root.resizable(width=False, height=False)
    root.geometry("466x640")

# CREATE MENUBAR #
menubar = Menu(calci)
typesmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label= "Types", menu=typesmenu)
typesmenu.add_command(label="Standard",command=Standard)
typesmenu.add_command(label="Scientific",command=Scientific)
typesmenu.add_separator()
typesmenu.add_command(label="QUIT", command=iQuit)
root.config(menu=menubar)

# MAIN LOOP #
root.mainloop()


