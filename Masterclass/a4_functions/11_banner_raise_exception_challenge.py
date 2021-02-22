def banner_text(text, screen_width=80):     #we can pass arguments with default value
    if len(text) > screen_width - 4:
        raise ValueError("the string '{0}' is not a valid for {1} width"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ", 50)
banner_text("When you're feeling in the dumps,", 50)
banner_text("Don't be silly chumps,", 50)
banner_text("Just purse your lips and whistle - that's the thing!", 50)
banner_text("And... always look on the bright side of life...", 50)
banner_text("*", 50)
