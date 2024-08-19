from tkinter import *
from tkinter import Tk,ttk
from tkinter import messagebox

# colors --------------
co0 = "#000000" # Black
co1 = "#feffff" # White
co2 = "#007FFF" # green
co3 = "#38576b" # value
co4 = "#403d3d" # letters


# create windown -------

window = Tk()
window.title('')
window.geometry('310x300')
window.configure(background=co1)
window.resizable(width=FALSE, height=FALSE)

# devide window --------------
frame_up = Frame(window, width=310, height=50, bg=co1, relief='flat')
frame_up.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_down = Frame(window, width=310, height=250, bg=co2, relief='flat')
frame_down.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# frame up config ---------------

l_name = Label(frame_up, text='LOGIN', anchor=NE, font=('Terminal 28'), bg=co1, fg=co3)
l_name.place(x=5, y=5)

l_line = Label(frame_up, text='', width=278, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_line.place(x=10, y=45)


informations = ['Dev ', '01234567']    


# function for check password
def check_pass():
    name = e_name.get()
    password = e_pass.get()


    if name == 'admin' and password == 'admin':
        messagebox.showinfo('Login', 'Welcome Administration  ')
    elif informations[0] == name and informations[1]==password:
        messagebox.showinfo('Login','Welcome Back Administration ' + informations[0])
        
        # delete items presents in frame down and frame up:


        for widget in frame_down.winfo_children():
             widget.destroy()

        for widget in frame_up.winfo_children():
            widget.destroy() 

        new_window()       


    else: messagebox.showwarning('Erro', 'Please,Check the correctly name and password' )
       
# function after check ----------
def new_window():

# frame up config ---------------

    l_name = Label(frame_up, text='User: '+informations[0], anchor=NE, font=('Terminal 20'), bg=co1, fg=co4)
    l_name.place(x=5, y=5)

    l_line = Label(frame_up, text='', width=278, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_line.place(x=10, y=45)


    l_name = Label(frame_down, text='Welcome'+informations[0], anchor=NE, font=('Terminal 20'), bg=co1, fg=co4)
    l_name.place(x=5, y=105)

# frame down config------------

l_name1 = Label(frame_down, text='Name *', anchor=NW, font=('Arial 9'), bg=co1, fg=co4)
l_name1.place(x=10,  y=20)
e_name = Entry(frame_down, width=25, justify='left', font=("",  10), highlightthickness=3, relief='solid' )
e_name.place(x=14, y=50)

l_pass =  Label(frame_down, text='password *', anchor=NW, font=('Arial 9'), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_down, width=25, justify='left',show='*',font=("", 10), highlightthickness=3, relief='solid' )
e_pass.place(x=14, y=130)

b_confirm = Button(frame_down, command=check_pass, text='LOGIN', width=10, height=2, justify='center', anchor=NW, font=('Ivy 6'), bg=co0, fg=co2, relief=RAISED, overrelief=RIDGE)
b_confirm.place(x=50, y=180)




window.mainloop()