class user():
    def __init__(self, userName):
        self.userName = userName
        self.userScore = 0

    def createUserName(self, userName):
        import json
        filename = "Class Files/test.json"

        entry = []
        
        entry.append({'name': userName, 'score': self.userScore})

        #open the file and read it
        with open(filename, "r") as file:
            file_data = json.load(file)
            file_data.append(entry)

        #write the new info to the file
        with open(filename, "w") as file:
            json.dump(file_data, file)

    #update the score to an existing user
    def updateUserData(self, score, name):
        import json
        filename = "Class Files/test.json"
        counter = 1

        self.userScore = score

        entry = {'name': name, 'score': score}

        #open the file and read it
        with open(filename, "r") as file:
            file_data = json.load(file)
            

            for x in file_data:
                print(f"{counter}. {x}")
                counter += 1

            #select your name    
            number = int(input("Please choose save destination number: "))
            file_data[number - 1] = entry
            
        #write the new info to the file
        with open(filename, "w") as file:
            json.dump(file_data, file)


#Debugging and testing
name = input("Please enter your name: ")
newuser = user(name)
#newuser.createUserName(name)
newuser.updateUserData(100, name)

print(f"Hello {newuser.userName}")
print(f"Your score is: {newuser.userScore}")