basic.show_icon(IconNames.YES)
basic.show_leds("""
    . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 100)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 100)
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
basic.pause(600)
basic.show_leds("""
    . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
basic.pause(400)
basic.show_leds("""
    . . # . .
        . # # . .
        # # # # #
        . # # . .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 70)
basic.pause(500)
basic.show_leds("""
    . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
basic.pause(50)
basic.show_leds("""
    . . # . .
        . # # . .
        # # # # #
        . # # . .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 200)
basic.pause(300)
basic.show_leds("""
    . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 200)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 200)
basic.pause(1200)
basic.show_leds("""
    . . # . .
        . . # # .
        # # # # #
        . . # # .
        . . # . .
""")
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
basic.pause(900)
basic.show_leds("""
    . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
""")
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
