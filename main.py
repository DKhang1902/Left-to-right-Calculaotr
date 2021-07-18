import tkinter as tk
root = tk.Tk()
root.title("Simple Calculator")

E = tk.Entry(root, width=60, borderwidth=5)
E.grid(row=0, column=0,columnspan=5, padx=10,pady=10)

display = ""

def button_add(number):
    global display
    display = E.get()
    number = str(number)
    display+= number
    E.delete(0,"end")
    E.insert(0,display)

def clear_all():
    global display
    E.delete(0,'end')
    E.insert(0,"")
    display= ""

def calculate(it,a,b):
    if it == "+":
        return str(float(a) + float(b))
    if it == "-":
        return str(float(a) - float(b))
    if it == "x":
        return str(float(a) * float(b))
    if it == ":":
        return str(float(a) / float(b))

    
def final_answer(list):
    current_number = ""
    current_op = ""
    answer = ""
    for thing in list:
        if thing in ['0','1','2','3','4','5','6','7','8','9']:
            current_number += thing
        elif thing in ['+','-','x',':']:
            if current_op == "":
                current_op = thing
                answer=current_number
                current_number = ""
            else:
                answer = calculate(current_op,answer,current_number)
                current_number = ""
                current_op= thing
        elif thing == "=":
            equals = list.count("=")
            answer = calculate(current_op,answer,current_number)
            current_number = ""
            if equals > 1:
                clear_all()
                E.insert(0,"Press CLEAR to continue")
                answer = ""
                current_number = ""
                break
    button_add(answer)
    

        
button_1 = tk.Button(root,text="1",padx=40,pady=30,command=lambda:button_add(1))
button_2 = tk.Button(root,text="2",padx=40,pady=30,command=lambda:button_add(2))
button_3 = tk.Button(root,text="3",padx=40,pady=30,command=lambda:button_add(3))
button_4 = tk.Button(root,text="4",padx=40,pady=30,command=lambda:button_add(4))
button_5 = tk.Button(root,text="5",padx=40,pady=30,command=lambda:button_add(5))
button_6 = tk.Button(root,text="6",padx=40,pady=30,command=lambda:button_add(6))
button_7 = tk.Button(root,text="7",padx=40,pady=30,command=lambda:button_add(7))
button_8 = tk.Button(root,text="8",padx=40,pady=30,command=lambda:button_add(8))
button_9 = tk.Button(root,text="9",padx=40,pady=30,command=lambda:button_add(9))
button_0 = tk.Button(root,text="0",padx=40,pady=30,command=lambda:button_add(0))
button_clear = tk.Button(root,text="CLEAR",padx=25.5,pady=30,command=clear_all)
button_equal = tk.Button(root,text="=",padx=40,pady=30,command= lambda:[button_add("="),final_answer(display)])

button_addition = tk.Button(root, text="+",padx=40, pady=30, command=lambda: button_add("+"))
button_subtraction = tk.Button(root, text="-",padx=40, pady=30,command=lambda: button_add("-"))
button_multiplication = tk.Button(root, text="x",padx=40, pady=30,command=lambda: button_add("x"))
button_division = tk.Button(root, text=":",padx=40, pady=30,command=lambda: button_add(":"))


button_1.grid(row=1, column=1)
button_2.grid(row=1, column=2)
button_3.grid(row=1, column=3)
button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)
button_7.grid(row=3, column=1)
button_8.grid(row=3, column=2)
button_9.grid(row=3, column=3)
button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_equal.grid(row=4, column=3)
button_addition.grid(row=1,column=4)
button_subtraction.grid(row=2,column=4)
button_multiplication.grid(row=3,column=4)
button_division.grid(row=4,column=4)


root.mainloop()

