import pygame, random
pygame.init()

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.width, self.height = width, height
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, WIDTH)
    def update(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.y > HEIGHT + 15:
            self.reset_pos()
        
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.width, self.height = width, height
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x, self.rect.y = (pos[0] - self.width / 2, pos[1] - self.height / 2)

class Everything(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.plus_block_list = pygame.sprite.Group()
        self.minus_block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.player = Player(BLUE, block_width, block_height)
        self.all_sprites_list.add(self.player)
        for i in range(50):
            self.block = Block(GREEN, block_width, block_height)
            self.block.rect.x, self.block.rect.y = random.randrange(WIDTH), random.randrange(HEIGHT)
            self.plus_block_list.add(self.block)
            self.all_sprites_list.add(self.block)
        for i in range(10):
            self.block = Block(RED, block_width, block_height)
            self.block.rect.x, self.block.rect.y = random.randrange(WIDTH), random.randrange(HEIGHT)
            self.minus_block_list.add(self.block)
            self.all_sprites_list.add(self.block)
    def create(self):
        self.plus_block_list = pygame.sprite.Group()
        self.minus_block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.player = Player(BLUE, block_width, block_height)
        self.all_sprites_list.add(self.player)
        for i in range(50):
            self.block = Block(GREEN, block_width, block_height)
            self.block.rect.x, self.block.rect.y = random.randrange(WIDTH), random.randrange(HEIGHT)
            self.plus_block_list.add(self.block)
            self.all_sprites_list.add(self.block)
        for i in range(10):
            self.block = Block(RED, block_width, block_height)
            self.block.rect.x, self.block.rect.y = random.randrange(WIDTH), random.randrange(HEIGHT)
            self.minus_block_list.add(self.block)
            self.all_sprites_list.add(self.block)

    def check_collide(self):
        global SCORE
        if pygame.sprite.spritecollide(self.player, self.plus_block_list, True):
            SCORE += 1
            self.block.reset_pos()
            create_block(GREEN, self.plus_block_list)
        if pygame.sprite.spritecollide(self.player, self.minus_block_list, True):
            SCORE -= 1
            self.block.reset_pos()
            create_block(RED, self.minus_block_list)

def create_block(color,block_list):
    block = Block(color, block_width, block_height)
    block.reset_pos()
    block_list.add(block)
    everything.all_sprites_list.add(block)
    
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SPEED = 1
SCORE = 0
FPS = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))

block_width, block_height = 20, 15
 
font = pygame.font.SysFont('serif', 25)

everything = Everything()
done = False
lost_menu = False
restart = True
clock = pygame.time.Clock()

while restart:
    done = False
    lost_menu = False
    SCORE = 0
    while not done:
        clock.tick(FPS)
        screen.fill(WHITE)
        everything.all_sprites_list.update()

        everything.check_collide()

        everything.all_sprites_list.draw(screen)

        text_score = font.render(f"Score : {SCORE}", True, BLACK)
        screen.blit(text_score, (10, 10))

        if SCORE < 0:
            lost_menu = True

        while lost_menu:
            screen.fill(WHITE)
            text_lost = font.render("YOU LOST",True, BLACK)
            text_restart = font.render("PRESS R TO RESTART", True, BLACK)
            screen.blit(text_lost, (WIDTH//2 - 70, HEIGHT//2 - 40))
            screen.blit(text_restart, (WIDTH//2 - 130, HEIGHT//2))
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    restart = False
                    lost_menu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        done = True
                        lost_menu = False
                        everything.create()
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                restart = False
        pygame.display.flip()
    pygame.display.flip()
pygame.quit()