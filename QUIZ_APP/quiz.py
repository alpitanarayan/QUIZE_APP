import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
answer = messagebox.askyesno("Question","Do you want to start the quiz ?")
if answer:
    root = tk.Tk()
    root.geometry('700x700')
else:
    ans1=messagebox.askretrycancel("Warning","You cann't start the quiz..")
    if ans1:
        messagebox.askyesno("Question","Do you want to start the quiz ?")
        root = tk.Tk()
        root.geometry('700x700')

    

questions = ["1. Who develop the C language ?",
            "2. How many datatype in C ?",
            "3. How is an array initialized in C language ?",
            "4. What is the size of the int data type(in bytes) in C ?",
            "5. How to declare a double-pointer in C ?"
             ]
options = [['Dennis MacAlistair Ritchie', 'Guido van Rossum', 'James Gosling', 'None','Dennis MacAlistair Ritchie'],
            ['31','32','23','30','32'],
            ['int a[2] = {1,2,3};', 'int a = {1,2,3};', 'int a[] = {1,2,3}', 'none','int a[] = {1,2,3};'],
            ['4','2','8','1','4'],
            ['int*var', 'int**var', 'int&var', 'None','int**var'],
            ]

frame_style = tk.Frame(root, padx=10, pady=10,bg='pink')
question_label = tk.Label(frame_style,height=7, width=42,bg='#DB7093',fg="#2F4F4F", 
                          font=("Times", 20, "bold italic"),wraplength=500)


O1 = StringVar(frame_style)
O2 = StringVar(frame_style)
O3 = StringVar(frame_style)
O4 = StringVar(frame_style)

option1 = tk.Radiobutton(frame_style, bg="#FFC0CB", variable=O1, font=("Times", 20, "italic"),
                         command = lambda : check_option(option1))
option2 = tk.Radiobutton(frame_style, bg="#FFC0CB", variable=O2, font=("Times", 20, "italic"), 
                         command = lambda : check_option(option2))
option3 = tk.Radiobutton(frame_style, bg="#FFC0CB", variable=O3, font=("Times", 20, "italic"), 
                         command = lambda : check_option(option3))
option4 = tk.Radiobutton(frame_style, bg="#FFC0CB", variable=O4, font=("Times", 20, "italic"), 
                         command = lambda : check_option(option4))

next_btn = tk.Button(frame_style, text='Next',bg='#8B475D', font=("Times", 20, "bold italic"), 
                        command = lambda : display_next_ques())

frame_style.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)

next_btn.grid(row=6, column=0)


var = 0
right = 0

# disable radiobuttons
def stop_btn(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state


# selected answer
def check_option(ans):
    global right, var

    #comparing selected option by user to the correct option 
    if ans['text'] == options[var][4]:
        right +=1

    var +=1
    stop_btn('disable')


#Display the next question
def display_next_ques():
    global var, right

    if next_btn['text'] == "Restart the quiz":
            right = 0
            var = 0
            question_label['bg'] = '#DB7093'
            next_btn['text'] = "Next"
            question_label['text'] = str(right) + " / " + str(len(options))

        
        

    if var == len(options):
       question_label['text'] = str(right) + " / " + str(len(options))
       next_btn['text'] = 'Restart the quiz'
       if right >= len(options)/2:
           question_label['bg'] = 'green4'
       else:
            question_label['bg'] = 'red'

    else:
        question_label['text'] = questions[var]
        
        stop_btn('normal')
        opts = options[var]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        O1.set(opts[0])
        O2.set(opts[1])
        O3.set(opts[2])
        O4.set(opts[3])

        if var == len(options) - 1:
            next_btn['text'] = 'Check the Results'






display_next_ques()

root.mainloop()
