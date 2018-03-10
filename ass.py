#!/usr/bin/env python3


from ev3dev.ev3 import *
from time import sleep

speed = 500
cl = ColorSensor("in4")
assert cl.connected, "Подключите датчик цвета EV3 в любой порт"
# Переводим датчик в режим измерения освещенности
# в этом режиме датчик выдает освещенность 0..100%
cl.mode='COL-REFLECT'
ts = TouchSensor("in2")
# проверка, подключен ли датчик
# программа завершится с сообщением, если датчик не подключен
us = UltrasonicSensor('in3')
assert us.connected
us.mode='US-DIST-CM'
units = us.units
barrierDistance = 35 # критическое расстояние до барьера
barrierCount = 0 # счёстчик количество поворотов


assert ts.connected, "Подключите датчик касания в любой порт"

motorLeft = LargeMotor('outD')
assert motorLeft.connected, 'Connect left motor in  por D'
motorRight = LargeMotor('outC')
assert motorRight.connected, 'Connect left motor in  por C'
    


while not ts.value():
   sleep(0.5)

colorBlack=cl.value()
print(colorBlack)

sleep(1)

while not ts.value():
    sleep(0.5)

colorWhite=cl.value()
print(colorWhite)

sleep(0.5)
summ=((colorBlack+colorWhite)/2)
print(summ)

while True:
    distance=us.value()/10 #переводим см в мм
    motorLeft.run_forever (speed_sp = speed/2)
    motorRight.run_forever(speed_sp = -speed/2)
   
    
    
    if  distance < barrierDistance:
        motorLeft.stop() #остановка робота
        motorRight.stop()
        sleep(0.5)
        motorLeft.run_forever(speed_sp = speed) #задали скорость -900.900
        motorRight.run_forever(speed_sp = speed)

        while cl.value()>summ:
            sleep(0.1)
            
        motorLeft.stop()
        motorRight.stop()
        sleep(1)

        motorLeft.run_forever(speed_sp=-speed)
        motorRight.run_forever(speed_sp=-speed)
        sleep(4)

        barrierCount+=1
        if barrierCount>3:
           break
    if barrierCount>3:
        break

motorLeft.stop
motorRifht.stop
