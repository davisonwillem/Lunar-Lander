#%%#    imports

# import various modules
import numpy as np 
import time
import pygame
# initiate pygame
pygame.init()
# setting font sizes
font1 = pygame.font.SysFont("bahnschrift", 20)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 100)

#%%#    window

# setting window & screen
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Lunar Lander")
# loading various images and setting their sizes
startscreen = pygame.image.load("startscreen.jpg")
startscreen = pygame.transform.scale(startscreen,(1152,768))
background = pygame.image.load("background.png")
background = pygame.transform.scale(background,(1024,768))
moonsurface = pygame.image.load("moonsurface.png")
moonsurface = pygame.transform.scale(moonsurface,(1024,40))
rocket = pygame.image.load("rockettransparent.png")
rocket = pygame.transform.scale(rocket,(100,150))
rocketnjets = pygame.image.load("rocketnjetstransparent.png")
rocketnjets = pygame.transform.scale(rocketnjets,(100,200))

#%%#    GIF

# as pygame does not support GIFs, the frames will be upload and reconstructed manually
f1 = pygame.image.load("f1.png")
f1 = pygame.transform.scale(f1,(1024,800))
f2 = pygame.image.load("f2.png")
f2 = pygame.transform.scale(f2,(1024,800))
f3 = pygame.image.load("f3.png")
f3 = pygame.transform.scale(f3,(1024,800))
f4 = pygame.image.load("f4.png")
f4 = pygame.transform.scale(f4,(1024,800))
f5 = pygame.image.load("f5.png")
f5 = pygame.transform.scale(f5,(1024,800))
f6 = pygame.image.load("f6.png")
f6 = pygame.transform.scale(f6,(1024,800))
f7 = pygame.image.load("f7.png")
f7 = pygame.transform.scale(f7,(1024,800))
f8 = pygame.image.load("f8.png")
f8 = pygame.transform.scale(f8,(1024,800))
f9 = pygame.image.load("f9.png")
f9 = pygame.transform.scale(f9,(1024,800))
f10 = pygame.image.load("f10.png")
f10 = pygame.transform.scale(f10,(1024,800))
f11 = pygame.image.load("f11.png")
f11 = pygame.transform.scale(f11,(1024,800))
f12 = pygame.image.load("f12.png")
f12 = pygame.transform.scale(f12,(1024,800))
f13 = pygame.image.load("f13.png")
f13 = pygame.transform.scale(f13,(1024,800))
f14 = pygame.image.load("f14.png")
f14 = pygame.transform.scale(f14,(1024,800))
f15 = pygame.image.load("f15.png")
f15 = pygame.transform.scale(f15,(1024,800))
f16 = pygame.image.load("f16.png")
f16 = pygame.transform.scale(f16,(1024,800))
f17 = pygame.image.load("f17.png")
f17 = pygame.transform.scale(f17,(1024,800))
f18 = pygame.image.load("f18.png")
f18 = pygame.transform.scale(f18,(1024,800))

#%%#    variables

# defining the game as a function to allow replay
def LunarLander():
    # setting various variables
    h = 10
    x = 0
    v = 0
    vx = 0
    a = 10
    ax = 0
    dt = 0.02
    fuel = 100
    both = 0
    # random landing pad position
    landing = np.random.randint(1,9)
    
#%%#    start screen

    # setting up start screen and waiting for input to continue
    l = 0
    while l == 0:
        for event in pygame.event.get():
            screen.blit(startscreen,(0,0))
            screen.blit(font3.render("LUNAR LANDER", True, (110,110,120)),(50,10))
            screen.blit(font2.render("Press SPACE to start", True, (0,0,0)),(520,495))
            screen.blit(font1.render("-SPACE for main thrusters", True, (0,0,0)),(520,570))
            screen.blit(font1.render("-A & D for transverse thrusters", True, (0,0,0)),(520,590))
            screen.blit(font1.render("-ESCAPE to pause", True, (0,0,0)),(520,610))
            screen.blit(font1.render("Land on the landing pad at low speed", True, (0,0,0)),(520,650))
            screen.blit(font1.render("Velocity indicator top left", True, (0,0,0)),(520,670))
            pygame.display.update()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                l=1
    
#%%#    game

    while h > 0:
        time.sleep(0.05)
        for event in pygame.event.get():
            # at all times expecting ESC input to pause
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.draw.rect(screen,(110,110,120),pygame.Rect(462,284,30,100))
                pygame.draw.rect(screen,(110,110,120),pygame.Rect(532,284,30,100))
                screen.blit(font2.render("GAME PAUSED", True, (110,110,120)),(344,400))
                screen.blit(font2.render("press ESC to continue", True, (110,110,120)),(265,450))
                pygame.display.update()
                pause = 0
                while pause == 0:
                    for event in pygame.event.get():
                        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                            pause=1
            # at all times expecting SPACE input to give thrust
            if pygame.key.get_pressed()[pygame.K_SPACE] and fuel > 0:
                # change upwards acceleration
                a = -20
                # change position of rocket and image
                screen.blit(rocketnjets,(462+x,600-h*76.8))
                pygame.display.update()
            else:
                a = 10
            # at all times expecting A & D inputs for left right thrust
            if pygame.key.get_pressed()[pygame.K_a] and pygame.key.get_pressed()[pygame.K_d] and fuel > 0:
                ax = 0
                # so that both keys in the image can light up at the same time if both pressed
                both = 1
            elif pygame.key.get_pressed()[pygame.K_a] and fuel > 0:
                ax = 500
            elif pygame.key.get_pressed()[pygame.K_d] and fuel > 0:
                ax = -500
            else:
                ax = 0
                both = 0
        screen.blit(background,(0,0))
        screen.blit(moonsurface,(0,730))
        if a == -20:
            # reduce fuel and light up space key
            pygame.draw.rect(screen,(100,100,100),pygame.Rect(800,100,200,50))
            fuel = fuel - 3
            screen.blit(rocketnjets,(462+x,600-h*76.8))
        else:
            pygame.draw.rect(screen,(50,50,50),pygame.Rect(800,100,200,50))
            screen.blit(rocket,(462+x,600-h*76.8))
        # altering movement
        v = v - a*dt
        h = h + v*dt
        vx = vx - ax*dt
        x = x + vx*dt
        if v < -3:
            # velocity display showing red or green
            pygame.draw.circle(screen,(110,110,120),(55,85),27)
            pygame.draw.circle(screen,(100,0,0),(55,85),25)
        else:
            pygame.draw.circle(screen,(110,110,120),(55,85),27)
            pygame.draw.circle(screen,(0,100,0),(55,85),25)
        if fuel > 0:
            # show the "FUEL OUT" square as empty
            pygame.draw.rect(screen,(110,110,120),pygame.Rect(28,673,54,54))
            pygame.draw.rect(screen,(0,0,0),pygame.Rect(30,675,50,50))
        else:
            # show the square as full
            pygame.draw.rect(screen,(110,110,120),pygame.Rect(28,673,54,54))
            pygame.draw.rect(screen,(100,0,0),pygame.Rect(30,675,50,50))
            screen.blit(font1.render("FUEL", True, (110,110,120)),(31,678))
            screen.blit(font1.render("OUT", True, (110,110,120)),(36,697))
        if ax == 500:
            # lighting up left and right keys
            pygame.draw.rect(screen,(100,100,100),pygame.Rect(830,30,50,50))
            pygame.draw.rect(screen,(50,50,50),pygame.Rect(920,30,50,50))
        elif ax == -500:
            pygame.draw.rect(screen,(50,50,50),pygame.Rect(830,30,50,50))
            pygame.draw.rect(screen,(100,100,100),pygame.Rect(920,30,50,50))
        elif both == 0:
            pygame.draw.rect(screen,(50,50,50),pygame.Rect(830,30,50,50))
            pygame.draw.rect(screen,(50,50,50),pygame.Rect(920,30,50,50))
        else:
            pygame.draw.rect(screen,(100,100,100),pygame.Rect(830,30,50,50))
            pygame.draw.rect(screen,(100,100,100),pygame.Rect(920,30,50,50))
        # draw arrows on keys
        screen.blit(font3.render("<", True, (0,0,0)),(833,-13))
        screen.blit(font3.render(">", True, (0,0,0)),(923,-13))
        # draw border of fuel guage
        pygame.draw.rect(screen,(110,110,120),pygame.Rect(28,153,54,504))
        # draw black interior of fuel guage
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(30,155,50,500))
        # draw fuel level
        pygame.draw.rect(screen,(66,77,11),pygame.Rect(30,655-fuel*5,50,fuel*5))
        screen.blit(font1.render("FUEL:", True, (110,110,120)),(28,125))
        screen.blit(font1.render("VEL.:", True, (110,110,120)),(30,30))
        # draw on landing pad
        pygame.draw.rect(screen,(40,50,50),pygame.Rect(100*landing,750,200,18))
        screen.blit(font1.render("LANDING PAD", True, (110,110,120)),(100*landing+38,746))
        pygame.display.update()

#%%#    end

    blackscreen = pygame.Surface((1024,768))
    # set criterior for success
    if v > -3 and 475+x > 100*landing and 349+x < 100*landing:
        # fade screen into black
        for i in range(0,50):
            time.sleep(0.07)
            blackscreen.set_alpha(i)
            screen.blit(blackscreen,(0,0))
            pygame.display.update()
        # show well done message and instructions, time delayed
        screen.fill((0,0,0))
        screen.blit(font3.render("WELL DONE", True, (110,110,120)),(241,250))
        pygame.display.update()
        time.sleep(1)
        screen.blit(font2.render("Press SPACE to play again", True, (110,110,120)),(214,400))
        pygame.display.update()
        time.sleep(1)
        screen.blit(font2.render("or ESC to quit", True, (110,110,120)),(358,450))
        pygame.display.update()
        # wait for input of SPACE or ESC
        p = 0
        while p == 0:
            for event in pygame.event.get():
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    p=1
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    # if input is esc, end the game
                    pygame.quit()
                    return()
        # if input is space the while loop is broken and LunarLander function is restarted
        LunarLander()
    else:
        # load frames of GIF into array
        frames = np.array([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18])
        for i in range (0,18,1):
            # show frames one after another with time delay
            screen.blit(frames[i],(x,-10))
            pygame.display.update()
            time.sleep(0.05)
        for i in range(0,50):
            time.sleep(0.07)
            blackscreen.set_alpha(i)
            screen.blit(blackscreen,(0,0))
            pygame.display.update()
        screen.fill((0,0,0))
        screen.blit(font3.render("YOU CRASHED", True, (110,110,120)),(187,250))
        pygame.display.update()
        time.sleep(1)
        screen.blit(font2.render("Press SPACE to try again", True, (110,110,120)),(231,400))
        pygame.display.update()
        time.sleep(1)
        screen.blit(font2.render("or ESC to quit", True, (110,110,120)),(359,450))
        pygame.display.update()
        p = 0
        while p == 0:
            for event in pygame.event.get():
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    p=1
                elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    return()
        LunarLander()

#%%# initial run

# run the LunarLander function for the first time
LunarLander()

#%%#