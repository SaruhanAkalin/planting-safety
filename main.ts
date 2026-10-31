pins.setPull(DigitalPin.P1, PinPullMode.PullDown)
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P0, 1)
    basic.pause(10)
    basic.showNumber(pins.analogReadPin(AnalogReadWritePin.P1))
    if (pins.analogReadPin(AnalogReadWritePin.P1) > 40) {
        music.play(music.stringPlayable("B A C5 C E C5 A G ", 120), music.PlaybackMode.UntilDone)
    }
    pins.digitalWritePin(DigitalPin.P0, 0)
    basic.pause(5000)
})
