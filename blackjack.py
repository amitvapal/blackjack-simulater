'''
Student Name: 
Game title:
Period:
Features of Game: 
'''

import pygame, sys, os                                      #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=700                                                   #Open and set window size
h=500                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Set caption here")          #set window title

#declare global variables here
background = pygame.image.load("background.png")
BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#other global variables (WARNING: use sparingly):





#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:
def showMessage(words, size, font, x, y, color, bg = None):
    text_font = pygame.font.SysFont(font, size, True, False)
    text = text_font.render(words, True, color, bg)
    textBounds = text.get_rect()
    textBounds.center = (x, y)    
    
    #return bounding rectangle for click detection
    return text, textBounds

def drawScreen():
    blackjackBackground = surface.blit(background, (0,0))
    titleText, titleBounds = showMessage("BlackJack", 60, "Consolas", w/2, h/11, BLUE)
    surface.blit(titleText,titleBounds)
    dealHandText, dealHandBounds = showMessage("Deal Hand", 15, "Consolas", w/2, h/1.2, WHITE)
    surface.blit(dealHandText,dealHandBounds) 
    hitText, hitBounds = showMessage("Hit", 15, "Consolas", w/4.5, h/1.2, WHITE)
    surface.blit(hitText,hitBounds)    
    
    

def createDeck():
    point_value = {}
    points = 0
    cardFileNames = os.listdir("card_images")
    print(cardFileNames)
    cardFileNames.sort()
    for i in cardFileNames:
        points += 1
        point_value.update({i:points})
        if points == 11:
            points = 1
            points += 1
            point_value.update({i:points})
        else:
            pass
        if i == "c10.gif" or i == "d10.gif" or i == "h10.gif" or  i == "s10.gif" or i == "cj.gif" or i == "ck.gif" or i == "cq.gif" or i == "dj.gif" or i == "dk.gif" or i == "dq.gif" or i == "hj.gif" or i == "hk.gif" or i == "hq.gif" or i == "sk.gif" or i == "sj.gif" or i == "sq.gif":
            points = 10
            point_value.update({i:points})
        else:
            pass
        if i == "d1.gif" or  i == "h1.gif" or i == "s1.gif":
            points = 1
            point_value.update({i:points})        

    return point_value



# -------- Main Program Loop -----------
def main():
    deck = createDeck()
    lookupDeck = deck.values()
    mainDeck = deck.keys()
    print(lookupDeck)
    
    #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    
    
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
        
      
        surface.fill(WHITE)                             #set background color
        
        #drawing code goes here
        drawScreen()
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
