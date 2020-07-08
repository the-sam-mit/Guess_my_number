import pygame
import time
import random

pygame.init()
win = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption("Guess The Number") 
# Indicates pygame is running 
run = True
x = 200
y = 200
width = 40
height = 40
# infinite loop
white = (255, 255, 255) 
green = (0, 255, 0) 
green = (8, 130, 130) 
blue = (4, 30, 66)
blue = (156, 196, 213)
light_green = (0, 0, 210)
font40 = pygame.font.Font('freesansbold.ttf', 30)
font = pygame.font.Font('freesansbold.ttf', 40)

font100 = pygame.font.Font('freesansbold.ttf', 70)
target = (random.randrange(0, 1000, 3))
print(target)
str = ""
score = 0

guessImg = pygame.image.load('images.jpeg')

text4 = font100.render('Guess The Number', True, green, blue)  
textRect4 = text4.get_rect()
textRect4.center = (600, 100)
instructions = 'Instructions :-  Guess a number from 1 to 1000.'

instruct = font40.render(instructions, True, light_green, blue)  
instruct4 = instruct.get_rect()
instruct4.center = (500, 700)


while run: 
    win.fill(blue) 
    pygame.time.delay(30) 
    great = 0
    final = 0
    result = 'Try a bigger number'
    for event in pygame.event.get(): 
          
        if event.type == pygame.QUIT: 
            run = False
            
        if event.type == pygame.KEYDOWN: 
            keyss = pygame.key.name(event.key)
            print ('"{}" key pressed'.format(keyss))
            if keyss == 'backspace':
                str = ""
                continue
            if keyss == 'return':
                score = score + 1
                num = int(str)
                print(num)
                if num > target:
                    result = 'Try a smaller number'
                if num == target:
                    if score <= 6:
                        result = 'Awesome!! You are genius'
                    elif score <= 10:
                        result = 'Great!! You are smart'
                    elif score <= 30:
                        result = 'Hurray!! Try to play better'
                    final = 1
                str = ""
                great = 1
            else:
                str = str + keyss
    
    text = font.render(str, True, light_green, blue)  
    textRect = text.get_rect()
    textRect.center = (300, 300)
    win.blit(text4, textRect4)
    win.blit(guessImg, (895, 160))
    win.blit(instruct, instruct4)


    win.blit(text, textRect)
    if great == 1:
        text2 = font.render(result, True, light_green, blue)  
        textRect2 = text2.get_rect()
        textRect2.center = (350, 350)
        win.blit(text2, textRect2)                
        pygame.display.update()  
        time.sleep(1) 

    great = 0
    if final == 1:
        break

      
    pygame.display.update()  

strn = "Your final score is {}".format(score)
print (strn) 
text3 = font.render(strn, True, green, blue)  
textRect3 = text3.get_rect()
textRect3.center = (300, 300)
win.blit(text3, textRect3)                
pygame.display.update()  
time.sleep(1) 

pygame.quit() 
