define mc = Character(
    "Madison",
    color="#5555ff",
    what_color="#FFFFFF",
    )

define ve = Character(
    "Voice",
    color="#FF0000",
    what_color="#FFFFFF",
    )

# narrator
define nr = Character(
    "",
    color="#00557f",
    what_color="#ffff7f",
    )

define mr = Character(
    "monster",
    color="#FF0000",
    what_color="#FFFFFF",
    )

image bg mixed = "images/mixed_background.png"


label start:
    
    play music "audio/hitslab-scary-creepy-horror-music-430823.mp3" volume 0.3

    scene bg mixed
    with fade

    nr "Finally awaken, only to discover a sea of eternal darkness."

    nr "Its murky waters push you foward, refusing consultation."

    nr "Opening and closing your eyes have no merit. Unable or unwilling. The result remains the same."

    nr "Dawn. Dusk. Such words belong to worlds touched by light. They hold no meaning upon the primordial waves."

    nr "The sea pushes onward paralyzing all. You are simply to follow."

    scene light at right
    with fade

    ve "Why, hello there."

    ve "Enjoying yourself I see."

    return
