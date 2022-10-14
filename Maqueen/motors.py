basic.show_icon(IconNames.YES)
basic.show_leds("""
    . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
basic.pause(800)
basic.show_leds("""
    . . # . .
        . . # # .
        # # # # #
        . . # # .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
basic.pause(800)
basic.show_leds("""
    . . # . .
        . # # . .
        # # # # #
        . # # . .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
basic.pause(800)
basic.show_leds("""
    . . # . .
        . . # . .
        # # # # #
        . # # # .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
basic.pause(800)
basic.show_leds("""
    . . # . .
        . # # . .
        # # # # #
        . # # . .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 0)
basic.pause(800)
basic.show_leds("""
    . . # . .
        . . # # .
        # # # # #
        . . # # .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 0)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
basic.pause(800)
basic.show_icon(IconNames.NO)
maqueen.motor_stop(maqueen.Motors.M2)
maqueen.motor_stop(maqueen.Motors.M1)

def on_forever():
    pass
basic.forever(on_forever)
