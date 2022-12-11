from PIL import Image
import glob


class Animal():
    #constructor for the Animal class. Accepts the continent name from the user. Creates an empty list for all the animals. 
    def __init__(self):
        # a list to hold all of our animals
        self.animal_list = []    
    #Get animal list once it is set
    def getAnimalList(self):
        return self.animal_list
    #Set animal list based on the contents of the animal photo file
    def setAnimalList(self):
        #declare count variable
        count = 0
        # declare list to hold images
        image_list = []
        #declare list to hold file names
        animal_name_list = []
        #import images and get count
        for filename in glob.glob('Animal Photos/*.png'): #all files should be .png
            #save image path and then append it to the image list
            image_list.append(filename)
            #parse out animal name from filename
            #declare substrings to get animal name we are using indexing and string slicing and replace to get the animal name geeks for geeks is awesome
            sub1 = ("Animal Photos")
            sub2 = ".png"
            #create indexes to get name
            idx1 = filename.index(sub1)
            idx2 = filename.index(sub2)
            animalName = filename[idx1 + len(sub1) + 1: idx2]
            #take out hyphens
            animalName = animalName.replace("-", " ")
            #also append file name to animal name list
            animal_name_list.append(animalName.capitalize())
            #increment count
            count += 1
        # print count for TESTING*******************************************
        print("Animal Count: " + str(count) + "\n")
        # for loop to add in animal details
        for x in range(count):
            self.animal_list.append({'name': animal_name_list[x], 'image': image_list[x]})
        # for loop to print animal details TESTING***********************
        for x in self.animal_list:
            print("Name: " + x['name'])
            print("Image: " + x['image'] + "\n")


