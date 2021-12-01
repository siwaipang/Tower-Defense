def drawLeftMenu():
    global img_exit, img_settings, img_rules
    img_exit = loadImage('exit.png')
    img_settings = loadImage('settings.png')
    img_rules = loadImage('rules.png')
    image(img_exit, 50, 50, 92, 101)
    image(img_settings, 167, 50, 92, 101)
    image(img_rules, 284, 50, 92, 101)
    
def drawNextButton():
    global img_btn_next
    img_btn_next = loadImage('btn_next.png')
    image(img_btn_next, 1666, 50, 204, 87)
    
def drawTroopsButton():
    global img_btn_troops
    img_btn_troops = loadImage('btn_troops.png')
    image(img_btn_troops, 58, 655, 204, 87)
