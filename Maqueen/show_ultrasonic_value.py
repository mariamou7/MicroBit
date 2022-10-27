def on_forever():
    basic.show_number(maqueen.ultrasonic(PingUnit.CENTIMETERS))
    basic.pause(5000)
basic.forever(on_forever)
