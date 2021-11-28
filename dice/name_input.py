# from dice import *
    
def setup():
    fullScreen()
    
    # create font
    global font_kabel
    font_kabel = loadFont('LeelawadeeUI-Bold-48.vlw')
    
    #loading image
    global img_logo, img_bg, img_round, img_exit, img_settings
    img_logo = loadImage('logo.png')
    img_bg = loadImage('background.png')
    img_round = loadImage('round.png')
    img_exit = loadImage('exit.png')
    img_settings = loadImage('settings.png')
    
    # input gamer names
    global gamer_names, allowed_characters, gamer_one, gamer_two, gamer_three, gamer_four
    gamer_one = ''
    gamer_two = ''
    gamer_three = ''
    gamer_four = ''
    gamer_names = [gamer_one, gamer_two, gamer_three, gamer_four]
    allowed_characters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
                          "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", \
                          "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

def drawBackground():
    global img_bg
    image(img_bg, 0, 0, width, height)
    
def drawLogo():
    global img_logo
    image(img_logo, width/3.7, 100)
    
def drawEnterNamesText():
    global font_kabel
    fill(255)
    textFont(font_kabel, 32)
    textAlign(CENTER)
    text('ENTER NAMES', width/2, 400)
    
def drawInputEnterNames():
    textAlign(LEFT)
    fill('#142438')
    stroke(255)
    rect(width/2.3, height/2.19, 400, 70)
    rect(width/2.3, height/1.89, 400, 70)
    rect(width/2.3, height/1.66, 400, 70)
    rect(width/2.3, height/1.48, 400, 70)
    fill(255)
    text('Player 1: \n\nPlayer 2: \n\nPlayer 3: \n\nPlayer 4: ', width/2.8, height/2)
    text(gamer_names[0], width/2.25, height/2.1, 400, 300)
    text(gamer_names[1], width/2.25, height/1.81, 400, 300)
    text(gamer_names[2], width/2.25, height/1.6, 400, 300)
    text(gamer_names[3], width/2.25, height/1.43, 400, 300)
    
def drawStartBtn():
    global img_round
    image(img_round, width/2.36, height/1.15, 290, 110)
    fill(255)
    textAlign(CENTER)
    text('START', width/2, height/1.08)
    
def drawLeftMenu():
    image(img_exit, 50, 50, 92, 101)
    image(img_settings, 167, 50, 92, 101)
    
def changeCursorToPointer():
    # when hovering over button, the cursor will change to a pointer
    if (mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151) or (mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151) or \
        (mouseX > 811 and mouseX < 1101 and mouseY > 936 and mouseY < 1046):
        cursor(HAND)
    else:
        cursor(ARROW)

def changeCursorToText():
    # when hovering over textfield, the cursor will change to a text cursor
    if (mouseX > 835 and mouseX < 1235 and mouseY > height/2.19 and mouseY < 560) or (mouseX > 835 and mouseX < 1235 and mouseY > height/1.89 and mouseY < 640) or \
        (mouseX > 835 and mouseX < 1235 and mouseY > height/1.66 and mouseY < 720) or (mouseX > 835 and mouseX < 1235 and mouseY > height/1.48 and mouseY < 800):
        cursor(TEXT)
    else:
        cursor(ARROW)
        
def drawPlayerList():
    # if player_list == 1:
    textAlign(LEFT)
    text('1. ' + gamer_names[0], width/1.5, height/2.4)
    text('2. ' + gamer_names[1], width/1.5, height/2.2)
    text('3. ' + gamer_names[2], width/1.5, height/2)
    text('4. ' + gamer_names[3], width/1.5, height/1.8)
    # else:
    #     fill('transparent')
    
    
def draw():
    drawBackground()
    drawLogo()
    changeCursorToPointer()
    changeCursorToText()
    drawEnterNamesText()
    drawInputEnterNames()
    drawStartBtn()
    drawLeftMenu()
    drawPlayerList()
    
    
def mousePressed():
    global player_list
    if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # exit button
        ### POPUP TOEVOEGEN??
        exit()
    if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # settings button
        fill(0)
        rect(167, 50, 92, 101)
    if mouseX > 811 and mouseX < 1101 and mouseY > 936 and mouseY < 1046: # start button
        fill(255)
        rect(811, 936, 290, 110)
    
     
def keyPressed():
    global gamer_names, allowed_characters
    # input names
    if mouseX > 835 and mouseX < 1235 and mouseY > height/2.19 and mouseY < 560: # player 1
        if len(gamer_names[0]) < 15:
            if key in allowed_characters:
                gamer_names[0] += key
            if key == ' ':
                gamer_names[0] += ' '
        if key == BACKSPACE:
            gamer_names[0] = gamer_names[0][:-1]
        if key == DELETE:
            gamer_names[0] = ''
            
    if mouseX > 835 and mouseX < 1235 and mouseY > height/1.89 and mouseY < 640: # player 2
        if len(gamer_names[1]) < 15:
            if key in allowed_characters:
                gamer_names[1] += key
            if key == ' ':
                gamer_names[1] += ' '
        if key == BACKSPACE:
            gamer_names[1] = gamer_names[1][:-1]
        if key == DELETE:
            gamer_names[1] = ''
            
    if mouseX > 835 and mouseX < 1235 and mouseY > height/1.66 and mouseY < 720: # player 3
        if len(gamer_names[2]) < 15:
            if key in allowed_characters:
                gamer_names[2] += key
            if key == ' ':
                gamer_names[2] += ' '
        if key == BACKSPACE:
            gamer_names[2] = gamer_names[2][:-1]
        if key == DELETE:
            gamer_names[2] = ''
        
    if mouseX > 835 and mouseX < 1235 and mouseY > height/1.48 and mouseY < 800: # player 4
        if len(gamer_names[3]) < 15:
            if key in allowed_characters:
                gamer_names[3] += key
            if key == ' ':
                gamer_names[3] += ' '
        if key == BACKSPACE:
            gamer_names[3] = gamer_names[3][:-1]
        if key == DELETE:
            gamer_names[3] = ''
            
