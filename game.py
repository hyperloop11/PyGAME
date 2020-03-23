import pygame
import time

pygame.init()
pygame.mixer.init()
win =  pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

#loading images of our character. images of enemy in enemy class
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#loading audio files
t = pygame.mixer.music
t.load('bullet.wav')
#t.load('bgmusic.wav')
#t.play(-1, 0.0)
t.load('hit.wav')

clock = pygame.time.Clock()

class player():
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 10 #your man.vel is 10 but video man.vel in 5
        self.isJump = False
        self.jumpcount = 10
        self.left = False
        self.right = False
        self.walkcount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y+ 11, 29, 52) #(x,y, width, height)

    def draw(self, win):
        if self.walkcount +1>= 27:
            self.walkcount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[man.walkcount//3], (self.x,self.y))
                self.walkcount +=1
            elif self.right:
                win.blit(walkRight[man.walkcount//3], (man.x,man.y))
                self.walkcount +=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
        self.hitbox = (self.x + 17, self.y+ 11, 29, 52) #to make hitbox move with the player
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self):
        print('kill')
        self.isJump = False #because if jumping man hits goblin, it continues its downward jump.
        self.jumpcount = 10
        self.x = 60
        self.y = 410
        goblin.x = 300
        goblin.y = 410
        walkcount = 0
        font1 = pygame.font.SysFont('corbel', 100)
        text = font1.render('-5',1, (255, 0, 0))
        win.blit(text,(250 - (text.get_width()/2), 240- (text.get_height()/2) ))
        pygame.display.update()
        time.sleep(2)

class Projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 5

    def draw(self, win):
        pygame.draw.circle( win, self.color, (self.x, self.y), self.radius)


class Enemy():
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x,self.end] #problem lag raha h
        self.walkcount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y+2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        if self.visible:
            self.move()  #very importanat to call on move function
            if self.walkcount + 1 >= 33:
                self.walkcount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkcount//3],(self.x, self.y))
                self.walkcount += 1
            else:
                win.blit(self.walkLeft[self.walkcount//3], (self.x, self.y))
                self.walkcount += 1
            pygame.draw.rect(win,(255,0,0), (self.hitbox[0],self.hitbox[1]- 20,50, 10))
            pygame.draw.rect(win,(0,128,0), (self.hitbox[0],self.hitbox[1]-20,50 -(5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y+2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel>0:
            if self.x +self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0

    def hit(self):
        print('hit')
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
            walkcount = 0

def redrawgamewindow():
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    if goblin.visible:
        text = font.render('Score: ' + str(score),1 , (0,0,0))
        win.blit(text, (380,10))
    else:
        text3 = font.render('Your score is '+ str(score), 1, (0,0,110))
        win.blit(text3,(250 - (text3.get_width()/2), 240- (text3.get_height()/2)))
    pygame.display.update()


#creating instances of characters
man = player(300, 410, 64, 64)
goblin = Enemy(50,410,64,64,450)

bulletsound = pygame.mixer.Sound('bullet.wav')
hitsound = pygame.mixer.Sound('hit.wav')
#bgsouond = pygame.mixer.Sound('bgmusic.wav')
#pygame.mixer.music.load('bgmusic.mp3')
#bgsound.play(-1)

font = pygame.font.SysFont('corbel', 30, True)
score = 0
shootcount = 0
bullets = []

run = True
while run:
    clock.tick(27)
    if shootcount in range(3): #basic timer for bullets
        shootcount += 1
    else:
        shootcount =  0

    for event in pygame.event.get(): #an entery in the list of events, get means get the entry.
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel*bullet.facing
        else:
            bullets.pop(bullets.index(bullet))
        if pygame.Rect(goblin.hitbox).collidepoint(bullet.x, bullet.y):
            goblin.hit()
            score += 1
            hitsound.play()
            bullets.pop(bullets.index(bullet))

    if goblin.visible:
        if pygame.Rect(goblin.hitbox).colliderect(man.hitbox):
            man.hit()
            score -= 5

    keys = pygame.key.get_pressed()
    if man.left:
        facing = -1
    else:
        facing = 1
    if keys[pygame.K_SPACE] and shootcount == 0:
        bulletsound.play()
        if len(bullets)<5:
            bullets.append(Projectile(round(man.x + man.width//2),round(man.y +man.height//2),5, (0,0,0), facing))

    if keys[pygame.K_RIGHT] and man.x < 500-man.width-man.vel: #alwasys put man.width rather than arbitary value
        man.x += man.vel                                    #so that you dont have to remember .
        man.right = True
        man.left = False
        man.standing = False

    elif keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False

    else:
        man.standing = True
        man.walkcount = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkcount = 0

    else:
        '''if man.jumpcount >= -10:
            man.y -= (man.jumpcount**2)/2
            man.jumpcount -= 1
        if man.jumpcount in range(-10,0):
            man.y -= -(man.jumpcount**2)/2
            man.jumpcount -= 1'''
        if man.jumpcount >= -10:
            neg =1
            if man.jumpcount<0:
                neg = -1
            man.y -= (man.jumpcount**2)/2 *neg
            man.jumpcount -= 1
        else:
            man.isJump = False
            man.jumpcount = 10

    redrawgamewindow()


pygame.quit()
