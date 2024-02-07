import pygame

class BirdSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(BirdSprite, self).__init__()
        # adding all the images to sprite array
        self.images_r = []
        self.images_r.append(pygame.image.load('images/Bird R 1.png'))
        self.images_r.append(pygame.image.load('images/Bird R 2.png'))
        self.images_r.append(pygame.image.load('images/Bird R 3.png'))
        self.images_r.append(pygame.image.load('images/Bird R 4.png'))
        self.images_r.append(pygame.image.load('images/Bird R 5.png'))
        self.images_r.append(pygame.image.load('images/Bird R 6.png'))
        self.images_r.append(pygame.image.load('images/Bird R 7.png'))
        self.images_r.append(pygame.image.load('images/Bird R 8.png'))

        self.images_l = []
        self.images_l.append(pygame.image.load('images/Bird L 1.png'))
        self.images_l.append(pygame.image.load('images/Bird L 2.png'))
        self.images_l.append(pygame.image.load('images/Bird L 3.png'))
        self.images_l.append(pygame.image.load('images/Bird L 4.png'))
        self.images_l.append(pygame.image.load('images/Bird L 5.png'))
        self.images_l.append(pygame.image.load('images/Bird L 6.png'))
        self.images_l.append(pygame.image.load('images/Bird L 7.png'))
        self.images_l.append(pygame.image.load('images/Bird L 8.png'))

        self.images = self.images_r

        # index value to get the image from the array
        # initially it is 0
        self.index = 0
        self.direction = 0  # 0 for still, -1 for left, +1 for right

        # now the image that we will display will be the index from the image array
        self.image = self.images[self.index]

        # creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
        self.x = 5
        self.y = 125
        self.size_x = 64
        self.size_y = 64
        self.rect = None
        self.update_rect()

    def left(self):
        if self.direction in [1, -1]:
            self.image = self.images[0]
            self.index = 0
            self.direction = 0
        elif self.direction == 0:
            self.images = self.images_l
            self.image = self.images[0]
            self.direction = -1

    def right(self):
        if self.direction in [1, -1]:
            self.image = self.images[0]
            self.index = 0
            self.direction = 0
        elif self.direction == 0:
            self.images = self.images_r
            self.image = self.images[0]
            self.direction = 1

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.x + self.size_x, self.y + self.size_y)

    def update(self):
        self.x += self.direction
        if self.direction != 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        self.update_rect()


def main():
    pygame.init()

    screen = pygame.display.set_mode([300, 200])
    pth = r'images/In the style of.png'
    bg = pygame.image.load(pth)
    screen.blit(bg, (0, 0))

    my_sprite = BirdSprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    my_sprite.left()
                if event.key == pygame.K_RIGHT:
                    my_sprite.right()

        my_group.update()
        screen.blit(bg, (0, 0))
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()

# pygame.init()
#
# # Set up the drawing window
# screen = pygame.display.set_mode([300, 200])
# pth = r'C:\code\GitHub\PyGameTest\Background.png'
# bg = pygame.image.load(pth)
#
#
# # Run until the user asks to quit
# x = 150
# y = 100
# running = True
# speed = 0
# while running:
#     screen.blit(bg, (0, 0))
#     # Did the user click the window close button?
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 speed -= 0.01
#             if event.key == pygame.K_RIGHT:
#                 speed += 0.01
#     x += speed
#     if x < 0:
#         speed = 0
#     if x > 300:
#         speed = 0
#
#
#
#     # Draw a solid blue circle in the center
#     pygame.draw.circle(screen, (0, 0, 255), (x, y), 25)
#
#     # Flip the display
#     pygame.display.flip()
# pygame.quit()
