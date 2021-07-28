import pygame, sys, random
run = True
SPEED = 1
SCORE = 0
screen_width = 800
screen_heigh = 600
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_heigh))
background = pygame.image.load("starfield.webp")
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('serif', 25)


class Block(pygame.sprite.Sprite):
    
    def __init__(self,picture_path):
        super().__init__()
        global SCORE
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("gun-gunshot-02.wav")
        self.score = SCORE
    def shoot(self):
        global SCORE,run,meteor_group,target_group
        self.gunshot.play()
        for target in target_group:
            if pygame.sprite.spritecollide(block,target_group,True):
                self.score += 1
        for meteor in meteor_group:
            if pygame.sprite.spritecollide(block,meteor_group,True):
                self.score -= 1
                if(self.score < 0):
                    run = False
                    print("LOST")
        create_star()
        create_meteor()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, x_pos, y_pos):
        super().__init__()
        self.path = picture_path
        self.x,self.y = x_pos,y_pos - 1000
        self.image = pygame.image.load(self.path)
        self.surf = pygame.Surface(self.image.get_size())
        center = (self.x, self.y)
        self.rect = self.surf.get_rect(center = center)    
    def draw(self):
        global SPEED
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > screen_heigh + 10):
            self.rect.center = (self.x, self.y)

def create_star():
    new_target = Target("star.png", random.randrange(15,screen_width),random.randrange(0,screen_heigh))
    target_group.add(new_target)
def create_meteor():
    new_target = Target("meteor.png", random.randrange(15,screen_width),random.randrange(0,screen_heigh))
    meteor_group.add(new_target)

block = Block("target.png")
block_group = pygame.sprite.Group()
block_group.add(block)
target_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()


clock.tick(10)
for _ in range(50):
    create_star()
for _ in range(10):
    create_meteor()

while run:
    scores = font.render(f"Score {block.score}",True,(255,255,255))
    screen.blit(background,(0,0))
    target_group.draw(screen)
    meteor_group.draw(screen)
    block_group.draw(screen)
    block_group.update()
    screen.blit(scores,(10,10))
    
    for tgt in target_group:
        tgt.draw()
    for meteor in meteor_group:
        meteor.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==  pygame.MOUSEBUTTONDOWN:
            block.shoot()

    pygame.display.flip()
