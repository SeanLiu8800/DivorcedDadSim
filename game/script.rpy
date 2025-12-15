# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.
define kid = Character("Kid", color="#00b3ff")
define dad = Character("Dad", color="#0037ff")

# Declare Backgrounds
image bg frontdoor = im.Scale("bg tempfrontdoor.png", 1920, 1080)

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg frontdoor

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # show eileen happy

    # These display lines of dialogue.
    "{i}This is the beginning of Divorced Dad Sim (Title Pending)"

    kid "coding with RenPy is definitely gonna need some getting used to"

    kid "ayo is that a f*ckin' DOG?"

    dad ".{cps=1}.."

    show screen example 
    play sound "audio/vine-boom.mp3"

    ""

    # This ends the game.
    return

screen example():
    add "its-cold-out-imma-wear-my-jamas-question-mark-dog-restored-v0-009m4oh1o0b91.webp": 
        align (0.5, 0.2)