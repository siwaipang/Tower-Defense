from mainscreen import *
from economy import *
from ui import *

import random

add_library("sound")

currentScreen = 'MAIN-MENU'
lastScreen = 'MAIN-MENU'
currentRound = 'POINTS'
currentPlayer = 0
activePlayers = []
enteredPlayers = 0
amountGained = 0

## INPUT NAMES AND DICE
shuffled = False
gamer_one = ''
gamer_two = ''
gamer_three = ''
gamer_four = ''
gamer_names = [gamer_one, gamer_two, gamer_three, gamer_four]

currentEntering = 1
current_round = 0

amountOne = 0
amountTwo = 0
thrownDice = False

diceGained = {
              1: {
                  'name': '',
                  'dice1': 0,
                  'dice2': 0,
                  'total': 0
                  },
              2: {
                  'name': '',
                  'dice1': 0,
                  'dice2': 0,
                  'total': 0
                  },
              3: {
                  'name': '',
                  'dice1': 0,
                  'dice2': 0,
                  'total': 0
                  },
              4: {
                  'name': '',
                  'dice1': 0,
                  'dice2': 0,
                  'total': 0
                  }
              }

tooltips = {'notEnoughPlayers': False}

players = {
               1: {
                   'name': '',
                   'health': 3,
                   'points': 30,
                   'cards': [],
                   'isDead': True
                   },
                2: {
                   'name': '',
                   'health': 3,
                   'points': 30,
                   'cards': [],
                   'isDead': True
                   },
                3: {
                   'name': '',
                   'health': 3,
                   'points': 30,
                   'cards': [],
                   'isDead': True
                   },
                4: {
                   'name': '',
                   'health': 3,
                   'points': 30,
                   'cards': [],
                   'isDead': True
                   }
               }
   
def setup():
    fullScreen()
    #size(1920,1080)
    
    ## SOUND
    sf = SoundFile(this,"themesong.mp3")
    sf.play()
    sf.amp(0.4)
    
    ## PLAYERCARDS
    global img_playercard, img_playercard_dead
    img_playercard = loadImage('playercard.png')
    img_playercard_dead = loadImage('playercard_dead.png')
    
    ## DICE
    global dice_1, dice_2, dice_3, dice_4, dice_5, dice_6
    dice_1 = loadImage('dice_1.png')
    dice_2 = loadImage('dice_2.png')
    dice_3 = loadImage('dice_3.png')
    dice_4 = loadImage('dice_4.png')
    dice_5 = loadImage('dice_5.png')
    dice_6 = loadImage('dice_6.png')
    
    ## CARDS
    global img_all_cards, img_btn_buy, img_btn_buy_small
    img_all_cards = loadImage('all_cards.png')
    img_btn_buy = loadImage('btn_buy.png')
    img_btn_buy_small = loadImage('btn_buy_small.png')
    
    img_card_counter = loadImage('card_counter.png')
    img_card_exchange = loadImage('card_exchange.png')
    img_card_exterminate = loadImage('card_exterminate.png')
    img_card_extramile = loadImage('card_extramile.png')
    img_card_ghost = loadImage('card_ghost.png')
    img_card_heal = loadImage('card_heal.png')
    img_card_kamikaze = loadImage('card_kamikaze.png')
    img_card_multihit = loadImage('card_multihit.png')
    img_card_mutiny = loadImage('card_mutiny.png')
    img_card_reach = loadImage('card_reach.png')
    img_card_refund = loadImage('card_refund.png')
    img_card_reversal = loadImage('card_reversal.png')
    img_card_shield = loadImage('card_shield.png')
    img_card_skip = loadImage('card_skip.png')
    img_card_switcheroo = loadImage('card_switcheroo.png')
    img_card_take = loadImage('card_take.png')
                
    global playingCards
    playingCards = {
             1: {
                 'img': img_card_counter,
                 'name': 'Counter',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             2: {
                 'img': img_card_exchange,
                 'name': 'Exchange',
                 'taken': False,
                 'drawn': 0,
                 'max': 3
                 },
             3: {
                 'img': img_card_exterminate,
                 'name': 'Exterminate',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             4: {
                 'img': img_card_extramile,
                 'name': 'Extra Mile',
                 'taken': False,
                 'drawn': 0,
                 'max': 2
                 },
             5: {
                 'img': img_card_ghost,
                 'name': 'Ghost',
                 'taken': False,
                 'drawn': 0,
                 'max': 3
                 },
             6: {
                 'img': img_card_heal,
                 'name': 'Heal',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             7: {
                 'img': img_card_kamikaze,
                 'name': 'Kamikaze',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             8: {
                 'img': img_card_multihit,
                 'name': 'Multi-Hit',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             9: {
                 'img': img_card_mutiny,
                 'name': 'Mutiny',
                 'taken': False,
                 'drawn': 0,
                 'max': 1
                 },
             10: {
                  'img': img_card_ghost,
                  'name': 'Reach',
                  'taken': False,
                  'drawn': 0,
                  'max': 2
                  },
             11: {
                  'img': img_card_refund,
                  'name': 'Refund',
                  'taken': False,
                  'drawn': 0,
                  'max': 2
                  },
             12: {
                  'img': img_card_reversal,
                  'name': 'Reversal',
                  'taken': False,
                  'drawn': 0,
                  'max': 2
                  },
             13: {
                  'img': img_card_shield,
                  'name': 'Shield',
                  'taken': False,
                  'drawn': 0,
                  'max': 1
                  },
             14: {
                  'img': img_card_skip,
                  'name': 'Skip',
                  'taken': False,
                  'drawn': 0,
                  'max': 2
                  },
             15: {
                  'img': img_card_switcheroo,
                  'name': 'Switcheroo',
                  'taken': False,
                  'drawn': 0,
                  'max': 1
                  },
             16: {
                  'img': img_card_take,
                  'name': 'Take',
                  'taken': False,
                  'drawn': 0,
                  'max': 1
                  },
             }
    
    ## FONT
    global font_kabel
    font_kabel = loadFont('LeelawadeeUI-Bold-48.vlw')
    
    ## CURSOR
    global img_cursor
    img_cursor = loadImage('cursor.png')
    
    ## BACKGROUND
    global img_bg, img_logo
    img_bg = loadImage('background.png')
    img_logo = loadImage('logo.png')
    
    ## CURRENT ROUND
    global img_round
    img_round = loadImage('round.png')
    
    ## LEFT MENU
    global img_exit, img_settings, img_rules
    img_exit = loadImage('exit.png')
    img_settings = loadImage('settings.png')
    img_rules = loadImage('rules.png')
    
    ## BUTTONS
    global img_btn_back, img_btn_cancel, img_btn_exit, img_btn_cards, img_btn_next, img_btn_shuffle, img_btn_roll
    img_btn_back = loadImage('btn_back.png')
    img_btn_cancel = loadImage('btn_cancel.png')
    img_btn_exit = loadImage('btn_exit.png')
    img_btn_cards = loadImage('btn_cards.png')
    img_btn_next = loadImage('btn_next.png')
    # img_btn_shuffle = loadImage('btn_shuffle.png')
    img_btn_shuffle = loadImage('btn_throw.png')
    img_btn_roll = loadImage('btn_roll_small.png')

    global img_btn_on, img_btn_off, img_btn_low, img_btn_medium, img_btn_high
    img_btn_on = loadImage('btn_on.png')
    img_btn_off = loadImage('btn_off.png')
    img_btn_low = loadImage('btn_low.png')
    img_btn_medium = loadImage('btn_medium.png')
    img_btn_high = loadImage('btn_high.png') 
    
    global img_btn_cardsmall, img_btn_number, img_btn_use
    img_btn_cardsmall = loadImage('btn_cardsmall.png')
    img_btn_number = loadImage('btn_number.png')
    img_btn_use = loadImage('btn_use.png')
    
    ### --- NAME INPUT --- ###
    # input gamer names
    global allowed_characters
    allowed_characters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", \
                          "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", \
                          "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    
    global dicePoints
    dicePoints = {
                  1: {
                      'amount': 1,
                      'img': dice_1
                      },
                  2: {
                      'amount': 2,
                      'img': dice_2
                      },
                  3: {
                      'amount': 3,
                      'img': dice_3
                      },
                  4: {
                      'amount': 4,
                      'img': dice_4
                      },
                  5: {
                      'amount': 5,
                      'img': dice_5
                      },
                  6: {
                      'amount': 6,
                      'img': dice_6 
                      }
            }
    
## --- MAIN SCREEN --- ##
def throwDicePoints():
    global amountGained, currentRound, amountOne, amountTwo, currentPlayer
    amountOne = random.randint(1,6)
    amountTwo = random.randint(1,6)
    amountGained = amountOne + amountTwo
    players[currentPlayer]['points'] += amountGained
    
def throwDiceSteps():
    global amountGained, currentRound, amountOne, amountTwo
    numbers = [1,2,2,3,3,4]
    index = random.randint(0,5)
    amountOne = numbers[index]
    amountGained = amountOne
    
def drawDiceAmount():
    global amountGained, currentRound, amountOne, amountTwo
    if amountGained != 0:
        if currentRound == 'POINTS':
            text(str(amountGained) + ' POINTS', 960, 709)
            image(dicePoints[amountOne]['img'], 677, 672)
            image(dicePoints[amountTwo]['img'], 735, 672)
        if currentRound == 'STEPS':
            text(str(amountGained) + ' STEPS', 960, 709)
            image(dicePoints[amountOne]['img'], 677, 672)
    
## --- SHUFFLE --- ##
def drawDiceShuffleAmount():
    global diceGained, shuffled, name1, gamerList
    
    ## DISPLAYING THROWN DICE
    if shuffled > 0:
        diceGained[1]['name'] = gamerList[0]
        if gamerList[0] == name1[0]:
            player1dice = diceGained[1]['dice1']
            player2dice = diceGained[1]['dice2']
            image(dicePoints[player1dice]['img'], 825, 463)
            image(dicePoints[player2dice]['img'], 885, 463)
        elif gamerList[1] == name1[0]:
            player3dice = diceGained[2]['dice1']
            player4dice = diceGained[2]['dice2']
            image(dicePoints[player3dice]['img'], 825, 463)
            image(dicePoints[player4dice]['img'], 885, 463)
        elif gamerList[2] == name1[0]:
            player5dice = diceGained[3]['dice1']
            player6dice = diceGained[3]['dice2']
            image(dicePoints[player5dice]['img'], 825, 463)
            image(dicePoints[player6dice]['img'], 885, 463)
        elif gamerList[3] == name1[0]:
            player7dice = diceGained[4]['dice1']
            player8dice = diceGained[4]['dice2']
            image(dicePoints[player7dice]['img'], 825, 463)
            image(dicePoints[player8dice]['img'], 885, 463)
        
    if shuffled > 1:
        diceGained[2]['name'] = gamerList[1]
        if gamerList[0] == name1[1]:
            player1dice = diceGained[1]['dice1']
            player2dice = diceGained[1]['dice2']
            image(dicePoints[player1dice]['img'], 825, 563)
            image(dicePoints[player2dice]['img'], 885, 563)
        elif gamerList[1] == name1[1]:
            player3dice = diceGained[2]['dice1']
            player4dice = diceGained[2]['dice2']
            image(dicePoints[player3dice]['img'], 825, 563)
            image(dicePoints[player4dice]['img'], 885, 563)
        elif gamerList[2] == name1[1]:
            player5dice = diceGained[3]['dice1']
            player6dice = diceGained[3]['dice2']
            image(dicePoints[player5dice]['img'], 825, 563)
            image(dicePoints[player6dice]['img'], 885, 563)
        elif gamerList[3] == name1[1]:
            player7dice = diceGained[4]['dice1']
            player8dice = diceGained[4]['dice2']
            image(dicePoints[player7dice]['img'], 825, 563)
            image(dicePoints[player8dice]['img'], 885, 563)
    
    if shuffled > 2:
        diceGained[3]['name'] = gamerList[2]
        if gamerList[0] == name1[2]:
            player1dice = diceGained[1]['dice1']
            player2dice = diceGained[1]['dice2']
            image(dicePoints[player1dice]['img'], 825, 663)
            image(dicePoints[player2dice]['img'], 885, 663)
        elif gamerList[1] == name1[2]:
            player3dice = diceGained[2]['dice1']
            player4dice = diceGained[2]['dice2']
            image(dicePoints[player3dice]['img'], 825, 663)
            image(dicePoints[player4dice]['img'], 885, 663)
        elif gamerList[2] == name1[2]:
            player5dice = diceGained[3]['dice1']
            player6dice = diceGained[3]['dice2']
            image(dicePoints[player5dice]['img'], 825, 663)
            image(dicePoints[player6dice]['img'], 885, 663)
        elif gamerList[3] == name1[2]:
            player7dice = diceGained[4]['dice1']
            player8dice = diceGained[4]['dice2']
            image(dicePoints[player7dice]['img'], 825, 663)
            image(dicePoints[player8dice]['img'], 885, 663)
    
    if shuffled > 3:
        diceGained[4]['name'] = gamerList[3]
        if gamerList[0] == name1[3]:
            player1dice = diceGained[1]['dice1']
            player2dice = diceGained[1]['dice2']
            image(dicePoints[player1dice]['img'], 825, 763)
            image(dicePoints[player2dice]['img'], 885, 763)
        elif gamerList[1] == name1[3]:
            player3dice = diceGained[2]['dice1']
            player4dice = diceGained[2]['dice2']
            image(dicePoints[player3dice]['img'], 825, 763)
            image(dicePoints[player4dice]['img'], 885, 763)
        elif gamerList[2] == name1[3]:
            player5dice = diceGained[3]['dice1']
            player6dice = diceGained[3]['dice2']
            image(dicePoints[player5dice]['img'], 825, 763)
            image(dicePoints[player6dice]['img'], 885, 763)
        elif gamerList[3] == name1[3]:
            player7dice = diceGained[4]['dice1']
            player8dice = diceGained[4]['dice2']
            image(dicePoints[player7dice]['img'], 825, 763)
            image(dicePoints[player8dice]['img'], 885, 763)
        
def drawDiceShuffle(n):
    global diceGained, playersAdded, gamer_names
    for i in range(1):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        diceGained[n]['dice1'] = dice1
        diceGained[n]['dice2'] = dice2
        diceGained[n]['total'] = dice1 + dice2
        diceGained[n]['name'] = gamer_names[shuffled - 1]
    return diceGained[n]['total']
        
def drawPlayerList():
    global diceGained, playersAdded, gamer_names, name1, playerList, gamerList, shuffled
    gamerList = []
    for i in range(len(gamer_names)):
        if gamer_names[i] != '':
            gamerList.append(gamer_names[i])
            
    playerList = {}
    shuffled = 0                         
    for player_name in gamerList:
        shuffled += 1
        playerRoll = drawDiceShuffle(shuffled)
        
        while playerRoll in playerList:
            playerRoll = drawDiceShuffle(shuffled)
        
        playerList[playerRoll] = player_name
        name1 = [playerList[roll] for roll in sorted(playerList.keys(), reverse=True)]
    return [playerList[roll] for roll in sorted(playerList.keys(), reverse=True)]

## --- CARDS SCREEN --- ##
def drawAllCards():
    image(img_all_cards, 50, 270)

def drawUseButton(x,y):
    image(img_btn_use, x, y, 204, 87)

def drawDiceBoxBottom():
    global currentPlayer
    fill('#1a2236')
    noStroke()
    rect(660, 950, 600, 78, 10)
    fill('#1dc2ce')
    textAlign(CENTER)
    textFont(font_kabel, 32)
    text(str(players[currentPlayer]['points']) + ' POINTS', 960, 1000)

def drawCardScreenBottom(player):
    global currentPlayer
    fill('#1a2236')
    noStroke()
    rect(660, 950, 600, 78, 10)
    fill('#1dc2ce')
    textAlign(CENTER)
    textFont(font_kabel, 32)
    text(str(players[player]['points']) + ' POINTS', 960, 1000)   

def drawCardsBuyButton():
    image(img_btn_buy_small, 1135, 966)
    
## --- PLAYING CARDS --- ##
def buyCard():
    bought = False
    while bought == False:
        num = random.randint(1, 16)
        if playingCards[num]['taken'] == False:
            cardName = playingCards[num]['name']
            players[currentPlayer]['cards'].append(cardName)
            bought = True
            playingCards[num]['drawn'] += 1
            if playingCards[num]['max'] == playingCards[num]['drawn']:
                playingCards[num]['taken'] = True
        
def drawCardPlayer(player):
    totalCards = len(players[player]['cards'])
    
    if totalCards > 0:
        card1 = players[player]['cards'][0]
        for i in range(1, 17):
            if playingCards[i]['name'] == card1:
                img1 = playingCards[i]['img']
    if totalCards > 1:
        card2 = players[player]['cards'][1]
        for i in range(1, 17):
            if playingCards[i]['name'] == card2:
                img2 = playingCards[i]['img']
    if totalCards > 2:
        card3 = players[player]['cards'][2]
        for i in range(1, 17):
            if playingCards[i]['name'] == card3:
                img3 = playingCards[i]['img']
           
    if totalCards > 2:
        image(img1, 465, 315)
        image(img2, 812, 315)
        image(img3, 1157, 315)
        drawUseButton(512, 760)
        drawUseButton(858, 760)
        drawUseButton(1205, 760)
    elif totalCards > 1:
        image(img1, 640, 315)
        image(img2, 985, 315)
        drawUseButton(685, 760)
        drawUseButton(1030, 760)
    elif totalCards > 0:
        image(img1, 812, 315)
        drawUseButton(858, 760)
        
        
## --- CARD FUNCTIONALITIES --- ##  
def checkCard(player, index):
    global amountGained, currentPlayer, currentRound, enteredPlayers, activePlayers
    specialCards = ['Heal', 'Extra Mile', 'Take', 'Exchange', 'Skip']
    
    if players[player]['cards'][index] == 'Heal' and players[player]['health'] != 3:
        healCard(player)
        del players[player]['cards'][index]
    elif players[player]['cards'][index] == 'Extra Mile' and currentRound == 'STEPS':
        amountGained+=1
        del players[player]['cards'][index]
    elif players[player]['cards'][index] == 'Take':
        logCards = len(players[player]['cards'])
        takeCard(player)
        del players[player]['cards'][index]
        if len(players[player]['cards']) < logCards:
            players[player]['cards'].append('Take')
    elif players[player]['cards'][index] == 'Skip':
        del players[player]['cards'][index]
        if players[currentPlayer+1]['isDead'] == True:
            currentPlayer+=3
        else:
            currentPlayer +=2
        if currentPlayer > activePlayers[-1]:
                    if currentRound == 'POINTS':
                        currentRound = 'STEPS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                    else:
                        currentRound = 'POINTS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                            
        if players[currentPlayer]['isDead'] == True:
            for i in range(0, enteredPlayers):
                if currentPlayer + i > enteredPlayers:
                    currentPlayer = 0
                if players[currentPlayer + i]['isDead'] == False and currentPlayer + i <= enteredPlayers:
                    currentPlayer = currentPlayer + i
                    break
            
    elif players[player]['cards'][index] not in specialCards:
        del players[player]['cards'][index]
            
def takeCard(player):
    totalCards = len(players[player]['cards'])
    found = 0
    
    
    if totalCards < 3:
        for i in range(0, len(activePlayers)):
            if activePlayers[i] != player:
                found = activePlayers[i]
                break
             
        if found != 0:
            stealable = len(players[found]['cards'])
            if stealable != 0:
                card = random.randint(1, stealable)    
                players[player]['cards'].append(players[found]['cards'][card-1])
                del players[found]['cards'][card-1]
        
def healCard(player):
    players[player]['health']+=1

## --- INPUT SCREEN --- ##
def addPlayers():
    global gamer_names, players, activePlayers, enteredPlayers, diceGained
    adding = 1
    
    for i in range(0, len(gamer_names)):
        if gamer_names[i] != '':
            players[adding]['name'] = gamer_names[i]
            players[adding]['isDead'] = False
            enteredPlayers+=1
            activePlayers.append(adding)
            adding+=1

def drawTooltip(title, message):
    fill('#131a2a')
    noStroke()
    rect(460, 210, 1000, 200, 10)
    textAlign(CENTER, CENTER)
    textFont(font_kabel, 32)
    text(message, 960, 335)

def drawInputEnterNames():
    global playerList, currentScreen
    ### 1
    if currentEntering == 1:
        fill('#212b44')
    else:
        fill('#1a2236')
    noStroke()
    rect(460, 450, 300, 75, 10)
    rect(810, 450, 650, 75, 10)
    textAlign(CENTER, CENTER)
    if currentEntering == 1:
        fill('#1dc2ce')
    else:
        fill('#939393')
    textFont(font_kabel, 32)
    text('PLAYER1', 612, 487.5)
    if not len(gamer_names) < 1:
        text(gamer_names[0], 1115, 487.5)
    
    ## 2
    if currentEntering == 2:
        fill('#212b44')
    else:
        fill('#1a2236')
    noStroke()
    rect(460, 550, 300, 75, 10)
    rect(810, 550, 650, 75, 10)
    textAlign(CENTER, CENTER)
    if currentEntering == 2:
        fill('#1dc2ce')
    else:
        fill('#939393')
    textFont(font_kabel, 32)
    text('PLAYER2', 612, 587.5)
    if not len(gamer_names) < 2:
        text(gamer_names[1], 1115, 587.5)
    
    ## 3
    if currentEntering == 3:
        fill('#212b44')
    else:
        fill('#1a2236')
    noStroke()
    rect(460, 650, 300, 75, 10)
    rect(810, 650, 650, 75, 10)
    textAlign(CENTER, CENTER)
    if currentEntering == 3:
        fill('#1dc2ce')
    else:
        fill('#939393')
    textFont(font_kabel, 32)
    text('PLAYER3', 612, 687.5) 
    if not len(gamer_names) < 3:
        text(gamer_names[2], 1115, 687.5)
    
    ## 4
    if currentEntering == 4:
        fill('#212b44')
    else:
        fill('#1a2236')
    noStroke()
    rect(460, 750, 300, 75, 10)
    rect(810, 750, 650, 75, 10)
    textAlign(CENTER, CENTER)
    if currentEntering == 4:
        fill('#1dc2ce')
    else:
        fill('#939393')
    textFont(font_kabel, 32)
    text('PLAYER4', 612, 787.5) 
    if not len(gamer_names) < 4:
        text(gamer_names[3], 1115, 787.5)
        
def changeCursor():
    global img_cursor
    cursor(img_cursor)
    
def drawPlayerCards():
    if players[1]['isDead'] == False:
        image(img_playercard, 50, 770)
        if currentPlayer == 1:
            drawCurrentPlayer(62, 1042)
    elif players[1]['isDead'] == True:
        image(img_playercard_dead, 50, 770)
        
    if players[2]['isDead'] == False:
        image(img_playercard, 50 + 430 + 30, 770)
        if currentPlayer == 2:
            drawCurrentPlayer(521, 1042)
    elif players[2]['isDead'] == True:
        image(img_playercard_dead, 50 + 430 + 30, 770)
        
    if players[3]['isDead'] == False:
        image(img_playercard, 50 + 430*2 + 30*2, 770)
        if currentPlayer == 3:
            drawCurrentPlayer(983, 1042)
    elif players[3]['isDead'] == True:
        image(img_playercard_dead, 50 + 430*2 + 30*2, 770)
        
    if players[4]['isDead'] == False:
        image(img_playercard, 50 + 430*3 + 30*3, 770)
        if currentPlayer == 4:
            drawCurrentPlayer(1445, 1042)
    elif players[4]['isDead'] == True:
        image(img_playercard_dead, 50 + 430*3 + 30*3, 770)
    
def drawCurrentPlayer(x,y):
    fill('#1dc2ce')
    noStroke()
    rect(x, y, 409, 10, 10)
    
def drawRound(title):
    image(img_round, 815, 47)
    textFont(font_kabel, 32)
    textAlign(CENTER)
    fill('#1dc2ce')
    text(title, 960, 112)
    
def drawBackground():
    image(img_bg, 0, 0, width, height)
    
def drawCardsButton():
    image(img_btn_cards, 1649, 655, 204, 87)    
    
def drawCardsButtonSmall(x, y):
    image(img_btn_cardsmall, x, y)    
    
def drawNextButton():
    image(img_btn_next, 1666, 50, 204, 87)
    
def drawNextButtonBottom():
    image(img_btn_next, 1260, 875, 204, 87)

def drawShuffleButton():
    image(img_btn_shuffle, 460, 875, 204, 87)

def drawBackButton():
    image(img_btn_back, 1666, 50, 204, 87)
    
def drawBackButtonLeft():
    image(img_btn_back, 50, 50, 204, 87)
    
def drawLogo():
    image(img_logo, 542, 150)

def drawExitButton():
    image(img_btn_exit, 725, 550, 204, 87)

def drawCancelButton():
    image(img_btn_cancel, 975, 550, 204, 87)
    
def drawNumberBackground(x, y):
    image(img_btn_number, x, y)

def drawPlayerStats():
    textAlign(LEFT)
    textFont(font_kabel, 32)
    fill('#1dc2ce')
    
    if bool(players[1]['name']) != False and players[1]['isDead'] == False:
        text(players[1]['name'], 110, 830)
        textSize(24)
        text('Points:', 110, 880)
        drawNumberBackground(325, 850)
        fill('#9d9ebf')
        textAlign(CENTER)
        text(players[1]['points'], 377, 880)
        fill('#1dc2ce')
        drawNumberBackground(325, 900)
        fill('#9d9ebf')
        textAlign(LEFT)
        text(players[1]['health'], 370, 930)
        text('-', 340, 930)
        text('+', 400, 930)
        fill('#1dc2ce')
        text('Health:', 110, 930)
        drawCardsButtonSmall(325, 955)      
        
    if bool(players[2]['name']) != False and players[2]['isDead'] == False:
        textSize(32)
        text(players[2]['name'], 570, 830)
        textSize(24)
        text('Points:', 570, 880)
        drawNumberBackground(785, 850)
        fill('#9d9ebf')
        textAlign(CENTER)
        text(players[2]['points'], 837, 880)
        fill('#1dc2ce')
        drawNumberBackground(785, 900)
        fill('#9d9ebf')
        textAlign(LEFT)
        text(players[2]['health'], 830, 930)
        text('-', 800, 930)
        text('+', 860, 930)
        fill('#1dc2ce')
        text('Health:', 570, 930)
        drawCardsButtonSmall(785, 955) 
        
    if bool(players[3]['name']) != False and players[3]['isDead'] == False:
        textSize(32)
        text(players[3]['name'], 1035, 830)
        textSize(24)
        text('Points:', 1035, 880)
        drawNumberBackground(1245, 850)
        fill('#9d9ebf')
        textAlign(CENTER)
        text(players[3]['points'], 1296, 880)
        fill('#1dc2ce')
        drawNumberBackground(1245, 900)
        fill('#9d9ebf')
        textAlign(LEFT)
        text(players[3]['health'], 1291, 930)
        text('-', 1260, 930)
        text('+', 1320, 930)
        fill('#1dc2ce')
        text('Health:', 1035, 930)
        drawCardsButtonSmall(1245, 955) 
        
    if bool(players[4]['name']) != False and players[4]['isDead'] == False:
        textSize(32)
        text(players[4]['name'], 1495, 830)
        textSize(24)
        text('Points:', 1495, 880)
        drawNumberBackground(1705, 850)
        fill('#9d9ebf')
        textAlign(CENTER)
        text(players[4]['points'], 1754, 880)
        fill('#1dc2ce')
        drawNumberBackground(1705, 900)
        fill('#9d9ebf')
        textAlign(LEFT)
        text(players[4]['health'], 1750, 930)
        text('-', 1720, 930)
        text('+', 1780, 930)
        fill('#1dc2ce')
        text('Health:', 1495, 930)
        drawCardsButtonSmall(1705, 955) 
    
def drawMusic():
    fill('#1a2236')
    noStroke()
    rect(460, 450, 300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('MUSIC', 612, 487.5)
    
def drawVolume():
    fill('#1a2236')
    noStroke()
    rect(460, 550, 300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('VOLUME', 612, 587.5)

def drawNotifications():
    fill('#1a2236')
    noStroke()
    rect(460, 650, 300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('NOTIFICATIONS', 612, 687.5)
    
def drawSoundEffects():
    fill('#1a2236')
    noStroke()
    rect(460, 750, 300, 75, 10)
    textAlign(CENTER, CENTER)
    fill('#1dc2ce')
    textFont(font_kabel, 32)
    text('SOUNDEFFECTS', 612, 787.5)        
            
def drawSoundButtons():     
    image(img_btn_on, 950, 450, 204, 87)
    image(img_btn_off, 1200, 450, 204, 87)
    image(img_btn_low, 950, 550, 204, 87)
    image(img_btn_medium, 1200, 550, 204, 87)
    image(img_btn_high, 1450, 550, 204, 87)    
    image(img_btn_on, 950, 650, 204, 87)
    image(img_btn_off, 1200, 650, 204, 87)    
    image(img_btn_on, 950, 750, 204, 87)
    image(img_btn_off, 1200, 750, 204, 87)
    
def drawStartMenu():
    image(img_round, 630, 535)
    image(img_round, 1020, 535)
    image(img_round, 630, 710)
    image(img_round, 1020, 710)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(32)
    textAlign(CENTER)
    text("PLAY", 772, 600)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(32)
    textAlign(CENTER)
    text("SETTINGS", 1165, 600)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(32)
    textAlign(CENTER)
    text("CREDITS", 772, 775)
    
    textFont(font_kabel)
    fill('#1dc2ce')
    textSize(32)
    textAlign(CENTER)
    text("CONTACT", 1165, 775)
    
    fill(255)
    textSize(24)
    textAlign(LEFT)
    text('VERSION 0.0', 20, 1060)

## BUTTONS
def mousePressed():
    
    ## GLOBALS
    global currentRound, currentScreen, currentPlayer, activePlayers, enteredPlayers, currentEntering
    global player_list, currentScreen, number, current_round, lastScreen, gamer_names, shuffled, tooltips, thrownDice, amountGained, playersAdded
    
    ## MAIN MENU
    if currentScreen == 'MAIN-MENU':
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 630 and mouseX < 920 and mouseY > 535 and mouseY < 651:
            currentScreen = 'INPUT-NAMES'
            lastScreen = 'MAIN-MENU'
        if mouseX > 1020 and mouseX < 1310 and mouseY > 535 and mouseY < 651:
            currentScreen = 'SETTINGS'
            lastScreen = 'MAIN-MENU'
        if mouseX > 630 and mouseX < 920 and mouseY > 710 and mouseY < 826:
            currentScreen = 'CREDITS'
            lastScreen = 'MAIN-MENU'
        if mouseX > 1020 and mouseX < 1310 and mouseY > 710 and mouseY < 826:
            currentScreen = 'CONTACT'
            lastScreen = 'MAIN-MENU'
            
    playersAdded = 0
    for i in range(0, len(gamer_names)):
        if gamer_names[i] != '':
            playersAdded+=1
    
    ## INPUT NAMES
    if currentScreen == 'INPUT-NAMES':
        tooltips['notEnoughPlayers'] = False
        if mouseX > 50 and mouseX < 254 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN-MENU'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137 and playersAdded >= 2: # NEXT BUTTON
            currentScreen = 'SHUFFLE'
            currentEntering = 0
            lastScreen = 'INPUT-NAMES'
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137 and playersAdded < 2:
            tooltips['notEnoughPlayers'] = True
        
        if mouseX > 810 and mouseX < 1460 and mouseY > 450 and mouseY < 525:
            currentEntering = 1 
        if mouseX > 810 and mouseX < 1460 and mouseY > 550 and mouseY < 625:
            currentEntering = 2
        if mouseX > 810 and mouseX < 1460 and mouseY > 650 and mouseY < 725:
            currentEntering = 3
        if mouseX > 810 and mouseX < 1460 and mouseY > 750 and mouseY < 825:
            currentEntering = 4
    
    if currentScreen == 'CONTACT':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = lastScreen
        
    if currentScreen == 'CREDITS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = lastScreen
            
    ## SHUFFLE
    if currentScreen == 'SHUFFLE':
        if mouseX > 50 and mouseX < 254 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'INPUT-NAMES'
            ## SHUFFLE
        if currentScreen == 'SHUFFLE':
            if mouseX > 50 and mouseX < 254 and mouseY > 50 and mouseY < 137 and shuffled == False: # BACK BUTTON
                currentScreen = 'INPUT-NAMES'
            if mouseX > 460 and mouseX < 664 and mouseY > 875 and mouseY < 962: # SHUFFLE BUTTON
                shuffled = True
                gamer_names = drawPlayerList()
                # drawDiceShuffle()
            if mouseX > 1260 and mouseX < 1464 and mouseY > 875 and mouseY < 962: # NEXT BUTTON
                addPlayers()
                currentScreen = 'MAIN' 
                lastScreen = 'MAIN'
                currentPlayer = 1
    
    ## MAIN SCREEN
    if currentScreen == 'MAIN':
        if mouseX > 1130 and mouseX < 1232 and mouseY > 675 and mouseY < 719:
            if currentRound == 'POINTS' and thrownDice == False:
                throwDicePoints()
                thrownDice = True
            if currentRound == 'STEPS' and thrownDice == False:
                throwDiceSteps()
                thrownDice = True
        
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137 and thrownDice == True: # NEXT BUTTON
            if players[currentPlayer]['points'] > 10:
                players[currentPlayer]['points'] = 10
            
            thrownDice = False
            amountGained = 0
            currentPlayer +=1
            
            if currentPlayer > activePlayers[-1]:
                    if currentRound == 'POINTS':
                        currentRound = 'STEPS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                    else:
                        currentRound = 'POINTS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                            
            if players[currentPlayer]['isDead'] == True:
                for i in range(0, enteredPlayers):
                    if currentPlayer + i > enteredPlayers:
                        currentPlayer = 0
                    if players[currentPlayer + i]['isDead'] == False and currentPlayer + i <= enteredPlayers:
                        currentPlayer = currentPlayer + i
                        break
                
        if mouseX > 58 and mouseX < 262 and mouseY > 655 and mouseY < 742 and currentRound == 'POINTS': # TROOPS BUTTON
            currentScreen = 'TROOPS'
        if mouseX > 1649 and mouseX < 1853 and mouseY > 655 and mouseY < 742: # CARDS BUTTON
            currentScreen = 'CARDS'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
        if mouseX > 325 and mouseX < 427 and mouseY > 955 and mouseY < 999: # PLAYER 1 CARDS BUTTON
            currentScreen = 'PLAYER 1 CARDS'
        
        if mouseX > 785 and mouseX < 887 and mouseY > 955 and mouseY < 999: # PLAYER 2 CARDS BUTTON
            currentScreen = 'PLAYER 2 CARDS'
        
        if mouseX > 1245 and mouseX < 1348 and mouseY > 955 and mouseY < 999: # PLAYER 3 CARDS BUTTON
            currentScreen = 'PLAYER 3 CARDS'
        
        if mouseX > 1705 and mouseX < 1807 and mouseY > 955 and mouseY < 999: # PLAYER 4 CARDS BUTTON
            currentScreen = 'PLAYER 4 CARDS'
       
        if mouseX > 336 and mouseX < 351 and mouseY > 915 and mouseY < 930: # PLAYER 1 MINUS BUTTON
            currentHealth = players[1]['health']
            if players[1]['health'] != 0:
                players[1]['health']-= 1
            if currentHealth - 1 == 0:
                players[1]['isDead'] = True
                index = activePlayers.index(1)
                del activePlayers[index]
            
                if currentPlayer + 1 > activePlayers[-1]:
                    if currentRound == 'POINTS':
                        currentRound = 'STEPS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                            else:
                                currentRound = 'POINTS'
                                currentPlayer = 1
                                for i in range (0, enteredPlayers):
                                    if players[i+1]['isDead'] == False:
                                        currentPlayer = i + 1
                                        break
                            
                for i in range(0, enteredPlayers):
                    if currentPlayer + i > len(activePlayers):
                        currentPlayer = 0
                    if players[currentPlayer + i]['isDead'] == False and currentPlayer + i <= enteredPlayers:
                        currentPlayer = currentPlayer + i
                        break
        
        if mouseX > 400 and mouseX < 415 and mouseY > 915 and mouseY < 930: # PLAYER 1 PLUS BUTTON
            if players[1]['health'] != 3:
                players[1]['health']+= 1
        
        if mouseX > 796 and mouseX < 811 and mouseY > 915 and mouseY < 930: # PLAYER 2 MINUS BUTTON
            currentHealth = players[2]['health']
            if players[2]['health'] != 0:
                players[2]['health']-= 1
            if currentHealth - 1 == 0:
                players[2]['isDead'] = True
                index = activePlayers.index(2)
                del activePlayers[index]
                if currentPlayer + 1 > activePlayers[-1]:
                    if currentRound == 'POINTS':
                        currentRound = 'STEPS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                            else:
                                currentRound = 'POINTS'
                                currentPlayer = 1
                                for i in range (0, enteredPlayers):
                                    if players[i+1]['isDead'] == False:
                                        currentPlayer = i + 1
                                        break
                            
                for i in range(0, enteredPlayers):
                    if currentPlayer + i > enteredPlayers:
                        currentPlayer = 0
                    if players[currentPlayer + i]['isDead'] == False and currentPlayer + i <= enteredPlayers:
                        currentPlayer = currentPlayer + i
                        break
        
        if mouseX > 860 and mouseX < 875 and mouseY > 915 and mouseY < 930: # PLAYER 2 PLUS BUTTON
            if players[2]['health'] != 3:
                players[2]['health']+= 1
        
        if mouseX > 1256 and mouseX < 1271 and mouseY > 915 and mouseY < 930: # PLAYER 3 MINUS BUTTON
            currentHealth = players[3]['health']
            if players[3]['health'] != 0:
                players[3]['health']-= 1
            if currentHealth - 1 == 0:
                players[3]['isDead'] = True
                index = activePlayers.index(3)
                del activePlayers[index]
                if currentPlayer + 1 > activePlayers[-1]:
                    if currentRound == 'POINTS':
                        currentRound = 'STEPS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                            else:
                                currentRound = 'POINTS'
                                currentPlayer = 1
                                for i in range (0, enteredPlayers):
                                    if players[i+1]['isDead'] == False:
                                        currentPlayer = i + 1
                                        break
                            
                for i in range(0, enteredPlayers):
                    if currentPlayer + i > enteredPlayers:
                        currentPlayer = 0
                    if players[currentPlayer + i]['isDead'] == False and currentPlayer + i <= enteredPlayers:
                        currentPlayer = currentPlayer + i
                        break
        
        if mouseX > 1320 and mouseX < 1335 and mouseY > 915 and mouseY < 930: # PLAYER 3 PLUS BUTTON
            if players[3]['health'] != 3:
                players[3]['health']+= 1
        
        if mouseX > 1716 and mouseX < 1731 and mouseY > 915 and mouseY < 930: # PLAYER 4 MINUS BUTTON
            currentHealth = players[4]['health']
            if players[4]['health'] != 0:
                players[4]['health']-= 1
            if currentHealth - 1 == 0:
                players[4]['isDead'] = True
                index = activePlayers.index(4)
                del activePlayers[index]
                if currentPlayer + 1 > activePlayers[-1]:
                    if currentRound == 'POINTS':
                        currentRound = 'STEPS'
                        currentPlayer = 1
                        for i in range (0, enteredPlayers):
                            if players[i+1]['isDead'] == False:
                                currentPlayer = i + 1
                                break
                            else:
                                currentRound = 'POINTS'
                                currentPlayer = 1
                                for i in range (0, enteredPlayers):
                                    if players[i+1]['isDead'] == False:
                                        currentPlayer = i + 1
                                        break
                            
                for i in range(0, enteredPlayers):
                    if currentPlayer + i > enteredPlayers:
                        currentPlayer = 0
                    if players[currentPlayer + i]['isDead'] == False and currentPlayer + i <= enteredPlayers:
                        currentPlayer = currentPlayer + i
                        break
        
        if mouseX > 1780 and mouseX < 1795 and mouseY > 915 and mouseY < 930: # PLAYER 4 PLUS BUTTON
            if players[4]['health'] != 3:
                players[4]['health']+= 1
            
    ## TROOP SCREEN
    elif currentScreen == 'TROOPS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
    ## CARDS SCREEN
    elif currentScreen == 'CARDS':
        if mouseX > 1135 and mouseX < 1237 and mouseY > 966 and mouseY < 1010: # BUY BUTTON
            if players[currentPlayer]['points'] >= 10 and len(players[currentPlayer]['cards']) < 3:
                players[currentPlayer]['points'] -= 10
                buyCard()
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
    ## EXIT SCREEN
    elif currentScreen == 'EXIT':
        if mouseX > 725 and mouseX < 929 and mouseY > 550 and mouseY < 637: # EXIT BUTTON
            exit() 
        if mouseX > 975 and mouseX < 1179 and mouseY > 550 and mouseY < 637: # CANCEL BUTTON
            currentScreen = lastScreen 
    
    ## SETTINGS SCREEN
    elif currentScreen == 'SETTINGS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = lastScreen
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
    ## RULES SCREEN
    elif currentScreen == 'RULES':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
    ## PLAYER 1 CARDS SCREEN
    elif currentScreen == 'PLAYER 1 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
        
        totalCards1 = len(players[1]['cards'])    
        if totalCards1 > 2:
            if mouseX > 512 and mouseX < 716 and mouseY > 760 and mouseY < 847:
                checkCard(1,0)
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                checkCard(1,1)
            if mouseX > 1205 and mouseX < 1409 and mouseY > 760 and mouseY < 847:
                checkCard(1,2)
        
        elif totalCards1 > 1:
            if mouseX > 685 and mouseX < 889 and mouseY > 760 and mouseY < 847:
                checkCard(1,0)
            if mouseX > 1030 and mouseX < 1234 and mouseY > 760 and mouseY < 847:
                checkCard(1,1)
        
        elif totalCards1 > 0:
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                checkCard(1,0)
                 
    ## PLAYER 2 CARDS SCREEN
    elif currentScreen == 'PLAYER 2 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
        totalCards2 = len(players[2]['cards'])    
        if totalCards2 > 2:
            if mouseX > 512 and mouseX < 716 and mouseY > 760 and mouseY < 847:
                checkCard(2,0)
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                checkCard(2,1)
            if mouseX > 1205 and mouseX < 1409 and mouseY > 760 and mouseY < 847:
                checkCard(2,2)
        
        elif totalCards2 > 1:
            if mouseX > 685 and mouseX < 889 and mouseY > 760 and mouseY < 847:
                checkCard(2,0)
            if mouseX > 1030 and mouseX < 1234 and mouseY > 760 and mouseY < 847:
                checkCard(2,1)
        
        elif totalCards2 > 0:
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                checkCard(2,0)
    
    ## PLAYER 3 CARDS SCREEN
    elif currentScreen == 'PLAYER 3 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
        totalCards3 = len(players[3]['cards'])    
        if totalCards3 > 2:
            if mouseX > 512 and mouseX < 716 and mouseY > 760 and mouseY < 847:
                checkCard(3,0)
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                checkCard(3,1)
            if mouseX > 1205 and mouseX < 1409 and mouseY > 760 and mouseY < 847:
                checkCard(3,2)
        
        elif totalCards3 > 1:
            if mouseX > 685 and mouseX < 889 and mouseY > 760 and mouseY < 847:
                checkCard(3,0)
            if mouseX > 1030 and mouseX < 1234 and mouseY > 760 and mouseY < 847:
                checkCard(3,1)
        
        elif totalCards3 > 0:
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                checkCard(3,0)
    
    ## PLAYER 4 CARDS SCREEN
    elif currentScreen == 'PLAYER 4 CARDS':
        if mouseX > 1666 and mouseX < 1870 and mouseY > 50 and mouseY < 137: # BACK BUTTON
            currentScreen = 'MAIN'
        if mouseX > 50 and mouseX < 142 and mouseY > 50 and mouseY < 151: # EXIT BUTTON
            currentScreen = 'EXIT'
        if mouseX > 167 and mouseX < 259 and mouseY > 50 and mouseY < 151: # SETTINGS BUTTON
            currentScreen = 'SETTINGS'
        if mouseX > 284 and mouseX < 376 and mouseY > 50 and mouseY < 151: # RULES BUTTON
            currentScreen = 'RULES'
            
        totalCards4 = len(players[4]['cards'])    
        if totalCards4 > 2:
            if mouseX > 512 and mouseX < 716 and mouseY > 760 and mouseY < 847:
                checkCard(4,0)
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                checkCard(4,1)
            if mouseX > 1205 and mouseX < 1409 and mouseY > 760 and mouseY < 847:
                checkCard(4,2)
        
        elif totalCards4 > 1:
            if mouseX > 685 and mouseX < 889 and mouseY > 760 and mouseY < 847:
                checkCard(4,0)
            if mouseX > 1030 and mouseX < 1234 and mouseY > 760 and mouseY < 847:
                checkCard(4,1)
        
        elif totalCards4 > 0:
            if mouseX > 858 and mouseX < 1062 and mouseY > 760 and mouseY < 847:
                checkCard(4,0)
            
def keyPressed():
    global gamer_names, allowed_characters, currentScreen, currentEntering
    # input names
    if currentScreen == 'INPUT-NAMES':
        if key == TAB:
            if currentEntering == 4:
                currentEntering = 1
            else:
                currentEntering+=1
                
        if key == ENTER:
            if currentEntering == 4:
                currentEntering = 1
            else:
                currentEntering+=1
        
        if len(gamer_names[currentEntering-1]) < 15:
            if key in allowed_characters:
                gamer_names[currentEntering-1] += key
            if key == ' ':
                gamer_names[currentEntering-1] += ' '
        if key == BACKSPACE:
            gamer_names[currentEntering-1] = gamer_names[currentEntering-1][:-1]
        if key == DELETE:
            gamer_names[currentEntering-1] = ''           
      
## DRAW SCREENS
def draw():
    global img_cursor, img_btn_roll
    
    ## GLOBALS
    global currentRound, currentScreen, currentPlayer, activePlayers, shuffled, tooltips, font_kabel, shuffled, diceGained
    
    if currentScreen == 'MAIN-MENU':
        lastScreen = 'MAIN-MENU'
        drawBackground()
        drawLogo()
        drawStartMenu()
        drawExit()
    
    ## INPUT NAMES
    if currentScreen == 'INPUT-NAMES':
        drawBackground()
        drawRound('NAMES')
        drawNextButton()
        drawBackButtonLeft()
        drawInputEnterNames()
        
        fill('#1a2236')
        noStroke()
        rect(460, 300, 1000, 100, 10)
        textAlign(CENTER, CENTER)
        fill('#1dc2ce')
        textFont(font_kabel, 32)
        text('PLEASE ENTER YOUR NAMES', 960, 350)
        
        if tooltips['notEnoughPlayers'] == True:
            drawTooltip('NOT ENOUGH PLAYERS', 'YOU NEED ATLEAST 2 PLAYERS TO START THE GAME\nPLEASE ENTER MORE NAMES')
            
        
    if currentScreen == 'SHUFFLE':
        drawBackground()
        drawRound('SHUFFLE')
        if shuffled == False:
            drawBackButtonLeft()
            drawShuffleButton()
        else:
            drawNextButtonBottom()
        drawInputEnterNames()
        drawDiceShuffleAmount()
        
        fill('#1a2236')
        noStroke()
        rect(460, 300, 1000, 100, 10)
        textAlign(CENTER, CENTER)
        fill('#1dc2ce')
        textFont(font_kabel, 32)
        text('THROW DICE TO DECIDE WHO GOES FIRST', 960, 350)
    
    ## MAIN SCREEN
    if currentScreen == 'MAIN':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawPlayerCards()
        drawPlayerStats()
        drawNextButton()
        drawCardsButton()
        drawRound(currentRound)
        drawDiceBox(amountGained, currentRound, img_btn_roll, font_kabel)
        drawDiceAmount()
        if currentRound == 'POINTS':
            drawTroopsButton()
            
    ## TROOPS SCREEN
    elif currentScreen == 'TROOPS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawRound(currentRound)
        drawBackButton()
    
    ## CARDS SCREEN
    elif currentScreen == 'CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawRound(currentRound)
        drawBackButton()
        drawDiceBoxBottom()
        drawAllCards()
        drawCardsBuyButton()
    
    ## EXIT SCREEN
    elif currentScreen == 'EXIT':
        drawBackground()
        fill('#1a2236')
        noStroke()
        rect(460, 390, 1000, 300, 10)
        textAlign(CENTER, CENTER)
        fill('#1dc2ce')
        textFont(font_kabel, 32)
        text('DO YOU WANT TO EXIT?', 960, 480)
        drawExitButton()
        drawCancelButton()
    
    ## SETTINGS SCREEN
    elif currentScreen == 'SETTINGS':
        drawBackground()
        drawExit()
        drawBackButton()
        drawNotifications()
        drawVolume()
        drawMusic()
        drawSoundButtons()
        drawSoundEffects()
        drawRound('SETTINGS')
        
    elif currentScreen == 'CONTACT':
        drawBackground()
        drawRound('CONTACT')
        drawExit()
        drawBackButton()
        
    elif currentScreen == 'CREDITS':
        drawBackground()
        drawRound('CREDITS')
        drawExit()
        drawBackButton()
        
    ## RULES SCREEN
    elif currentScreen == 'RULES':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound('RULES')
    
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 1 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
        drawCardPlayer(1)
        drawCardScreenBottom(1)
        
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 2 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
        drawCardPlayer(2)
        drawCardScreenBottom(2)
    
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 3 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
        drawCardPlayer(3)
        drawCardScreenBottom(3)
    
    ## PLAYER 1 CARDS SCREEN 
    elif currentScreen == 'PLAYER 4 CARDS':
        drawBackground()
        drawLeftMenu(img_exit, img_settings, img_rules)
        drawBackButton()
        drawRound(currentRound)
        drawCardPlayer(4)
        drawCardScreenBottom(4)
