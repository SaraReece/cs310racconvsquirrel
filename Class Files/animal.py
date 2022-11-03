from PIL import Image
import glob

#continent name
c = "Antarctica"
#declare count variable
count = 0
# declare list to hold images
image_list = []
#declare list to hold file names
animal_name_list = []
#import images and get count
for filename in glob.glob('C:/Users/Sara Reece/Documents/GitHub/cs310racconvsquirrel/Animal Photos/Antarctica/*.png'): #all files should be .png
    #save image and then append it to the image list
    im=Image.open(filename)
    image_list.append(im)
    #parse out animal name from filename
    #declare substrings to get animal name we are using indexing and string slicing and replace to get the animal name geeks for geeks is awesome
    sub1 = ("/Animal Photos/" + c)
    sub2 = ".png"
    #create indexes to get name
    idx1 = filename.index(sub1)
    idx2 = filename.index(sub2)
    animalName = filename[idx1 + len(sub1) + 1: idx2]
    #take out hyphens
    animalName = animalName.replace("-", " ")
    #also append file name to animal name list
    animal_name_list.append(animalName)
    #increment count
    count += 1
# print count for TESTING*******************************************
print("Count: " + str(count) + "\n")
# a list to hold all of our animals
animal_list = []
# for loop to add in animal details
for x in range(count):
    animal_list.append({'name': animal_name_list[x], 'continent': c, 'image': image_list[x]})
# for loop to print animal details TESTING***********************
for x in animal_list:
    print("Name: " + x['name'])
    print("Continent: " + x['continent'])
    print("Image: \n")


