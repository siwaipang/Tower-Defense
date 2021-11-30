from name_input import *

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
    
    # create player list
    global gamer_names
    gamer_names = ['Si Wai', 'Lucas', 'Sven', 'Anton']
    
def drawBackground():
    global img_bg
    image(img_bg, 0, 0, width, height)
    
def drawLogo():
    global img_logo
    image(img_logo, width/3.7, 100)
    
def drawEnterNames():
    global font_kabel
    fill(255)
    textFont(font_kabel, 32)
    textAlign(CENTER)
    text('ENTER NAMES', width/2, 400)
    
def drawStartBtn():
    global img_round
    image(img_round, width/2.36, height/1.15, 290, 110)
    fill(255)
    textFont(font_kabel, 25)
    text('THROW DICE', width/2, height/1.08)
    
def drawLeftMenu():
    image(img_exit, 50, 50, 92, 101)
    image(img_settings, 167, 50, 92, 101)
    
def changeCursorToPointer():
    if (mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151) or (mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151) or \
        (mouseX > 811 and mouseX < 1101 and mouseY > 936 and mouseY < 1046):
        cursor(HAND)
    else:
        cursor(ARROW)
        
def drawPlayerList():
    global gamer_names
    text('1. ' + gamer_names[0], width/2, height/2)
    text('2. ' + gamer_names[1], width/2, height/1.7)
    text('3. ' + gamer_names[2], width/2, height/1.47)
    text('4. ' + gamer_names[3], width/2, height/1.3)
    
def draw():
    drawBackground()
    drawLogo()
    changeCursorToPointer()
    drawEnterNames()
    drawPlayerList()
    drawStartBtn()
    drawLeftMenu()
    
def mousePressed():
    if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # exit button
        ### POPUP TOEVOEGEN??
        exit()
    if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # settings button
        fill(0)
        rect(167, 50, 92, 101)
    if mouseX > 811 and mouseX < 1101 and mouseY > 936 and mouseY < 1046: # throw dice option
        fill(0)
        rect(811, 936, 290, 110)
     
