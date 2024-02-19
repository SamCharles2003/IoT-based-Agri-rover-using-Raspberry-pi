import time
import serial.tools.list_ports

device_name = "USB Serial"

def read_usb_port(device_name):
    try:
        ports = list(serial.tools.list_ports.comports())
        print(ports)
        for port, desc, hwid in ports:
            if device_name in desc:
                ser = serial.Serial(port=port, baudrate=9600, timeout=1, write_timeout=1)
                ser.reset_input_buffer()  # Clear any existing data in the buffer
                print(f"Connected to USB port: {port} ({desc})")
                while True:
                    try:
                        data = ser.readline().decode().strip()  # Read data from USB port
                        if data:
                            values_list = data.split()
                            if len(values_list) >= 4:
                                  print("Nitrogen: ",values_list[0],"Phosphorus: ",values_list[1],"Potassium: ", values_list[2],"Moisture: ",values_list[3],end = "\n")
                                  return
                    except serial.SerialException:
                        break  # Break out of the loop on serial exception
                break
        else:
            print(f"No USB device with name '{device_name}' found.")
    except Exception as e:
        print(f"Error: {e}")



def test():
    read_usb_port(device_name)
