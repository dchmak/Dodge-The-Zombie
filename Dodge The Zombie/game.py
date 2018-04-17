import pygame as pg
import random

black = (0, 0, 0)

windowSize = windowWidth, windowHeight = 800, 800
fps = 60

close = False

def collide(pos1, size1, pos2, size2):
    return not (pos1[0] + size1[0] <= pos2[0] or
                pos1[0] >= pos2[0] + size2[0] or
                pos1[1] + size1[1] <= pos2[1] or
                pos1[1] >= pos2[1] + size2[1])

def outBound(pos, size):
    return not (pos[0] + size[0] >= 0 and
                pos[1] + size[1] >= 0 and
                pos[0] <= windowWidth and
                pos[1] <= windowHeight)


# Car data
carSize = [carWidth, carHeight] = [90, 210]
carImg = pg.image.load('Image\GreenCar.png')
carImg = pg.transform.scale(carImg, carSize)

def drawCar(pos):
    display.blit(carImg, pos)
    

# Zombie data
zombieSize = [zombieWidth, zombieHeight] = [102, 128]
zombieSpeed = 1
zombieImg = pg.image.load('Image\Zombie.png')
zombieImg = pg.transform.scale(zombieImg, zombieSize)

zombieNo = 3
zombies = []
def createZombies(num):
    for i in range(num):
        found = False
        while not found:
            pos = [x, y] = [random.randint(0, windowWidth - zombieWidth),
                            random.randint(0, 100)]
            found = True
            for zombie in zombies:
                if ( collide(zombie, zombieSize, pos, zombieSize) ):
                    found = False            
            
        zombies.append( pos )

createZombies(3)

def drawZombie(pos):
    display.blit(zombieImg, pos)


# Gameover
lost = False
gameoverImg = pg.image.load('Image\Gameover.png')
    

# Main
pg.init()

pg.font.init()
font = pg.font.SysFont('Comic Sans MS', 30)

clock = pg.time.Clock()
clock.tick(fps)

display = pg.display.set_mode(windowSize)
pg.display.set_caption('Game')

while not close:
    if not lost:
        pg.display.set_caption('Game ' + str(len(zombies)))

        display.fill(black)

        if outBound(pg.mouse.get_pos(), (0, 0)):
            print('out!')

        carPos = [carX, carY] = (pg.mouse.get_pos()[0] - carWidth/2,
                                 pg.mouse.get_pos()[1] - carHeight/2)

        '''
        if outBound(carPos, carSize):
            print('out!')
        '''     
        
        drawCar(carPos)

        for zombiePos in zombies:
            zombiePos[1] += zombieSpeed;
            drawZombie( zombiePos )
            
            if collide(carPos, carSize, zombiePos, zombieSize):
                #print('crash!')
                clock.tick(fps)
                lost = True
                            
            if outBound(zombiePos, zombieSize):
                zombies.remove(zombiePos);
                createZombies(1)

        zombieSpeed += 0.0001
        
    else:
        display.fill(black)
        display.blit(gameoverImg, ( (windowWidth - 568)/2,
                                    (windowHeight - 75)/2 ))
        string = 'Time: ' + str(clock.get_time()/1000) + ' s'
        text = font.render(string, True, (255,255,255))
        textSize = textWidth, textHeight = font.size(string)
        display.blit(text, ( (windowWidth - textWidth)/2,
                             windowHeight*3/4 - textHeight ))


    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            close = True
        

pg.quit()
