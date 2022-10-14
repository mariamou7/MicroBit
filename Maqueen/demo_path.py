basic.show_icon(IconNames.YES)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 100)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 100)
basic.pause(1100)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
basic.pause(1000)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
basic.pause(700)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 70)
basic.pause(700)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
basic.pause(200)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 200)
basic.pause(750)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 200)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 200)
basic.pause(1500)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
basic.pause(1100)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
basic.pause(300)
basic.show_leds("""
    # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
""")
maqueen.motor_stop(maqueen.Motors.M2)
maqueen.motor_stop(maqueen.Motors.M1)

def on_forever():
    pass
basic.forever(on_forever)
