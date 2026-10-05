import pygame
import math
import random

pygame.init()
BULLET_SPEED = 10
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


class Player:

    def __init__(self):
        self.pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
        self.is_dead = False

    @property
    def x(self):
        return self.pos.x
    
    @x.setter
    def x(self, value):
        self.pos.x = value
    
    @property
    def y(self):
        return self.pos.y
    
    @y.setter
    def y(self, value):
        self.pos.y = value

    def draw(self, surf):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.pi / 2
        if mouse_y < self.y:
            angle = -math.pi / 2
        if mouse_x != self.x:
            angle = math.atan( (mouse_y - self.y) / (mouse_x - self.x))
        if mouse_x < self.x:
            angle += math.pi
        pts = [
            (self.x + 15 * math.cos(angle), self.y + 15 * math.sin(angle)),  # top of spaceship
            (self.x + 10 * math.cos(angle + math.pi * 2 / 3), self.y + 10 * math.sin(angle + math.pi * 2 / 3)),  # wing 1
            (self.x, self.y),
            (self.x + 10 * math.cos(angle - math.pi * 2 / 3), self.y + 10 * math.sin(angle - math.pi * 2 / 3)),  # wing 2
        ]
        pygame.draw.polygon(surf, 'green', pts)

    def shoot(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        b = Bullet(self.x, self.y)
        b.target(mouse_x, mouse_y)
        return b

    def move(self):  #homework
        pressed = pygame.key.get_pressed()
        vx = pressed[pygame.K_d] - pressed[pygame.K_a]
        vy = pressed[pygame.K_s] - pressed[pygame.K_w]
        speed = pygame.Vector2(vx, vy)
        if speed.magnitude() > 0:
            self.pos += 2 * speed.normalize()

    def die(self):
        self.is_dead = True


class Bullet:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_v = 0
        self.y_v = 0

    def target(self, x, y):
        d = dist((self.x, self.y), (x, y))
        if d != 0:
            self.x_v = BULLET_SPEED * (x - self.x) / d
            self.y_v = BULLET_SPEED * (y - self.y) / d
            self.x += 5 * (x - self.x) / d
            self.y += 5 * (y - self.y) / d
        else:
            self.x_v = BULLET_SPEED
            self.y_v = 0

    def update(self):
        self.x += self.x_v
        self.y += self.y_v

    def draw(self, surf):
        pygame.draw.circle(surf, 'red', (self.x, self.y), 3)

    def is_dead(self):
        return self.x < -3 or self.x > WIDTH + 3 or self.y < -3 or self.y > HEIGHT + 3


bullets = []
players = [Player() for i in range(100)]
for player in players:
    player.x = random.randint(0, WIDTH)
    player.y = random.randint(0, HEIGHT)

clock = pygame.time.Clock()

running = True

print(players)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))



    if pygame.mouse.get_just_pressed()[0] or pygame.key.get_pressed()[pygame.K_SPACE]:
        for player in players:
            bullets.append(player.shoot())
    for bullet in bullets:
        bullet.update()
        for p in players:
            if dist((p.x, p.y), (bullet.x, bullet.y)) <= 10:
                print("COLLIDE")
                p.die()
        bullet.draw(screen)
    for player in players:
        player.move()
        player.draw(screen)

    bullets = [b for b in bullets if not b.is_dead()]
    players = [p for p in players if not p.is_dead]
    pygame.display.flip()

    clock.tick(60)
    

pygame.quit()