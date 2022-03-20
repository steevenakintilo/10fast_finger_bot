# Python program to determine which
# button was pressed in tkinter

# Import the library tkinter
from tkinter import *
import tkinter
from fast import *
#from fast import *
# Create a GUI app
app = Tk()

# Create a function with one parameter, i.e., of
# the text you want to show when button is clicked
def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

def write_id(path,x):
    f = open(path, "w")
    f.write(str(x))
    f.close

def print_ok():
    for i in range(1000):
        print(i)
def which_button(b,display_res):
    speed_mode = print_file("speed_mode.txt")
    speed_num = print_file("speed_num.txt")
    speed_n = int(speed_num)
    s = speed_mode
    print(b)
    if b == "1":
        if s == "fast":
            fast_bot_multi(speed_n,1)
        else:
            slow_bot_multi(speed_n,1)
    elif b == "2":
        if s == "fast":
            fast_bot_multi(speed_n,2)
        else:
            slow_bot_multi(speed_n,2)
    elif b == "3":
        if s == "fast":
            fast_bot_multi(speed_n,3)
        else:
            slow_bot_multi(speed_n,3)
    elif b == "4":
        if s == "fast":
            fast_bot_multi(speed_n,4)
        else:
            slow_bot_multi(speed_n,4)
    elif b == "5":
        if s == "fast":
            fast_bot_multi(speed_n,5)
        else:
            slow_bot_multi(speed_n,5)
    elif b == "Solo":
        if s == "fast":
            fast_bot(speed_n)
        else:
            slow_bot(speed_n)
    elif b == "Slow Mode":
        write_id("speed_mode.txt","slow")
    elif b == "Fast Mode":
        write_id("speed_mode.txt","fast")
    elif b == "+":
        speed_n = speed_n + 1
        write_id("speed_num.txt",str(speed_n))
    elif b == "-":
        speed_n = speed_n - 1
        if speed_n <= 0:
            speed_n = 0
        write_id("speed_num.txt",str(speed_n))
    elif b == "Quit":
        quit()
    display_res["text"] = "Sleep time " + str(speed_n)

write_id("speed_num.txt","0")
num_to_display = print_file("speed_num.txt")

little_text = tkinter.Label(text="10FastFingerBot",width=0,height=0)
little_text.grid()

# Creating and displaying of button b1

b1 = Button(app, text="1",
			command=lambda m="1": which_button(m,display_time))

b1.grid(padx=10, pady=10)

# Creating and displaying of button b2
b2 = Button(app, text="2",
			command=lambda m="2": which_button(m,display_time))
b2.grid(padx=10, pady=10)

b3 = Button(app, text="3",
			command=lambda m="3": which_button(m,display_time))

b3.grid(padx=10, pady=10)

# Creating and displaying of button b2
b4 = Button(app, text="4",
			command=lambda m="4": which_button(m,display_time))
b4.grid(padx=10, pady=10)

b5 = Button(app, text="5",
			command=lambda m="5": which_button(m,display_time))

b5.grid(padx=10, pady=10)

b6 = Button(app, text="Solo",
			command=lambda m="Solo": which_button(m,display_time))

b6.grid(padx=10, pady=10)


b7 = Button(app, text="Slow Mode",
			command=lambda m="Slow Mode": which_button(m,display_time))

b7.grid(padx=10, pady=10)


b8 = Button(app, text="Fast Mode",
			command=lambda m="Fast Mode": which_button(m,display_time))

b8.grid(padx=10, pady=10)

b8.grid(padx=10, pady=10)

b9 = Button(app, text="+",
			command=lambda m="+": which_button(m,display_time))

b9.grid(padx=10, pady=10)

display_time = tkinter.Label(text="Sleep time " + num_to_display,width=0,height=0,fg="black")
display_time.grid()

b10 = Button(app, text="-",
			command=lambda m="-": which_button(m,display_time))

b10.grid(padx=10, pady=10)

b11 = Button(app, text="Quit",
			command=lambda m="Quit": which_button(m,display_time))

b11.grid(padx=10, pady=10)

# Make the infinite loop for displaying the app
app.geometry("150x870")
app.mainloop()