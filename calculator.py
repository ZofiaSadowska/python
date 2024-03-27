from tkinter import *  
import math
top = Tk()  
top.geometry('300x300')
top.title('calculator')
expression =""
equation = StringVar()




def press(button):                                 
    global expression
    expression = expression + str(button)
    equation.set(expression)


def pierwiastek():
    global expression
    expression = math.sqrt(int(expression))
    equation.set(expression)



def equalpress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)

        expression = ''
    except:
        equation.set("error")
        expression=""    

def clear():
    global expression
    expression = ""
    equation.set("")





expression_field = Entry(top, textvariable = equation)
expression_field.grid(columnspan=10, ipadx=70)





#first row
cancel = Button(top,text='C', width=5, height=3, foreground='red',command=lambda: clear())
cancel.grid(row=2, column=0)
parentheses = Button(top, text='()', width=5, height=3,)
parentheses.grid(row=2, column=1)
percent = Button(top, text='√', width=5, height=3,command=lambda: pierwiastek())
percent.grid(row=2, column=2)
division = Button(top,text = '÷',width=5, height=3,command=lambda: press('/'))
division.grid(row=2, column=3)


#second row

seven = Button(top,text='7', width=5, height=3,command=lambda: press(7))
seven.grid(row=3, column =0)
eight = Button(top,text='8', width=5, height=3,command=lambda: press(8))
eight.grid(row=3, column=1)
nine = Button(top,text='9', width=5, height=3,command=lambda: press(9))
nine.grid(row=3, column=2)
times = Button(top,text = '×',width=5, height=3,command=lambda: press('*'))
times.grid(row=3, column=3)


# third row

four = Button(top,text='4', width=5, height=3,command=lambda: press(4))
four.grid(row=4, column =0)
five = Button(top,text='5', width=5, height=3,command=lambda: press(5))
five.grid(row=4, column=1)
six = Button(top,text='6', width=5, height=3,command=lambda: press(6))
six.grid(row=4, column=2)
minus = Button(top,text = '-',width=5, height=3,command=lambda: press('-'))
minus.grid(row=4, column=3)




# fouth row


one = Button(top,text='1', width=5, height=3, command=lambda: press(1))
one.grid(row=5, column =0)
two = Button(top,text='2', width=5, height=3,command=lambda: press(2))
two.grid(row=5, column=1)
three = Button(top,text='3', width=5, height=3,command=lambda: press(3))
three.grid(row=5, column=2)
plus = Button(top,text = '+',width=5, height=3,command=lambda: press('+'))
plus.grid(row=5, column=3)

# fifth row

sign = Button(top, text="+/-", width=5,height=3)
sign.grid(row=6, column=0)
zero = Button(top, text="0", width=5,height=3,command=lambda: press(0))
zero.grid(row=6, column=1)
comma = Button(top,text=',',width=5, height=3)
comma.grid(row=6, column=2)
equal = Button(top, text="=", width=5,height=3, bg='gray',command=lambda: equalpress())
equal.grid(row=6, column=3)





top.mainloop()  
