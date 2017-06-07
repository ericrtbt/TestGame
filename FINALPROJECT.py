import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
DARKGREEN = (35, 150, 35)

level = 1
score = 0
gameover = False 
# --- Classes
 
 
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
        
        # Load the image
        self.image = pygame.image.load("alien.png").convert() 
        self.rect = self.image.get_rect()
        # Set our transparent color
        self.image.set_colorkey(BLACK)       
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
    def update(self):
        self.rect.y += 1
        if self.rect.y > 600:
            self.reset_pos()
        
        if level == 2:
            self.rect.y += 1     
            
            
class Ufo(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
        
        # Load the image
        self.image = pygame.image.load("ufo.png").convert() 
        self.rect = self.image.get_rect()
        # Set our transparent color
        self.image.set_colorkey(WHITE)       
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
    def update(self):
        self.rect.y += 2
        if self.rect.y > 600:
            self.reset_pos()
       

 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Load the image
        self.image = pygame.image.load("player.png").convert()
     
        # Set our transparent color
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.rect.x = pos[0]
 
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3
 
 
# --- Create the window
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
 
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
# --- Create the sprites

for i in range(14):
    # This represents a block
    block = Block(DARKGREEN)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(-300, -20) 
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
#GET UFO TO SPAWN IN LEVEL 2    
if level == 1:
    for i in range(8):
        # This represents a block
        block = Ufo(DARKGREEN)
 
        # Set a random location for the block
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(-300, -20) 
    
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
# Create a red player block
player = Player()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 

player.rect.y = 605

# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)



display_instructions = True
instruction_page = 1
name = ""
#Background Music
pygame.mixer.music.load('music.ogg')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

background_image = pygame.image.load("background.bmp").convert()
click_sound = pygame.mixer.Sound("Gun.ogg") 
# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                name += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.key == pygame.K_RETURN:
                instruction_page += 1  
                if instruction_page == 3:
                    display_instructions = False                
                    pygame.mixer.music.stop()
                  
    # Set the screen background
    screen.fill(BLACK)
    #Put in Background Image
    screen.blit(background_image, [0, 0])        
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
 
        text = font.render("DEFENDER OF SPACE", True, WHITE)
        screen.blit(text, [220, 10])
       
        text = font.render("Enter your username: ", True, WHITE)
        screen.blit(text, [10, 40])    
       
        text = font.render(name, True, WHITE)
        screen.blit(text, [270, 40])        
 
        text = font.render("Hit enter to continue.", True, WHITE)
        screen.blit(text, [10, 70])
           

 
    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render("Control your Spaceship with the mouse.", True, WHITE)
        screen.blit(text, [10, 10])    
 
        text = font.render("Use the left mouse button to fire", True, WHITE)
        screen.blit(text, [10, 40])
 
        text = font.render("Hit enter to continue.", True, WHITE)
        screen.blit(text, [10, 80])
        
        text = font.render("Gain Points by Shooting the Aliens.", True, WHITE)
        screen.blit(text, [10, 110])        
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    

 
# -------- Main Program Loop -----------

   
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    file = open('highscore.txt', 'w')
    writescore = str(score) + "\n"
    file.write(writescore)
    writename = name + "\n"
    file.write(writename)
    file.close()                
               
               
    try:
        file = open('highscore.txt', 'r')
        lines = file.readlines()
        prevhighscore = int(lines[0])
        prevname = lines[1]
        file.close()                    
    except IOError:
        file = open('highscore.txt', 'w')
        writescore = str(score) + "\n"
        file.write(writescore)
        writename = name + "\n"
        file.write(writename)
        file.close()
 
 
    if score > prevhighscore:
        file = open('highscore.txt', 'w')
        writescore = str(score) + "\n"
        file.write(writescore)
        writename = name + "\n"
        file.write(writename)
        file.close()            

         
    
    # --- Game logic

    

    
    # Call the update() method on all the sprites
    all_sprites_list.update()
 
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
            if score == 10:
                level += 1  
                
                for block in block_list:
                    block.reset_pos()

          
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
           
           
    if pygame.sprite.spritecollide(player, block_list, True):
        gameover = True
        pygame.quit()
        
    if pygame.sprite.spritecollide(player, block_list, True):
        gameover = True        
    if gameover == True:
        screen.fill(BLACK) 
        text = font.render("GAME OVER", True, WHITE)
        screen.blit(text, [50, 240])
    # --- Draw a frame
   
     
    #Displaying Level
    screen.blit(background_image, [0, 0])        
    leveltext = "LEVEL: " + str(level)
    text = font.render(leveltext, True, WHITE)
    screen.blit(text, [0, 0])    
    
    #Displaying Score
    scoretext = "SCORE: " + str(score)
    text = font.render(scoretext, True, WHITE)
    screen.blit(text, [0, 25])      
    
    #Displaying High Score
    file = open('highscore.txt', 'r')
    lines = file.readlines()    
    highscoretext = "HIGHSCORE : " + str(prevhighscore)
    text = font.render(highscoretext, True, WHITE)
    screen.blit(text, [0, 50])      

    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()