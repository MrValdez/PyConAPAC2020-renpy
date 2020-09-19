define hero = Character("Hero")
define alex = Character("Alex")


label start:

# example code for python:
#    python:
#        import requests
#        import webbrowser
#        import certifi

#        # https://lemmasoft.renai.us/forums/viewtopic.php?p=474569#p474569
#        # The path to the certificate file used to verify secure websites.
#        ca_file = os.path.join(config.gamedir, certifi.where())

#        if not os.path.exists(ca_file):
#            ca_file = os.path.join(config.savedir, "cacert.pem")

#            with open(ca_file, "wb") as f:
#                f.write(renpy.file("python-packages/certifi/cacert.pem").read())

#        url = "https://random.dog/woof.json"
#        r = requests.get(url, verify=ca_file)
#        data = r.json()

#        # webbrowser.open(data["url"])

#    scene bg black
#    with fade

#    "this is the story of [data[url]]"


    scene bg meadow
    with fade

    python:
        alex.name = renpy.input("What is your name?")

    show hero walking

    hero "Hello [alex]. Welcome to PyCon APAC 2020"

    show hero walking at right
    with moveinright

    hero "What is this?"

    show alex gasp at left
    with moveinleft

    alex "How {size=+5}{b}adorable{/b}"

    show alex offer
    show hero thinking

    $ secret_ending = True

    menu:
        hero "Am I a good boy?"
        
        "Yes, I am":
            jump good_ending
        
        "No, I am not":
            jump bad_ending

        "secret ending" if secret_ending:
            jump secret_ending

    return

label good_ending:
    show hero love at left
    with moveinleft
    show alex behind hero

    "good ending"
    return

label bad_ending:
    with vpunch

    show alex surprise

    show hero bark
    hide hero
    with moveoutright

    "bad ending"
    return

label secret_ending:
    init python:
        class MiniGame(renpy.Displayable):
            def __init__(self):
                renpy.Displayable.__init__(self)
                
                self.image = renpy.displayable("hero bark") 
                self.pos = [0, 0]

            def render(self, width, height, st, at):
                screen = renpy.Render(width, height)

                
                sprite = renpy.render(self.image, width, height, st, at)
                self.pos = renpy.get_mouse_pos()
                screen.blit(sprite, (self.pos[0], self.pos[1]))

                # Have renpy redraw this Displayable. Otherwise, we'll be stuck in one frame
                renpy.redraw(self, 0)

                return screen

            def event(self, ev, x, y, st):
                import pygame
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    return True

    image bg blank = Color("#000000")
    screen minigame():
        default minigame = MiniGame()

        add "bg blank"
        add minigame

        text "[alex]'s imagination":
            xpos 200
            ypos 50
            size 40

    call screen minigame