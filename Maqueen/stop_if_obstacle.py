def on_forever():
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) > 25:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 150)
        basic.pause(500)
    else:
        maqueen.motor_stop(maqueen.Motors.ALL)
        basic.pause(500)
basic.forever(on_forever)
