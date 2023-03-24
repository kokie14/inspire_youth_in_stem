

from machine import Pin 
from time import sleep

led_13=Pin(13,Pin.OUT)
led_14 =Pin(14,Pin.OUT)
led_12 =Pin(12,Pin.OUT)

while True: 
    led_12.value(1)
    led_13.value(0)
    led_14.value(0)
    sleep(1.0)
    led_12.value(0)
    led_13.value(1)
    led_14.value(0)
    sleep(2)
    led_12.value(0)
    led_13.value(0)
    led_14.value(1)
    sleep(0.5)
State=0  #0 means that the light is currently off
if __name__ =='__main__':
    while True:
        print(button.value())
        if button.value() ==0; #key press
        if State ==0:
            led.value(1)
            sleep_ms=100
            while button.value()==0:
                State=1
            else:
                led.value(0)
                sleep_ms=100
                while button.value()==0:
                    State=0


import machine
import time

red_button = machine.Pin(6,machine.Pin.IN,machine.Pin.PULL_UP)
green_button= machine.Pin(6,machine.Pin.IN,machine.Pin.PULL_UP)
yellow_button= machine.Pin(6,machine.Pin.IN,machine.Pin.PULL_UP)

while True:
    if (button.value()):
        button_state =button.value()
        print("button_state",button_state)
        led_12.value(button_state)
        led_13.value(button_state)
        led_14.value(button_state)

while True:
    button_state=button.value()
    print("button_state",button_state)
    led_12.value(button_state)
    led_13.value(button_state)
    led_14.value(button_state)
#idr code
light_sensor = machine.ADC(machine.Pin(28))     # create ADC object on ADC pin


#connected button to 3.3v
while True:
  light_value = light_sensor.read_u16()
  print("Light Intensity :",light_value)
  print("\n\n")
  print("Date ",rtc.datetime()) 
   red_button_state = red_button.value()
  print("Button state", red_button_state) #high / low
  led_12.value(red_button_state)

  blue_button_state = blue_button.value()
  print("Button state", blue_button_state) #high / low
  led_13.value(blue_button_state)

   yellow_button_state = yellow_button.value()
  print("But


import machine
import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

WIDTH  = 128                                            # declaramos el ancho de pantalla OLED
HEIGHT = 64                                             # declaramos la altura de la pantalla OLED
i2c = I2C(0)                                            # Inicializa I2C usando los valores predeterminados de
                                                        # I2C0, SCL= Pin GP9, SDA= Pin GP8, freq = 400000
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Muestra la dirección del dispositivo en la shell o consola
print("I2C Configuration: "+str(i2c))                   # Muestra la configuración I2C en la shell o consola
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) 

rtc  = machine.RTC()
rtc.datetime()

red_led  = machine.Pin(12, Pin.OUT)
blue_led  = machine.Pin(14, Pin.OUT)
yellow_led  = machine.Pin(15, Pin.OUT)

light_Sensor = machine.ADC(machine.Pin(28))

button  = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)

oled.text("Nairobi",5,5)    # escribimos en la columna 5 fila 5
oled.text("Temp :",5,15)           # escribimos en la columna 5 fila 15
oled.text("Hum :",5,35)       # escribimos en la columna 5 fila 35
oled.text("Light :",5,45)         # escribimos en la columna 5 fila 45

# Finalmente actualiza la pantalla oled para que se muestre la imagen y el texto
oled.show()
while True:
    light_value = light_Sensor.adc.read_u16()
    print("Light Intensity :", light_value)
    print("\n\n")
    button_state = button.value()
    print("Button_state", button_state)
    red_led.value(button_state)
    blue_led.value(button_state)
    yellow_led.value(button_state)

