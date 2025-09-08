import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player vs Enemies")

clock = pygame.time.Clock()
FPS = 60

score = 0
font = pygame.font.SysFont(None, 36)

background = pygame.image.load("bla.jpeg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

pygame.mixer.music.load("bro what.mp3")
pygame.mixer.music.play(-1)
hit_sound = pygame.mixer.Sound("hit.wav")

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        x = random.randint(0, WIDTH - 40)
        y = random.randint(0, HEIGHT - 40)
        self.rect = self.image.get_rect(topleft=(x, y))

player = Player("idk.jpeg")
player_group = pygame.sprite.Group(player)

enemies = pygame.sprite.Group()
for _ in range(7):
    enemies.add(Enemy("eney.png"))

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    hits = pygame.sprite.spritecollide(player, enemies, dokill=True)
    if hits:
        hit_sound.play()
        score += len(hits)

    screen.blit(background, (0, 0))
    player_group.draw(screen)
    enemies.draw(screen)

    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
