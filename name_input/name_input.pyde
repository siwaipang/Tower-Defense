from mainscreen import *
import random

currentScreen = 'NAME_INPUT'
current_round = 0
def setup():
    # size(1920, 1080)
    fullScreen()
    
    # create font
    global font_kabel
    font_kabel = loadFont('LeelawadeeUI-Bold-48.vlw')
    
    # create cursor
    global img_cursor
    img_cursor = loadImage('cursor.png')

    #loading image
    global img_logo, img_bg, img_round, img_exit
    img_logo = loadImage('logo.png')
    img_bg = loadImage('background.png')
    img_round = loadImage('round.png')
    img_exit = loadImage('exit.png')
    
    ## BUTTONS
    global img_btn_back, img_btn_cancel, img_btn_exit, img_btn_cards, img_settings, img_buttons
    img_btn_back = loadImage('btn_back.png')
    img_btn_cancel = loadImage('btn_cancel.png')
    img_btn_exit = loadImage('btn_exit.png')
    img_btn_cards = loadImage('btn_cards.png')
    img_settings = loadImage('settings.png')
    img_buttons = loadImage('btn_number.png')
    
    global img_btn_cardsmall, img_btn_number
    img_btn_cardsmall = loadImage('btn_cardsmall.png')
    img_btn_number = loadImage('btn_number.png')
    
    # input gamer names
    global gamer_names, allowed_characters
    gamer_one = ''
    gamer_two = ''
    gamer_three = ''
    gamer_four = ''
    gamer_names = [gamer_one, gamer_two, gamer_three, gamer_four]
    allowed_characters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
                          "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", \
                          "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    
    # create random number between 2 and 12
    global min_number, max_number, number
    min_number = 2
    max_number = 12
    number = random.randint(min_number, max_number)
    
    # loading dice images
    global img_dice
    img_dice_1 = loadImage('dices/dice_1.png')
    img_dice_2 = loadImage('dices/dice_2.png')
    img_dice_3 = loadImage('dices/dice_3.png')
    img_dice_4 = loadImage('dices/dice_4.png')
    img_dice_5 = loadImage('dices/dice_5.png')
    img_dice_6 = loadImage('dices/dice_6.png')
    img_dice = [img_dice_1, img_dice_2, img_dice_3, img_dice_4, img_dice_5, img_dice_6]

def drawBackground():
    global img_bg
    image(img_bg, 0, 0, width, height)
    
def drawLogo():
    global img_logo
    image(img_logo, width/3.7, 100, 900, 282)
    
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
    
def drawBackButton():
    image(img_btn_back, 1666, 50, 204, 87)
    
def drawExitButton():
    image(img_btn_exit, 725, 550, 204, 87)
    
def drawCancelButton():
    image(img_btn_cancel, 975, 550, 204, 87)
    
def drawRound(title):
    image(img_round, 793, 47)
    textFont(font_kabel, 32)
    textAlign(CENTER)
    fill('#1dc2ce')
    text(title, 938, 112)
    
def drawPlayerList():
    global gamer_names
    text('1. ' + gamer_names[0], width/2, height/2.1)
    text('2. ' + gamer_names[1], width/2, height/1.8)
    text('3. ' + gamer_names[2], width/2, height/1.57)
    text('4. ' + gamer_names[3], width/2, height/1.4)
    
def drawThrowDiceBtn():
    global img_round
    image(img_round, width/2.36, height/1.15, 290, 110)
    fill(255)
    textFont(font_kabel, 25)
    text('THROW DICE', width/2, height/1.08)
    
def changeCursor():
    global img_cursor
    cursor(img_cursor)
    
# displays the dice numbers when user throws the dice
def throwDice():
    global img_dice, number
    if number == 2:
        image(img_dice[0], width/3, height/2.2)
        image(img_dice[0], width/1.9, height/2.2)
    elif number == 3:
        image(img_dice[1], width/3, height/2.2)
        image(img_dice[0], width/1.9, height/2.2)
    elif number == 4:
        image(img_dice[1], width/3, height/2.2)
        image(img_dice[1], width/1.9, height/2.2)
    elif number == 5:
        image(img_dice[2], width/3, height/2.2)
        image(img_dice[1], width/1.9, height/2.2)
    elif number == 6:
        image(img_dice[2], width/3, height/2.2)
        image(img_dice[2], width/1.9, height/2.2)
    elif number == 7:
        image(img_dice[3], width/3, height/2.2)
        image(img_dice[2], width/1.9, height/2.2)
    elif number == 8:
        image(img_dice[3], width/3, height/2.2)
        image(img_dice[3], width/1.9, height/2.2)
    elif number == 9:
        image(img_dice[4], width/3, height/2.2)
        image(img_dice[3], width/1.9, height/2.2)
    elif number == 10:
        image(img_dice[4], width/3, height/2.2)
        image(img_dice[4], width/1.9, height/2.2)
    elif number == 11:
        image(img_dice[5], width/3, height/2.2)
        image(img_dice[4], width/1.9, height/2.2)
    elif number == 12:
        image(img_dice[5], width/3, height/2.2)
        image(img_dice[5], width/1.9, height/2.2)

def nextPlayer():
    global img_round
    image(img_round, width/2.36, height/1.15, 290, 110)
    fill(255)
    textAlign(CENTER)
    if current_round < 4:
        text('NEXT PLAYER', width/2, height/1.08)
    else:
        text('START GAME', width/2, height/1.08)
        
# displays the text: 'user throws number'
def playerThrowsNumber():
    global gamer_names, current_round, number
    if current_round == 0:
        text(gamer_names[0] + ' throws ' + str(number), width/2, height/2.5)
    elif current_round == 1:
        text(gamer_names[1] + ' throws ' + str(number), width/2, height/2.5)
    elif current_round == 2:
        text(gamer_names[2] + ' throws ' + str(number), width/2, height/2.5)
    elif current_round == 3:
        text(gamer_names[3] + ' throws ' + str(number), width/2, height/2.5)
    else:
        text('Please start game', width/2, height/2.5)
       
def draw():
    drawBackground()
    drawLogo()
    changeCursor()
    drawEnterNamesText()
    drawInputEnterNames()
    drawStartBtn()
    drawLeftMenu()
    
    if currentScreen == 'DICE':
        drawBackground()
        drawLogo()
        drawLeftMenu()
        drawPlayerList()
        drawThrowDiceBtn()
        drawBackButton()
        
    ## THROW DICES SCREEN
    elif currentScreen == 'THROW_DICES':
        drawBackground()
        drawLogo()
        drawLeftMenu()
        drawBackButton()
        fill('#1a2236')
        noStroke()
        rect(460, 390, 1000, 400, 10)
        textAlign(CENTER, CENTER)
        fill('#1dc2ce')
        playerThrowsNumber()
        throwDice()
        textFont(font_kabel, 25)
        nextPlayer()
        
    ## EXIT SCREEN
    elif currentScreen == 'EXIT':
        drawBackground()
        fill('#1a2236')
        noStroke()
        rect(460, 390, 1000, 300, 10)
        textAlign(CENTER, CENTER)
        fill('#1dc2ce')
        text('DO YOU WANT TO EXIT?', 960, 480)
        drawExitButton()
        drawCancelButton()
    
    ## SETTINGS SCREEN
    elif currentScreen == 'SETTINGS':
        drawBackground()
        drawLeftMenu()
        drawBackButton()
        drawRound('SETTINGS')
    
def mousePressed():            
    global player_list, currentScreen, number, current_round
    if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
        currentScreen = 'EXIT'
    if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
        currentScreen = 'SETTINGS'
    if currentScreen == 'NAME_INPUT':
        if mouseX > 811 and mouseX < 1101 and mouseY > 936 and mouseY < 1046: # START BUTTON
            currentScreen = 'DICE'
        
    ## DICE SCREEN
    elif currentScreen == 'DICE':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'NAME_INPUT'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
        if mouseX > 811 and mouseX < 1101 and mouseY > 936 and mouseY < 1046: # THROW_DICES BUTTON
            currentScreen = 'THROW_DICES'
            
    ## THROW DICES SCREEN
    elif currentScreen == 'THROW_DICES':
        if mouseX > 811 and mouseX < 1101 and mouseY > 936 and mouseY < 1046: # NEXT PLAYER
            current_round += 1
            if current_round < 4:
                number = random.randint(min_number, max_number)
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'DICE'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
            
    ## EXIT SCREEN
    elif currentScreen == 'EXIT':
        if mouseX > 725 and mouseX < 929 and mouseY > 550 and mouseY < 637: # EXIT BUTTON
            exit() 
        if mouseX > 975 and mouseX < 1179 and mouseY > 550 and mouseY < 637: # CANCEL BUTTON
            currentScreen = 'NAME_INPUT' 
            
    ## SETTINGS SCREEN
    elif currentScreen == 'SETTINGS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'NAME_INPUT'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
     
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
