import pygame, sys, random

class Block(pygame.sprite.Sprite):
    def __init__(self,picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("C:/Users/Admin/Desktop/pygame/gun-gunshot-02.wav")
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(block,target_group,True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]


pygame.init()
clock = pygame.time.Clock()


screen_width = 800
screen_heigh = 600
screen = pygame.display.set_mode((screen_width,screen_heigh))
background = pygame.image.load("C:/Users/Admin/Desktop/pygame/starfield.webp")
pygame.mouse.set_visible(False)


block = Block("C:/Users/Admin/Desktop/pygame/target.png")
block_group = pygame.sprite.Group()
block_group.add(block)

target_group = pygame.sprite.Group()
for target in range(50):
    new_target = Target("star.png", random.randrange(0,screen_width),random.randrange(0,screen_heigh))
    target_group.add(new_target)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==  pygame.MOUSEBUTTONDOWN:
            block.shoot()
            
    pygame.display.flip()
    screen.blit(background,(0,0))
    target_group.draw(screen)
    block_group.draw(screen)
    block_group.update()
    clock.tick(60)

