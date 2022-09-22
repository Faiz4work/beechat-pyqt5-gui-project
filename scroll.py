from faulthandler import cancel_dump_traceback_later
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.title("Beechat Networks")
root.configure(bg="#010523")
root.iconbitmap('logo.ico')
root.geometry("400x500")

frame_main = tk.Frame(root, bg="#010523")
frame_main.grid(sticky='news')

# ********************header frame********************************

header_frame = LabelFrame(frame_main, bg="#010523", border=0, pady=10)
header_frame.grid(row=0, column=0, columnspan=2, sticky='ew')

width = 60
height = 60
photo= Image.open("logo.png")
photo= photo.resize((width, height),Image.ANTIALIAS)

# create an object of PhotoImage
photoImg = ImageTk.PhotoImage(photo)
photo_label= Label(header_frame, image=photoImg, bg="#010523")
photo_label.grid(row=0, column=0, rowspan=2)


# Label
public_broadcast = Label(header_frame, text="Public broadcast",
                    font="bold", bg="#010523", fg="white")
public_broadcast.grid(row=0, column=1)


_id = Label(header_frame, text="MY ID: 0013A20041EFD12C",
            font="10", bg="#010523", fg="grey")
_id.grid(row=1, column=1, padx=10)

# ********************end of header frame*************************


# Create a frame for the canvas with non-zero row&column weights
frame_canvas = tk.Frame(frame_main)
frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)


# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas, bg="#010523")
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(frame_canvas, orient=VERTICAL, command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

# Create a frame to contain the buttons
frame_buttons = tk.Frame(canvas, bg="blue")


# Add 9-by-5 buttons to the frame
last_frame_row = 3



frame_canvas.config(width=400, height=300)


# Entering self msg frame with text
def add_msg_frame():
    global last_frame_row
    global canvas
    global vsb
    msg = "This is a test msg"
    # msg = e.get()
    # e.delete(0, END)
    new_frame = Frame(frame_buttons, bg="#4857a8", borderwidth=0)
    new_frame.grid(row=last_frame_row, column=1, columnspan=2, sticky='e', pady=5)
    last_frame_row += 1
    
    new_label = Label(new_frame, text=msg, font="10", bg="#4857a8", fg="white")
    new_label.grid(row=0, column=0)
    
    canvas.config(scrollregion=canvas.bbox("all"), yscrollcommand=vsb.set)
    


def add_reply_msg(device_id="0983ADFCD9827sd", msg="this is a sample message"):
    global last_frame_row
    new_frame = Frame(frame_buttons, bg="#1f243f", borderwidth=0)
    new_frame.grid(row=last_frame_row, column=0, columnspan=2, sticky='w', pady=5)
    last_frame_row += 1
    
    new_label = Label(new_frame, text=device_id, bg="#1f243f", font="10", fg="#a6a6a6")
    new_label.grid(row=0, column=0)
    
    new_label2 = Label(new_frame, text=msg, font="10", bg="#1f243f", fg="white")
    new_label2.grid(row=1, column=0)
    
    canvas.config(scrollregion=canvas.bbox("all"), yscrollcommand=vsb.set)




# add_reply_msg()
# add_reply_msg()
# add_msg_frame()

# frame_buttons.update_idletasks()


# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"), yscrollcommand=vsb.set)
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# # Entry
eFrame = Frame(root, width=400, height=100)
eFrame.grid(row=1000, column=0)

e = Entry(eFrame, width=50)
e.grid(row=0, column=0)

ebtn = Button(eFrame, text="Send", bg="skyblue", command=add_msg_frame)
ebtn.grid(row=0, column=1)

# Launch the GUI
root.mainloop()