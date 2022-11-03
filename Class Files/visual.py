import pygame
from sys import exit

# Start the PyGame module.
pygame.init()

class visual():

    def __init__(self, width, height, position_x, position_y):
        """Constructs a new instance of Die.

        Args:
            self (Die): An instance of Die.
        """
        self.width = width
        self.height = height
        self.surface = pygame.Surface((self.width, self.height))
        self.position_x = position_x
        self.position_y = position_y
        self.color = "Red"
        self.text = ""
        self.functional = False


    def display(self, window):

        self.surface.fill(self.color)
        window.blit(self.surface, (self.position_x, self.position_y))



#========== TEST CLASS ==========#

# Create Test Display Surface and caption it.
window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Visual/Button Class Test")

# Create a "Clock" object to regulate the "game's" fps.
clock = pygame.time.Clock()

# Create a "Visual" object to test.
visual = visual(100, 200, 0, 0)

# The gameplay loop. Loops until the player closes
# the window.
while True:

    # If the user clicks the "X" button at the top of
    # the window, close the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw the visuals in the window.
    visual.display(window)

    # Update the window.
    pygame.display.update()

    # Run the "game" at 60 fps.
    clock.tick(60)
