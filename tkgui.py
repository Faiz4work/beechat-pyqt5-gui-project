from tkinter import *
from digi.xbee.devices import XBeeDevice

# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600


main = Tk()
main.geometry("350x400")

# initilizing device
device = XBeeDevice(PORT, BAUD_RATE)
device.open()

last_row = 0
# last_column = 0

def add_message_frame():
    global last_row
    global device
    msg = ent.get()
    ent.delete(0, END)
    device.send_data_broadcast(msg)
    print(msg)
    
    # adding a new frame with message
    new_frame = Frame(main, width=200, height=100, padx=10, pady=10, bg="red")
    new_frame.grid(row=last_row, column=1)
    last_row += 1
    
    new_label = Label(new_frame, text=msg)
    new_label.grid(row=0, column=0)


def add_reply_frame(device_id, message):
    global last_row
    print(message)
    
    # adding a new frame with message
    new_frame = Frame(main, width=200, height=100, padx=10, pady=10, bg="green")
    new_frame.grid(row=last_row, column=0)
    last_row += 1
    
    new_label = Label(new_frame, text=message)
    new_label.grid(row=0, column=0)

def data_receive_callback(xbee_message):
    print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
                                    xbee_message.data.decode()))
    add_reply_frame(xbee_message.remote_device.get_64bit_addr(),
                    xbee_message.data.decode())
device.add_data_received_callback(data_receive_callback)

# f1 = Frame(main, width=100, height=50, padx=10, pady=10, bg="red")
# f1.grid(row=0, column=0)
# flabel = Label(f1, text="this is a message")
# flabel.grid(row=1, column=0)


entry_frame = Frame(main, width=300, height=200, padx=10, pady=10)
entry_frame.grid(row=1000, column=1)
ent = Entry(entry_frame)
ent.grid(row=0, column=0)
btn = Button(entry_frame, text="Send", command=add_message_frame)
btn.grid(row=0, column=1)





main.mainloop()