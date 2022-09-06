from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
from tkinter import ttk

win = Tk()


win.title("Beechat Network")
win.configure(bg="#010523")

win.iconbitmap('logo.ico')


win.geometry("500x500")


header_frame = LabelFrame(win, bg="#010523", border=0)
header_frame.grid(row=0, column=0, columnspan=2, sticky='n')

width =50
height =50
photo= Image.open("logo.png")
photo= photo.resize((width, height),Image.Resampling.LANCZOS)
# create an object of PhotoImage
photoImg = ImageTk.PhotoImage(photo)
win.wm_iconphoto(False, photoImg)
photo_label= Label(header_frame, image=photoImg, bg="#010523")
photo_label.grid(row=0, column=0, rowspan=2)


# Label
public_broadcast = Label(header_frame, text="Public broadcast",
                    font="bold", bg="#010523", fg="white")
public_broadcast.grid(row=0, column=1)


_id = Label(header_frame, text="MY ID: 0013A20041EFD12C",
            font="10", bg="#010523", fg="grey")
_id.grid(row=1, column=1)


main_frame = LabelFrame(win, bg="#010523", border=0)
main_frame.grid(row=1, column=0, padx=30, pady=20)

# frame_1
frame1 = LabelFrame(main_frame, bg="#1f243f", borderwidth=0)
frame1.grid(row=0, column=0, columnspan=2, sticky='w', pady=10)

text = Label(frame1, text="0013A20041EFD12C",font="10", bg="#1f243f", fg="grey")
text.grid(row=0, column=0)

text2 = Label(frame1,text="Hello everyone!",font="10", bg="#1f243f", fg="white")
text2.grid(row=1, column=0)

# frame_2
frame2 = LabelFrame(main_frame, bg="#1f243f", borderwidth=0)
frame2.grid(row=1, column=0, columnspan=2, sticky='w', pady=10)

text3 = Label(frame2, text="0013A20041EFD12C",font="10", bg="#1f243f", fg="grey")
text3.grid()

text4 = Label(frame2,text="Hello everyone! this is a message that is\n 73 characters long. Yes it is",font="10", bg="#1f243f", fg="white")
text4.grid()


# frame_3
# frame3 = LabelFrame(main_frame, bg="blue", borderwidth=0)
# frame3.grid(row=2, column=1, columnspan=2, sticky='e', pady=10)

# text5 = Label(frame3,text="Hello everyone!",font="10",bg="blue", fg="white")
# text5.grid()


# practice
canvas = Canvas(main_frame)
canvas.grid(row=2, column=0, columnspan=2)

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

my_rectangle = round_rectangle(50, 50, 150, 100, radius=20, fill="blue")





win.mainloop()
