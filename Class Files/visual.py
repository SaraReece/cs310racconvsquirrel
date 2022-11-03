import pygame
from sys import exit

# Start the PyGame module.
pygame.init()


class Visual():

    def __init__(self, text, width, height, position_x, position_y, color, function=False):
        """Constructs a new instance of the Visual class. The Visuals
        can either be non-functional and serve only an aesthetic purpose
        or they can have a function.

        Args:
            self (Visual): An instance of Visual.
            text: The text that will be displayed on the visual.
            width: The width (or length) of the visual in pixels.
            height: The height of the visual in pixels.
            position_x: The x-coordinate of the position that the
                visual will be rendered in the window.
            position_y: The y-coordinate of the position that the
                visual will be rendered in the window.
            color: The background color of the visual.
            function: Whether or not the visual serves a purpose.
                Defaults to False.
        """
        self.width = width
        self.height = height
        # Create a PyGame Surface object using the
        # provided width and height.
        self.surface = pygame.Surface((self.width, self.height))
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.text = text
        # Calculate where the x-coordinate of the text whould be.
        self.text_position_x = position_x + 20
        # Calculate where the y-coordinate of the text whould be.
        self.text_position_y = position_y + (height / 3.5)
        # Set the font of the Visual object.
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.function = function


    def render_text(self, text):
        """
        Creates a second PyGame surface object to place text on
        top of initial Visual surface and returns it.
        """
        text_surface = self.font.render(text, False, (0, 0, 0))
        return text_surface


    def display(self, window):
        """
        Fills the surface with it's color and draws the surface
        and it's text in the window.
        """
        self.surface.fill(self.color)
        window.blit(self.surface, (self.position_x, self.position_y))
        window.blit(self.render_text(self.text), (self.text_position_x, self.text_position_y))


    def do_stuff(self):
        """
        This function is called so the Visual does something if it
        is clicked on.
        """
        # If the mouse is being pressed...
        if pygame.mouse.get_pressed()[0]:
            # If the visual is functional...
            if self.function:
                # If the mouse is over the visual...
                if pygame.mouse.get_pos():
                    # DO STUFF!
                    pygame.quit()
                    exit()







#========== TEST THE VISUAL CLASS ==========#

# Create Test Display Surface and caption it.
window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Visual/Button Class Test")

# Create a list to hold the Visuals in that are in the window.
visuals = []

# Create a "Clock" object to regulate the "game's" fps.
clock = pygame.time.Clock()

# Create a "Visual" object to test and add it
# to the "visuals" list.
visual = Visual("Does Nothing", 300, 100, 50, 50, "Red")
visuals.append(visual)

# Create an interactive "Visual" object to testand
# add it to the "visuals" list.
button = Visual("Does Something", 300, 100, 50, 200, "Green", True)
visuals.append(button)

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
    for i in visuals:
        i.display(window)

    # Check to see if the visuals in the window
    # need to do anything.
    for i in visuals:
        i.do_stuff()

    # Update the window.
    pygame.display.update()

    # Run the "game" at 60 fps.
    clock.tick(60)
