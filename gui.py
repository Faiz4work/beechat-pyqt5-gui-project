from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
win = Tk()


win.title("Hello Python")
win.configure(bg="#010523")
win.iconbitmap('logo.ico')
win.geometry("400x500")
last_frame_row = 3

header_frame = LabelFrame(win, bg="#010523", border=0)
header_frame.grid(row=0, column=0, columnspan=2, sticky='w')

width =50
height =50
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
_id.grid(row=1, column=1)


# creating for scroll bar
wrapper1 = Frame(win)
wrapper1.grid(sticky='news')

main_frame = Frame(wrapper1, bg="#010523")
main_frame.grid(row=1, column=0, pady=(5, 0), sticky='nw')
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

canvas = Canvas(main_frame, bg='yellow')
canvas.grid(row=0, column=0, sticky='news')

# Link a scrollbar to the canvas
vsb = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

# Create a frame to contain the messages
msg_frame = Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=msg_frame, anchor='nw')

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))

main_frame.config(width=400, height=400)
msg_frame.update_idletasks()

# frame_1
frame1 = LabelFrame(msg_frame, bg="#1f243f", borderwidth=0)
frame1.grid(row=0, column=0, columnspan=2, sticky='w', pady=5)

text = Label(frame1, text="0013A20041EFD12C",font="10", bg="#1f243f", fg="grey")
text.grid(row=0, column=0)

text2 = Label(frame1,text="Hello everyone!",font="10", bg="#1f243f", fg="white")
text2.grid(row=1, column=0)

# frame_2
frame2 = LabelFrame(msg_frame, bg="#1f243f", borderwidth=0)
frame2.grid(row=1, column=0, columnspan=2, sticky='w', pady=5)

text3 = Label(frame2, text="0013A20041EFD12C",font="10", bg="#1f243f", fg="grey")
text3.grid()

text4 = Label(frame2,text="Hello everyone! this is a message that is\n 73 characters long. Yes it is",font="10", bg="#1f243f", fg="white")
text4.grid()


# frame_3
frame3 = LabelFrame(msg_frame, bg="blue", borderwidth=0)
frame3.grid(row=2, column=1, columnspan=2, sticky='e', pady=5)

text5 = Label(frame3,text="Hello everyone!", font="10", bg="#4857a8", fg="white")
text5.grid()


# Entering self msg frame with text
def add_msg_frame():
    global last_frame_row
    msg = e.get()
    e.delete(0, END)
    new_frame = Frame(msg_frame, bg="#4857a8", borderwidth=0)
    new_frame.grid(row=last_frame_row, column=1, columnspan=2, sticky='e', pady=5)
    last_frame_row += 1
    
    new_label = Label(new_frame, text=msg, font="10",bg="blue", fg="white")
    new_label.grid(row=0, column=0)


def add_reply_msg(device_id="0983ADFCD9827sd", msg="this is a sample message"):
    global last_frame_row
    new_frame = Frame(msg_frame, bg="#1f243f", borderwidth=0)
    new_frame.grid(row=last_frame_row, column=0, columnspan=2, sticky='w', pady=5)
    last_frame_row += 1
    
    new_label = Label(new_frame, text=device_id, bg="#1f243f", font="10", fg="#a6a6a6")
    new_label.grid(row=0, column=0)
    
    new_label2 = Label(new_frame, text=msg, font="10", bg="#1f243f", fg="white")
    new_label2.grid(row=1, column=0)
    

# def data_receive_callback(xbee_message):
#     print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
#                                     xbee_message.data.decode()))
#     add_reply_msg(xbee_message.remote_device.get_64bit_addr(),
#                     xbee_message.data.decode())
# device.add_data_received_callback(data_receive_callback)

# # Entry
eFrame = Frame(win, width=400, height=100)
eFrame.grid(row=1000, column=0)

e = Entry(eFrame, width=50)
e.grid(row=0, column=0)

ebtn = Button(eFrame, text="Send", bg="skyblue", command=add_reply_msg)
ebtn.grid(row=0, column=1)


win.mainloop()