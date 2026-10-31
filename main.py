pins.set_pull(DigitalPin.P1, PinPullMode.PULL_DOWN)

def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 1)
    basic.pause(10)
    basic.show_number(pins.analog_read_pin(AnalogReadWritePin.P1))
    if pins.analog_read_pin(AnalogReadWritePin.P1) > 40:
        music.play(music.string_playable("B A C5 C E C5 A G ", 120),
            music.PlaybackMode.UNTIL_DONE)
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.pause(5000)
basic.forever(on_forever)
