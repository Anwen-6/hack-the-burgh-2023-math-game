# sweet shop game

# import
import pygame

pygame.init()
# screen and colours
screen = pygame.display.set_mode([1400,780]) 
pygame.display.set_caption("Sweet shop")
COLOR_INACTIVE = pygame.Color('black')
COLOR_ACTIVE = pygame.Color('red')
font = pygame.font.Font(None, 30)
background_image = pygame.image.load("sweetshop 1.png").convert() 
black    = (   0,   0,   0)

space = 0
question = 1

# objects

# text box
class InputBox:
#class textBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font.render(text, True, black)
        self.active = False

    def validate(self,enterdText,option,correct):
        print(enterdText,'entered text')
        if option == 1:
            if enterdText=='10':
                correct=True
                space= 3
            else:
                space=2
        elif option == 5:
            if enterdText=="4":
                correct=True
                space=6
            else:
                space=2
        elif option==8:
            if enterdText=="4":
                correct=True
                space=9
            else:
                space=2
        elif option==11:
            if enterdText=="8":
                correct=True
                space=12
            else:
                space=2
        elif option==14:
            if enterdText=="2":
                correct=True
                space=15
            else:
                space=2
        elif option==17:
            if enterdText=="3":
                correct=True
                space=18
            else:
                space=2

        return space, correct
    

    # handel event
    def handle_event(self, event, option, space,):
        input_box = InputBox(375, 203, 140, 32)
        input_boxes = [input_box]
        running = True
        correct = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    #self.text = ''
                    running = False
                    for box in input_boxes:
                        enterdText=self.text
                        space, correct =box.validate(enterdText, option, correct)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = font.render(self.text, True, self.color)
       
        return space, running
    
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # draw screen + text
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
        pygame.draw.rect(screen, self.color, self.rect, 2)




#button
def button(space):
    
    if space==0:
        text = font.render("Begin", True, black)
        button = pygame.Rect(1100,525,160,30)
    elif space==3 or space ==4:
        text = font.render("next", True, black)
        button = pygame.Rect(1100,675,160,30)
    elif space==6 or space ==7:
        text = font.render("next", True, black)
        button = pygame.Rect(1100,675,160,30)
    elif space==9 or space ==10:
        text = font.render("next", True, black)
        button = pygame.Rect(1100,675,160,30)
    elif space==12 or space ==13:
        text = font.render("next", True, black)
        button = pygame.Rect(1100,675,160,30)
    elif space==15 or space ==16:
        text = font.render("next", True, black)
        button = pygame.Rect(1120,695,160,30)
    elif space==18 or space ==19:
        text = font.render("next", True, black)
        button = pygame.Rect(1150,725,160,30)
    elif space==20:
        text = font.render("next", True, black)
        button = pygame.Rect(1100,675,160,30)
    pygame.display.update()
    

    Quit='no'
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Quit='yes'
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if button.collidepoint(mouse_pos):
                        if space==3 or space==6 or space==9 or space==12 or space==15 or space==18:
                            space=space+2
                        else:
                            space=space+1
                        running = False

        pygame.draw.rect(screen, [225, 225, 225], button)
        if space==0:
            screen.blit(text, (1150,530,100,30))
        elif space==3 or space==4:
            screen.blit(text, (1150,680,100,30))
        elif space==6 or space==7:
            screen.blit(text, (1150,680,100,30))
        elif space==9 or space==10:
            screen.blit(text, (1150,680,100,30))
        elif space==12 or space==13:
            screen.blit(text, (1150,680,100,30))
        elif space==15 or space==16:
            screen.blit(text, (1170,700,100,30))
        elif space==18 or space==19:
            screen.blit(text, (1200,730,100,30))
        elif space==20:
            screen.blit(text, (1150,680,100,30))
        pygame.display.update()

    if Quit=='yes':
        pygame.quit()
        
    return space

#try again buttons
def buttons2 (question):
    print(question,'question')
    text = font.render("Try again",True,black)
    button = pygame.Rect(480, 400, 150, 30)

    text2 = font.render("Get answer",True,black)
    button2 = pygame.Rect(780, 400, 150, 30)
    pygame.display.update()

    Quit='no'
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Quit='yes'
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if button.collidepoint(mouse_pos):
                        if question==1:
                            space=1
                        elif question==2:
                            space=5
                        elif question==3:
                            space=8
                        elif question==4:
                            space=11
                        elif question==5:
                            space=14
                        elif question==6:
                            space=17
                        running = False
                        
                    elif button2.collidepoint(mouse_pos):
                        if question==1:
                            space=4
                        elif question==2:
                            space=7
                        elif question==3:
                            space=10
                        elif question==4:
                            space=13
                        elif question==5:
                            space=16
                        elif question==6:
                            space=19
                        running = False 
        pygame.draw.rect(screen, [225, 225, 225], button)
        screen.blit(text, (508,405,100,30))
        pygame.draw.rect(screen, [225, 225, 225], button2)
        screen.blit(text2, (800,405,100,30))
        pygame.display.update()

    if Quit=='yes':
        pygame.quit()
        sys.exit
    return space

# text box
def textbox(option,space,background_image):
    if option == 1:
        screen.blit(background_image, [-40,0])
    elif option==5:
        screen.blit(background_image, [-10,0])
    elif option==8:
        screen.blit(background_image, [-10,0])
    elif option==11:
        screen.blit(background_image, [-20,-20])
    elif option==14:
        screen.blit(background_image, [-30,-30])
    elif option==17:
        screen.blit(background_image, [0,0])
    #screen.blit(background_image, [0,0])
    clock = pygame.time.Clock()

    text = font.render("type when box is red", 1, black)
    text2 = font.render("press enter to submit answer", 1, black)


    if option == 1:
        input_box = InputBox(960, 640, 140, 32)
    elif option==5:
        input_box = InputBox(820, 630, 140, 32)
    elif option==8:
        input_box = InputBox(820, 620, 140, 32)
    elif option==11:
        input_box = InputBox(800, 640, 140, 32)
    elif option==14:
        input_box = InputBox(915, 620, 140, 32)
    elif option==17:
        input_box = InputBox(990, 590, 140, 32)
    input_boxes = [input_box]

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            for box in input_boxes:
                space,running=box.handle_event(event,option,space)


            #screen.blit(background_image, [0,0])
        for box in input_boxes:
            box.update()
        
        for box in input_boxes:
            box.draw(screen)

        screen.blit(text, (50,600,500, 200))
        screen.blit(text2, (20,650, 500, 200))

##        screen.blit(text, (50,600,500, 200))  
##        screen.blit(text2, (50,650, 500, 200))

        pygame.display.flip()
        clock.tick(20)

    return space




# changing the page
def drawIntro(screen,space,question):
    # page 0 start/ info page
    running=True
    if space == 0:

        background_image = pygame.image.load("1stpage.png").convert() 
        screen.blit(background_image, [-80,0])
        # display button
        space=button(space)
        print(space,'space test2')
        pygame.display.update()
        
    # page 1 challange 1
    elif space == 1:
        option=1
        background_image = pygame.image.load("challange1png.png").convert() 
        screen.blit(background_image, [-50,0])
        space=textbox(option, space, background_image)
        pygame.display.update()

    # page 2 wrong try again
    elif space == 2:
        background_image = pygame.image.load("notrightpage.png").convert() 
        screen.blit(background_image, [-50,0])
        space=buttons2(question)
        pygame.display.update()

    # page 3 challange 1 yay answer
    elif space == 3:
        background_image = pygame.image.load("correctanwer1.png").convert() 
        screen.blit(background_image, [-50,0])
        space=button(space)
        pygame.display.update()

    # page 4 challange 1 nay answer
    elif space == 4:
        background_image = pygame.image.load("answer1.png").convert() 
        screen.blit(background_image, [-50,0])
        space=button(space)
        pygame.display.update()

    # page 5 challange 2
    elif space == 5:
        question=2
        option=5
        background_image = pygame.image.load("challang2a.png").convert() 
        screen.blit(background_image, [-10,0])
        space=textbox(option, space, background_image)
        pygame.display.update()

    # page 6 challange 2 yay answer
    elif space == 6:
        background_image = pygame.image.load("2acorrectanswer.png").convert() 
        screen.blit(background_image, [-10,0])
        space=button(space)
        pygame.display.update()

    # page 7 challange 2 nay answer
    elif space == 7:
        background_image = pygame.image.load("2aanswer.png").convert() 
        screen.blit(background_image, [-10,0])
        space=button(space)
        pygame.display.update()

        # page 8 challange 2b
    elif space == 8:
        question=3
        option=8
        background_image = pygame.image.load("challange2b.png").convert() 
        screen.blit(background_image, [-10,0])
        space=textbox(option, space, background_image)
        pygame.display.update()

    # page 9 challange 2b yay answer
    elif space ==9:
        background_image = pygame.image.load("2bcorrectanswer.png").convert() 
        screen.blit(background_image, [-10,0])
        space=button(space)
        pygame.display.update()

    # page 10 challange 2b nay answer
    elif space == 10:
        background_image = pygame.image.load("2banswe4.png").convert() 
        screen.blit(background_image, [-10,0])
        space=button(space)
        pygame.display.update()

    # page 11 challange 2c
    elif space == 11:
        question=4
        option=11
        background_image = pygame.image.load("challange2c.png").convert() 
        screen.blit(background_image, [-10,0])
        space=textbox(option, space, background_image)
        pygame.display.update()

    # page 12 challange 2c yay answer
    elif space ==12:
        background_image = pygame.image.load("2ccorrectanswer.png").convert() 
        screen.blit(background_image, [-40,-30])
        space=button(space)
        pygame.display.update()

    # page 13 challange 2c nay answer
    elif space == 13:
        background_image = pygame.image.load("2canswer.png").convert() 
        screen.blit(background_image, [-40,-30])
        space=button(space)
        pygame.display.update()

    # page 14 challange 2d
    elif space == 14:
        question=5
        option=14
        background_image = pygame.image.load("challange2d.png").convert() 
        screen.blit(background_image, [-10,0])
        space=textbox(option, space, background_image)
        pygame.display.update()

    # page 15 challange 2d yay answer
    elif space ==15:
        background_image = pygame.image.load("2dcorrectanswer.png").convert() 
        screen.blit(background_image, [-50,-20])
        space=button(space)
        pygame.display.update()

    # page 16 challange 2d nay answer
    elif space == 16:
        background_image = pygame.image.load("2danswed.png").convert() 
        screen.blit(background_image, [-50,-20])
        space=button(space)
        pygame.display.update()

    # page 17 challange 3
    elif space == 17:
        question=6
        option=17
        background_image = pygame.image.load("Challange3.png").convert() 
        screen.blit(background_image, [-10,0])
        space=textbox(option, space, background_image)
        pygame.display.update()

    # page 18 challange 3 yay answer
    elif space ==18:
        background_image = pygame.image.load("3correctanswer.png").convert() 
        screen.blit(background_image, [-20,-30])
        space=button(space)
        pygame.display.update()

    # page 19 challange 3 nay answer
    elif space == 19:
        background_image = pygame.image.load("3answer.png").convert() 
        screen.blit(background_image, [-20,-30])
        space=button(space)
        pygame.display.update()

    # page 20 after
    elif space == 20:
        background_image = pygame.image.load("resolution.png").convert() 
        screen.blit(background_image, [-50,0])
        space=button(space)
        pygame.display.update()

    # page 21 after
    elif space == 21:
        background_image = pygame.image.load("thankyous.png").convert() 
        screen.blit(background_image, [-50,-20])
        pygame.display.update()
        
    return space, question
        
        


# main programe

screen.blit(background_image, [0,0])
clock = pygame.time.Clock()
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #space, question=drawIntro(screen,space,question)
        space, question=drawIntro(screen,space,question)
        pygame.display.flip()
        clock.tick(20)

pygame.quit()

