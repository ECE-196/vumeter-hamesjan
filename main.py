import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26,  # type: ignore
    board.IO47,
    board.IO33,  # type: ignore
    board.IO34,  # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    print(volume)
    if (volume > 40000):
        for i in range(11):
            leds[i].value = 1
    elif (volume > 35000):
        for i in range(9):
            leds[i].value = 1
    elif (volume > 30000):
        for i in range(7):
            leds[i].value = 1
    elif (volume > 25000):
        for i in range(5):
            leds[i].value = 1
    elif (volume > 20000):
        for i in range(3):
            leds[i].value = 1
    elif (volume > 15000):
        for i in range(1):
            leds[i].value = 1
    else:
        for i in range(11):
            leds[i].value = 0

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
