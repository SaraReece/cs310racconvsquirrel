import pygame
from visual import Visual
from sys import exit
import json

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
            background_image_location: The file path to the location
                of the background image.
            background: The background image loaded into a useable
                PyGame 'Image' object.
            file_selected: A Boolean variable to track if the player
                has selected a file or not.
<<<<<<< Updated upstream
            current_player: A variable to hold the current player's number.
                If the player has not been selected yet, this string is
                empty.
            current_player_score: A variable to hold the current player's
                score. If the player has not been selected yet, this
                number is 0.
            
            
=======
            save_file_path: The file path to the json file containing
                player data.
            users: A Python dictionary obtained from 'save_files.json'.
            player_selected: A Boolean variable to track if a player has
                been selected.
            current_user: A variable to keep track of the current user.
            in_game: A Boolean variable to track if a continent has
                been selected.
            current_continent: The currently selected continent.
>>>>>>> Stashed changes
        """
        self.screen_width = 412
        self.screen_height = 732
        self.visuals = []
        # Create a "Clock" object to regulate the "game's" fps.
        self.clock = pygame.time.Clock()
        self.background_image_location = "background.png"
        self.background = pygame.image.load(self.background_image_location)
        self.save_file_path = "Class Files/save_files.json"
        self.users = self.load_users()
        self.player_selected = False
        self.current_user = ""
        self.in_game = False
        self.current_continent = ""


    def main(self):
        """
        The main function of the Director class. Facilitates the gameplay loop.
        """
        # Create Test Display Surface and caption it.
        window = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Raccoon VS Squirrel")

        # Create example objects.
        # TODO: Remove from final product.
        # self.create_test_objects()

        # Create the title at the top of the game.
        self.save_file_select_screen()

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

            # While the user has not selected a save file...
            if not self.player_selected:
                # Check to see if the save file select buttons
                # in the window need to do anything.
                for i in self.visuals:
                    self.player_selected = i.player_select_button()
                    # If one has been selected, get rid of the save
                    # file select buttons on screen.
                    if self.player_selected:
                        self.destroy_save_file_select_screen(i)
            # Otherwise the user has selected a save file.
            else:
                pass

            # Update the window.
            pygame.display.update()

            # Run the "game" at 60 fps.
            self.clock.tick(60)


    def load_users(self):
        # Open the file and read it.
        with open(self.save_file_path, "r") as file:
            users = json.load(file)
        # Return file data as Python dictionary.
        return users


    def save_file_select_screen(self):
        """
        Displays the first screen of the game to the player. This
        allows the player to select one of the three player files
        to use. This will either be an existing user, or a new
        'Empty' file.
        """
        # Create a "Visual" object to display the game's title at
        # the top of the screen.
        title_visual = Visual("Title", "Raccoon VS Squirrel", 300, 100, 56, 28, (184,180,156))
        self.visuals.append(title_visual)

        # Create "Visual" objects to display the game's save files
        # on screen. Get user scores from self.users.
        userOneScore = self.users[0]["userOne"]
        save_file_one = Visual("userOne", f"Player 1: {userOneScore} Pts", 300, 100, 56, 350, (184,72,120), True)
        self.visuals.append(save_file_one)
        userTwoScore = self.users[1]["userTwo"]
        save_file_two = Visual("userTwo", f"Player 2: {userTwoScore} Pts", 300, 100, 56, 475, (184,72,120), True)
        self.visuals.append(save_file_two)
        userThreeScore = self.users[2]["userThree"]
        save_file_three = Visual("userThree", f"Player 3: {userThreeScore} Pts", 300, 100, 56, 600, (184,72,120), True)
        self.visuals.append(save_file_three)


    def destroy_save_file_select_screen(self, i):
        """
        Gets rid of the buttons created by save_file_select_screen().
        """
        # Set self.current_user based on the user's selection.
        self.current_user = i.name
        # Log which player wax selected in the terminal.
        print(f"{self.current_user} was selected")
        # Delete everything but the title Visual in self.visuals.
        title = self.visuals[0]
        self.visuals.clear()
        self.visuals.append(title)


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