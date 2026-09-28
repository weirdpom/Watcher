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
    what_color="#ffff00",
    what_slow_cps=20
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

    nr "The suffocating sensation only seem to proliferate in its intensity as your try to make sense of your surroundings."

    nr "Its murky waters push you onward, refusing any consultation."

    nr "Opening and closing your eyes have no merit. Unable or unwilling. The result remains the same."

    nr "{b}You cannot see.{/b}"  # make bold

    nr "Dawn."

    nr "Dusk."

    nr "You miss them."

    nr "But, such words belong to worlds touched by light. They hold no meaning upon these primordial waves."

    nr "The sea pushes you foward, paralyzing all. You are simply to follow."

    nr "You are nameless."

    nr "You are faceless."

    nr "You are formless."

    nr "Yet not {i}forsaken.{/i}" # make italics

    nr "Nothing but the soul remains."

    nr "Your history has been omitted throughout time itself."

    scene river

    nr "here"

    scene light at right
    with fade

    ve "Why, hello there."

    ve "Enjoying yourself I see."

    return
