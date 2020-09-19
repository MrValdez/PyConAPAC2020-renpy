image bg:
    "bg.jpg"
    zoom 0.4

define header = Character(None, kind=nvl,
    font="Candara", what_size=50, what_bold=True, what_outlinecolor="#00ff00", what_xalign=.5, what_text_align=.5,
)

define text = Character(None, kind=nvl,
    font="Arial", what_size=40,
)

init python:
    gui.nvl_text_xpos = 10
    gui.nvl_text_width = None

    # spacing between text
    gui.nvl_height = None
    gui.nvl_spacing = 10

    # text outline
    gui.dialogue_text_outlines = [
        (2, "#000000", 0, 0)      # parameters = (Stroke/Outline width, Color, X offset, Y offset)
    ]

init:
    style nvl_window:
        background None

# override main menu to skip it
label main_menu:
    return

label start:
    show title:
        zoom 1.1
        xalign 0.5 ypos -0

    $ renpy.pause()

    scene bg
    with fade

    # we use call instead of jump to pass control to the label
    call slide_introduction from _call_slide_introduction
    call slide_visual_novel from _call_slide_visual_novel
    call slide_what_is_renpy from _call_slide_what_is_renpy
    call slide_live_coding from _call_slide_live_coding
    call slide_end from _call_slide_end

    $ renpy.quit()
    return

label slide_template:
    nvl clear

    # {nw} tag means no-wait
    header "Lorem ipsum.{nw}"
    text "Lorem ipsuum"

    # show an image on slide. We put this on the same layer as nvl
    # unfortunately, we need to position this manually
    show image_name onlayer overlay:
        #size (100, 100)
        zoom .5
        xalign 0.5 yalign 0.7

    # we need to return so the next label won't be called
    return

# Normally, we would put these labels in a different file for organization
label slide_introduction:
    nvl clear

    # {nw} tag means no-wait
    header "About Me{nw}"

    show sony onlayer overlay:
        xalign 0.5 ypos 160
        zoom .8

    text "Hi. I'm Sony Valdez. Gamer. Programmer. Mostly harmless."
    text "Teach Python. One of the founders of Python Philippines."
    text "I use Ren'Py to teach simple programming and\n how to do project management to non-programmers"
    text "In this talk, we will make a simple game in under 20 minutes.\n I'll be sharing the source code after the talk."
    text "If you have questions, feel free to ask in chat.\n I'll get back to them after my talk."

    return

label slide_visual_novel:
    call slide_what_is_visual_novel from _call_slide_what_is_visual_novel
    call slide_visual_novel_examples_1 from _call_slide_visual_novel_examples_1
    call slide_visual_novel_examples_2 from _call_slide_visual_novel_examples_2
    call slide_visual_novel_examples_3 from _call_slide_visual_novel_examples_3
    call slide_visual_novel_examples_4 from _call_slide_visual_novel_examples_4
    call slide_visual_novel_examples_5 from _call_slide_visual_novel_examples_5
    call slide_visual_novel_examples_6 from _call_slide_visual_novel_examples_6
    call slide_visual_novel_examples_7 from _call_slide_visual_novel_examples_7
    
    return

label slide_what_is_visual_novel:
    nvl clear
    header "What are Visual Novels?{nw}"

    text "They are games focused on stories with multiple branching paths."
    text "Most of the gameplay is just reading... literally like reading a novel!"
    text "Some high production visual novels have voice acting."
    text "The popular ones can sometimes become anime."
    text "There are different story genres such as Romance, Action, Mystery, and Horror."
    text "Some visual novels even combine different game genres!"

    return

label slide_visual_novel_examples_1:
    nvl clear
    header "7 Visual Novel examples{nw}"

    show steins gate onlayer overlay:
        zoom .48
        xalign 0.5 ypos 150

    text "1. Steins;Gate (mystery story that has been adopted into anime)"

    return

label slide_visual_novel_examples_2:
    nvl clear
    header "7 Visual Novel examples{nw}"

    show long live the queen onlayer overlay:
        zoom 1.8
        xalign 0.5 ypos 150

    text "2. Long Live The Queen (Simulation game)"

    return

label slide_visual_novel_examples_3:
    nvl clear
    header "7 Visual Novel examples{nw}"

    show the yahwg onlayer overlay:
        zoom 0.8
        xalign 0.5 ypos 150

    text "3. The Yawhg (one hour 1-4 players rpg about the world ending)"

    return

label slide_visual_novel_examples_4:
    nvl clear
    header "7 Visual Novel examples{nw}"

    show phoenix wright onlayer overlay:
        zoom .48
        xalign 0.5 ypos 150

    text "4. Phoenix Wright (court room puzzle drama)"

    return

label slide_visual_novel_examples_5:
    nvl clear
    header "7 Visual Novel examples{nw}"

    show persona 4 onlayer overlay:
        zoom .48
        xalign 0.5 ypos 150

    text "5. Persona 4 Golden (dungeon rpg with visual novel elements)"

    return

label slide_visual_novel_examples_6:
    nvl clear
    header "7 Visual Novel examples{nw}"

    show melty blood onlayer overlay:
        zoom .55
        xalign 0.5 yalign 0.7

    text "6. Melty Blood (a shonen visual novel combined with a fighting game)"
    return

label slide_visual_novel_examples_7:
    nvl clear
    header "7 Visual Novel examples{nw}"

    show the letter onlayer overlay:
        zoom .5
        xalign 0.5 yalign 0.7

    text "7. The Letter (horror visual novel)"
    return

label slide_what_is_renpy:
    call slide_what_is_renpy_1 from _call_slide_what_is_renpy_1
    call slide_what_is_renpy_2 from _call_slide_what_is_renpy_2
    call slide_what_is_renpy_3 from _call_slide_what_is_renpy_3
    return

label slide_what_is_renpy_1:
    nvl clear

    header "What is Ren'Py?{nw}"

    show renpy onlayer overlay:
        zoom 1.7
        xalign 0.95 yalign 0.7
    show runs_on onlayer overlay:
        zoom 1.5
        xalign 0.2 yalign 0.7

    text "Ren'py is a game engine built on top of pygame and Python.\n\nIt is used to make visual novels.\nIt is designed to be usable by non-programmers\n\nhttps://www.renpy.org/"

    return

label slide_what_is_renpy_2:
    nvl clear

    header "What is Ren'Py?{nw}"

    show renpy onlayer overlay:
        zoom 1.7
        xalign 0.95 yalign 0.7

    show pygame onlayer overlay:
        xalign 0.4 yalign 0.7

    text "Programmers can access Python and pygame to do advanced stuff like create minigames and connecting to the Internet\n\nA lot of ren'py visual novels are sold in\n itch.io, Steam, Google Play Store,\n and Apple's App Store"

    return

label slide_what_is_renpy_3:
    nvl clear

    header "What is Ren'Py?{nw}"

    show renpy onlayer overlay:
        zoom 1.7
        xalign 0.95 yalign 0.7

    text "Still under active development!\n\nDisclaimer: I contribute to Ren'Py's Patreon to support\nthe game engine's development."

    return

label slide_live_coding:
    nvl clear

    # {nw} tag means no-wait
    header "Live coding{nw}"
    text "Let's make a simple {size=50}{b}visual novel{/b}{/size}!"

    return

label slide_end:
    call slide_extra from _call_slide_extra
    call slide_surprise from _call_slide_surprise
    call slide_resources from _call_slide_resources
    return

label slide_extra:
    nvl clear
    header "Source code{nw}"

    text "After this session ends, I'll be pushing the code and this presentation to my github:{nw}"
    text "{b}https://github.com/MrValdez{/b}"
    
    text "I'll also be including a minigame so the programmers in the audience can see how to access pygame with ren'py."
    text "(Do we have time? I can show the minigame)"

    return

label slide_surprise:
    nvl clear
    header "Suprise{nw}"

    text "Now for a surprise on this presentation."
    text "This slide show is actually built on Ren'Py!"

    show mrvaldez at right:
        zoom 1
        yalign 0.3
    show hero bark:
        xzoom -1
        yalign 0.5
    show alex cry at right:
        xalign 0.5 yalign 0.4
        zoom 1.3

    with pixellate

    "Sony Valdez" "{size=+10}{outlinecolor=#111111}Hello there"
    hide mrvaldez
    hide alex
    hide hero

    text "I will be sharing the source code so if you are interested\nin looking at how I made a visual novel presentation,\nyou can study how I did it"
    text "I'll also make a writeup on my personal website\non how I coded this presentation."

    return

label slide_resources:
    nvl clear
    header "Resources{nw}"

    text "{b}You can find the source code for this presentation at:{/b}\n - https://github.com/MrValdez/PyConAPAC2020-renpy{nw}"

    text "{b}My personal website:{/b}\n - https://MrValdez.ph{nw}"

    text "{b}You can find me on twitter:{/b}\n- https://twitter.com/MrValdez{nw}"
    
    text "{b}You can find more of Richel Valdez's art at{/b}\n https://SimplyRara.com{nw}"
    text "{b}Her Instagram is {/b} raravaldez"

    show hero and alex onlayer overlay:
        zoom 1.7
        xalign 0.98 yalign 0.5

    text "Any questions?"

    return