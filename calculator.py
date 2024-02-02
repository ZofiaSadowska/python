from tkinter import *  

top = Tk()  
top.geometry('300x250')
top.title('calculator')


#first row
division = Button(top,text = '÷',width=5, height=3)
division.grid(row=1, column=3)


#second row

seven = Button(top,text='7', width=5, height=3)
seven.grid(row=2, column =0)
eight = Button(top,text='8', width=5, height=3)
eight.grid(row=2, column=1)
nine = Button(top,text='9', width=5, height=3)
nine.grid(row=2, column=2)
times = Button(top,text = '×',width=5, height=3)
times.grid(row=2, column=3)


# third row

four = Button(top,text='4', width=5, height=3)
four.grid(row=3, column =0)
five = Button(top,text='5', width=5, height=3)
five.grid(row=3, column=1)
six = Button(top,text='6', width=5, height=3)
six.grid(row=3, column=2)
minus = Button(top,text = '-',width=5, height=3)
minus.grid(row=3, column=3)




# fouth row


one = Button(top,text='1', width=5, height=3)
one.grid(row=4, column =0)
two = Button(top,text='2', width=5, height=3)
two.grid(row=4, column=1)
three = Button(top,text='3', width=5, height=3)
three.grid(row=4, column=2)
plus = Button(top,text = '+',width=5, height=3)
plus.grid(row=4, column=3)

# fifth row

sign = Button(top, text="+/-", width=5,height=3)
sign.grid(row=5, column=0)
zero = Button(top, text="0", width=5,height=3)
zero.grid(row=5, column=1)
comma = Button(top,text=',',width=5, height=3)
comma.grid(row=5, column=3)
equal = Button(top, text="=", width=5,height=3)
equal.grid(row=5, column=4)







top.mainloop()  