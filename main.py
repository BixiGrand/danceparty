basic.show_string("Heya!")
basic.show_leds("""
    # . # . #
    . # # # .
    . . # . .
    . # . # .
    . # . # .
    """)
basic.show_leds("""
    # . # # .
    . # # # .
    . . # . .
    . # . # .
    . # . # .
    """)
basic.show_leds("""
    # . # . #
    . # # # .
    . . # . .
    . # . # .
    . # . # .
    """)

def on_forever():
    basic.show_leds("""
        . . # . .
        . # # # .
        # . # . #
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        # # # # #
        # . # . .
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        # # # # .
        . . # # #
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        # # # # #
        . . # . #
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        . # # # #
        # # # . .
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        # # # # #
        # . # . .
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        # # # # .
        . . # # #
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        # # # # #
        . . # . #
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        . # # # #
        # # # . .
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        . # . # .
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # . # .
        . # . # .
        """)
basic.forever(on_forever)
