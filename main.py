# Simple Pong Game
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
dt = 0
# fill the screen with a color to wipe away anything from last frame
screen.fill("grey")

# Creates ball
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# Random initial direction
ball_velocity_x = random.choice([-1, 1]) * random.uniform(1, 3)
ball_velocity_y = random.choice([-1, 1]) * random.uniform(1, 3)

# Creates players
p1 = pygame.Rect(10, 220, 20, 60)
p2 = pygame.Rect(470, 220, 20, 60)

# Creates score
pygame.font.init() 
my_font = pygame.font.SysFont('Arial', 30)
p1v = 0
p2v = 0
p1s = my_font.render(str(p1v), False, (0, 0, 0))
p2s = my_font.render(str(p2v), False, (0, 0, 0))

# Runs Pong
while running:
    # Update ball position based on velocities
    ball_pos.x += ball_velocity_x
    ball_pos.y += ball_velocity_y
    # Check boundary conditions (screen edges)
    if ball_pos.x <= 10 or ball_pos.x >= 490:
        ball_velocity_x *= -1  # Reverse direction in x-axis
    if ball_pos.y <= 10 or ball_pos.y >= 490:
        ball_velocity_y *= -1  # Reverse direction in y-axis
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Ensure players stay within the screen bounds and move players
    pressed_keys = pygame.key.get_pressed()
    # Move player 1
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w] and p1.y > 0:
        p1.y -= 3  # Move up
    if pressed_keys[pygame.K_s] and p1.y < 440:
        p1.y += 3  # Move down
    # Move player 2
    if pressed_keys[pygame.K_UP] and p2.y > 0:
        p2.y -= 3  # Move up
    if pressed_keys[pygame.K_DOWN] and p2.y < 440:
        p2.y += 3  # Move down
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # ball
    ball = pygame.draw.circle(screen, "black", ball_pos, 10)

    # Reverse ball direction if it collides with p1 or p2
    if ball.colliderect(p1) or ball.colliderect(p2):
        ball_velocity_x *= -1  # Reverse direction in x-axis

    # Ball hits wall, update score
    if ball_pos.x <= 10:
        p2v += 1
        p2s = my_font.render(str(p2v), False, (0, 0, 0))  # Update score surface
        ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    if ball_pos.x >= 490:
        p1v += 1
        p1s = my_font.render(str(p1v), False, (0, 0, 0))  # Update score surface
        ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    screen.blit(p1s, (10,10))
    screen.blit(p2s, (470,10))

    # Draw player 1 and player 2 on the screen
    pygame.draw.rect(screen, "black", p1)
    pygame.draw.rect(screen, "black", p2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000
