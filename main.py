# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import serial
import binascii
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

print('serial'+serial.__version__)

ser=serial.Serial('COM8', 115200, timeout=1)

count = 0
hexValue = 0
data = 0
b_arr = 0
arr = []
while(count < 3):
    if ser.readable():
        y = ser.readline()
    x = ser.read()
    #print(x)
    byte = y
    data = byte.hex() #binbary -> hex값으로 변경
    #print(byte.hex())
    print(data)
    arr_data = ' '.join([data[x:x+2] for x in range(0,len(data),2)])
    print(arr_data)
    print("data len:", end="")
    print(len(data))

    b_arr = bytearray.fromhex(arr_data) #b'\x02\x0b ... 으로 변경
    print(b_arr)
    arr = b_arr
    print(arr_data[0], arr_data[1], arr_data[2], arr_data[3])

    #print(b_arr[0], b_arr[1], b_arr[2], b_arr[3])
    #arr_data
   # hexValue = binascii.b2a_hex(x)

    count = count + 1
    if hexValue == b'ff':
        count = count + 1

fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(0, 30))
line, = ax.plot([], [], lw=2)

max_points = 50
line, = ax.plot(np.arange(max_points), np.ones(max_points, dtype=np.float)*np.nan, lw=2)

def init():
    return line,

def animate(i):
    y = serial.readline()
    y = y.decode()[:-2]
    y = float(y)

    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=False)

plt.show()

"""
#set a port number&baud rate

PORT = 'COM6'
BaudRate = 115200

ARD=(serial.Serial(PORT, BaudRate))


ARD.readline()
def Decode(A):
    A=A.decode()
    A=str(A)
    if (A[0]=='0x0D'):
        if (len(A)==10):
            Ard1=int(A[1:4])
            Ard2=int(A[4:8])
            result=[Ard1,Ard2]
            return result
        else:
            print("error_lack of number _ %d"%len(A))
            return False
    else:
        print("error_wrong signal")
    return False

def Ardread():

    if ARD.readable():
        LINE=ARD.readline()
        code=Decode(LINE)
        print(code)

        return code

    else:
        print("읽기 실패 from_Ardread")

    while(True):
        Ardread()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""