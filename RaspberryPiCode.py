import time
import RPi.GPIO as GPIO
from os import _exit
import serial
import numpy as np
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BOARD)
#I:E
GPIO.setup(7, GPIO.IN)
#FreR
GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
#VT
GPIO.setup(15, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(23, GPIO.IN)
k = 0
h = 0.15
GPIO.setup(32, GPIO.OUT)
freqPWM = 50
pwm = GPIO.PWM(32, freqPWM)
pwm.start(4)
#ser = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(2)
xs = []
ys = []
#f = open("Datos3.txt", "w")
j1 = 0
x1a = 0.5
while True:
    #x = ser.readline()
    x = "1"
    x1 = x.rstrip()
    if x1 == b'':
        x1 = x1a
    try:
        float(x1)
        x1 = x1
    except:
        x1 = x1a
    if float(x1) > 1:
        x1 = x1a
    x1a = x1
    x2 = float(x1)
    #print('Presión= ', x2)
    xs.append(k * h)
    ys.append(x2)
    #f.write(str(round(k * h, 3)) + '\t')
    #f.write(str(round(x2, 3)) + '\n')
    if(GPIO.input(7) == True):
        aux1 = 3
    if(GPIO.input(7) == False):
        aux1 = 2
    #FR
    if(GPIO.input(3) == False and GPIO.input(5) == False and GPIO.input(11) == False and GPIO.input(13) == False):
        fr = 25 #TH 5
    if(GPIO.input(3) == False and GPIO.input(5) == False and GPIO.input(11) == False and GPIO.input(13) == True):
        fr = 20 #TH 4
    if(GPIO.input(3) == False and GPIO.input(5) == False and GPIO.input(11) == True and GPIO.input(13) == True):
        fr = 15 #TH 3
    if(GPIO.input(3) == False and GPIO.input(5) == True and GPIO.input(11) == True and GPIO.input(13) == True):
        fr = 10 #TH 2
    if(GPIO.input(3) == True and GPIO.input(5) == True and GPIO.input(11) == True and GPIO.input(13) == True):
        fr = 5  #TH 1
	
    #VT
    if(GPIO.input(15) == False and GPIO.input(19) == False and GPIO.input(21) == False and GPIO.input(23) == False):
        aux2 = 1.1 #TH 5
    if(GPIO.input(15) == False and GPIO.input(19) == False and GPIO.input(21) == False and GPIO.input(23) == True):
        aux2 = 1   #TH 4
    if(GPIO.input(15) == False and GPIO.input(19) == False and GPIO.input(21) == True and GPIO.input(23) == True):
        aux2 = 0.9 #TH 3
    if(GPIO.input(15) == False and GPIO.input(19) == True and GPIO.input(21) == True and GPIO.input(23) == True):
        aux2 = 0.8 #TH 2
    if(GPIO.input(15) == True and GPIO.input(19) == True and GPIO.input(21) == True and GPIO.input(23) == True):
        aux2 = 0.7 #TH 1
	
    #Servo-Motor
    j1 = j1 + h
    if j1 <= (60 / ((aux1 + 1) * fr)):
        pwm.ChangeDutyCycle(8 * aux2)
    if j1 > (60 / ((aux1 + 1) * fr)) and j1 <= (60 / fr):
        pwm.ChangeDutyCycle(3.0)
    if j1 > (60 / fr):
        j1 = 0
    time.sleep(h)
    k = k + 1
    if k > 10000 * h:
        pwm.ChangeDutyCycle(3.0)
        pwm.stop()
        GPIO.cleanup()
        #ser.close()
        #f.close()
        #break
    pwm.ChangeDutyCycle(3.0)
    #plt.plot(xs,ys)
    #plt.show()
    #f.close()
    #-exit()