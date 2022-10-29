def on_forever():
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 39)
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 10:
        if Math.random_boolean():
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
            basic.pause(500)
        else:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
            basic.pause(500)
basic.forever(on_forever)
