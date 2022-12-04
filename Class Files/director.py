import pygame
from visual import Visual
from sys import exit
import os

# Start the PyGame module.
pygame.init()


class Director():

    def __init__(self):
        """Constructs a new instance of the Director class. Facilitates
        the game of "Raccoon VS Squirrel"

        Args:
            self (Director): An instance of Director.
            screen_width: The display's width.
            screen_height: The display's height.
            visuals: The list of Visual objects that the Director
                should be displaying.
            clock: A PyGame Clock object used to regulate framerate.
        """
        self.screen_width = 412
        self.screen_height = 732
        self.visuals = []
        # Create a "Clock" object to regulate the "game's" fps.
        self.clock = pygame.time.Clock()
        self.background_image_location = "background.png"
        self.background = pygame.image.load(self.background_image_location)


    def main(self):
        """
        The main function of the Director class. Facilitates the gameplay loop.
        """
        # Create Test Display Surface and caption it.
        window = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Raccoon VS Squirrel")

        # Create example objects.
        # TODO: Remove from final product.
        self.create_test_objects()

        # The gameplay loop. Loops until the player closes
        # the window.
        while True:

            # If the user clicks the "X" button at the top of
            # the window, close the window.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Display background image.
            window.blit(self.background, (0, 0))

            # Draw the visuals in the window.
            for i in self.visuals:
                i.display(window)

            # Check to see if the visuals in the window
            # need to do anything.
            for i in self.visuals:
                i.do_stuff()

            # Update the window.
            pygame.display.update()

            # Run the "game" at 60 fps.
            self.clock.tick(60)


    def create_test_objects(self):
        """
        A method to create objects for testing the Director class.
        """
        # Create a "Visual" object to test and add it
        # to the "visuals" list.
        visual = Visual("Does Nothing", 300, 100, 50, 50, "Red")
        self.visuals.append(visual)

        # Create an interactive "Visual" object to testand
        # add it to the "visuals" list.
        button = Visual("Does Something", 300, 100, 50, 550, "Green", True)
        self.visuals.append(button)


# Create an instance of Director and call the "Main" function.
director = Director()
director.main()