from digi.xbee.devices import XBeeDevice

# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600


def main():
    print(" +-----------------------------------------+")
    print(" |     Beechat Network PC dev chat app     |")
    print(" +-----------------------------------------+\n")
    device = XBeeDevice(PORT, BAUD_RATE)
     

    try:
        device.open()
        def data_receive_callback(xbee_message):
            print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
                                    xbee_message.data.decode()))

        device.add_data_received_callback(data_receive_callback)

        while(True):
            MSG = input("Type a message to broadcast:\n")
            device.send_data_broadcast(MSG)
            print("\n")

    except(KeyboardInterrupt):
        print("Quitting application.")

    finally:
        if device is not None and device.is_open():
            device.close()



if __name__ == '__main__':
    main()
