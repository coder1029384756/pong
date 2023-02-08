from pygame import *

class ImageSprite(sprite.Sprite):
    def __init__(self, filename, size, pos):
        super().__init__()
        original_image = image.load(filename)
        self.image = transform.scale(original_image, size)
        self.rect = Rect(pos, size)
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
    def is_colliding_with(self, other_sprite):
        return sprite.collide_rect(self, other_sprite)
    
    # Any sub class of sprite.Sprite NEEDS to have a rect object and an image object
class RectSprite(sprite.Sprite):
    # Constructor: Function that runs only ONCE when a new object is created
    def __init__(self, color, pos, size):
        super().__init__() # Call the constructor of the super class
        self.rect = Rect(pos, size)
        self.image = Surface(size)
        self.image.fill(color)
    # Function to draw the rectangle
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft) 
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= 3
        if keys[K_DOWN]:
            self.rect.y += 3
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

WIDTH, HEIGHT = 1150, 670
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()

bat1 = RectSprite(color = (21,230,56), pos = (120, 335), size = (45, 100))

while not event.peek(QUIT):
    window.fill('lightblue')
    bat1.update()  
    bat1.draw(window)
    display.update()
    clock.tick(60)