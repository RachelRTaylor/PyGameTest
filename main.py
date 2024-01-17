import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([300, 200])
pth = r'C:\Users\rache\OneDrive\Documents\pixcel art\thing2.png'
bg = pygame.image.load(pth)


# Run until the user asks to quit
x = 150
y = 100
running = True
speed = 0
while running:
    screen.blit(bg, (0, 0))
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed -= 0.01
            if event.key == pygame.K_RIGHT:
                speed += 0.01
    x += speed
    if x < 0:
        speed = 0
    if x > 300:
        speed = 0



    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 25)

    # Flip the display
    pygame.display.flip()
pygame.quit()
