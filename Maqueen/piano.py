def on_forever():
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) <= 5:
        music.play_melody("C C C C C C C C ", 500)
    elif maqueen.ultrasonic(PingUnit.CENTIMETERS) <= 10:
        music.play_melody("E E E E E E E E ", 500)
    elif maqueen.ultrasonic(PingUnit.CENTIMETERS) <= 15:
        music.play_melody("G G G G G G G G ", 500)
    elif maqueen.ultrasonic(PingUnit.CENTIMETERS) <= 20:
        music.play_melody("B B B B B B B B ", 500)
    else:
        music.play_melody("C5 C5 C5 C5 C5 C5 C5 C5 ", 500)
    basic.show_icon(IconNames.GHOST)
basic.forever(on_forever)
