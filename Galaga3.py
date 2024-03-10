import pgzrun
import random
#screen dimensions
WIDTH = 1200
HEIGHT = 600

#definiting colours
WHITE = (255,255,255)
BLUE = (0,0,255)

#create a ship
ship = Actor('galaga')
bug = Actor('bug')

ship.pos = (WIDTH//2, HEIGHT-60)

speed = 5

#define a list for bullets
bullets = []

#defining a list of enemies
enemies = []

#we want 8 enemies
for x in range(8):
    for y in range(4):
        enemies.append(Actor('bug'))
        #now the enemies will be ina straight line
        enemies[-1].x = 100+ 50*x
        #starting off the screen thats why putting it at -100,
        #slowly the enemy will come down
        enemies[-1].y = 80 + 50*y
    
score = 0
direction = 1
ship.dead = False
ship.countdown = 90

#for updating the score
def displayScore():
    screen.draw.text(str(score), (50,30))

def gameOver():
    screen.draw.text("GAME OVER", (250,300))
    
def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:        
            bullets.append(Actor('bullet'))
            #the last bullet added , set its position
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y - 50

   
def update():
    global score
    global direction
    moveDown = False
    
    #move the ship left or right with arrow keys
    if ship.dead == False:
        if keyboard.left:
            ship.x -= speed
            if ship.x <= 0:
                ship.x = 0
                
        elif keyboard.right:
            ship.x += speed
            if ship.x >= WIDTH:
                ship.x = WIDTH
            
    #to fire bullets
    #it should not be while you on hold spapce key event
    #rather it should be on s[ace key down event
    '''
    if keyboard.space:
        print("Pressing space")
        bullets.append(Actor('bullet'))
        #the last bullet added , set its position
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y
    '''
    for bullet in bullets:
        #if the bullet reaches the top of the screen it should get removed
        #else the list will become huge
        if bullet.y <=0 :
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    
    #check the position of the last enemy
    
    if len(enemies) == 0:
        gameOver()
        
    if len(enemies)>0  and (enemies[-1].x > WIDTH-80 or enemies[0].x < 80):
        moveDown = True
        direction = direction*-1
    for enemy in enemies:
        enemy.x += 5*direction
        if moveDown == True:
            enemy.y += 100
        if enemy.y > HEIGHT :
            enemies.remove(enemy)
            
        #checking if the enemy hits a bullet while moving down
        #iterate over all the bullets and check for a collision
        for bullet in bullets :
            if enemy.colliderect(bullet):
                score +=100
                #we also want to destory the bullet
                bullets.remove(bullet)
                #instead of removing the enemy we could send it back up?
                enemies.remove(enemy)
                if len(enemies) == 0:
                    gameOver()
        #checking for enemy hits the ship
        if enemy.colliderect(ship):
            ship.dead = True
    if ship.dead:
        ship.countdown -=1
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90
            
                     
def draw():
    screen.clear()
    screen.fill(BLUE)
    #ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    #ship to be drawn last
    if ship.dead == False:
        ship.draw()
    displayScore()
    if len(enemies) == 0:
        gameOver()
    
    
pgzrun.go()