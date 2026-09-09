define mc = Character(
    "Madison",
    color="#5555ff",
    what_color="#FFFFFF",
    what_slow_cps=25,
    )

define ve = Character(
    "Voice",
    color="#FF0000",
    what_color="#FFFFFF",
    what_slow_cps=25
    )


label start:

    scene black
    with fade

    mc "What the?"

    scene dreamscape at right
    with fade

    ve "Enjoying yourself are you?"

    return
