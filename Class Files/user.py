class user():
    def __init__(self):
        self.userScore = 0

    def createUserName(self):
        import json
        filename = "Class Files/save_files.json"
        userName = input("Please enter your name: ")

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
        filename = "Class Files/save_files.json"
        counter = 1

        self.userScore = score

        entry = {'name': name, 'score': score}

        #open the file and read it
        with open(filename, "r") as file:
            file_data = json.load(file)
            
            print("Thanks for playing!")
            for x in file_data:
                print(f"{counter}. {x}")
                counter += 1

            #select your name    
            number = int(input("Please choose save destination(1-9): "))
            file_data[number - 1] = entry
            
        #write the new info to the file
        with open(filename, "w") as file:
            json.dump(file_data, file)


    def loadUserName(self):
        import json
        filename = "Class Files/save_files.json"
        counter = 1
        nameCheck = False
        scoreCheck = False
        name = ""
        score = ""

        with open(filename, "r") as file:
            file_data = json.load(file)

        for x in file_data:
            print("Saved Users: ")
            print(f"{counter}. {x}")
            counter += 1

        load = int(input("Please choose your file save: "))
        strData = str(file_data[load - 1])
        i = 0
        count = 0
        for y in strData:
            if strData[i] == ":" and strData[i - 3] == "m":
                nameCheck = True
                count = i + 3
                i += 1
                while nameCheck:
                    for z in strData:
                        if strData[count] == "'":
                            nameCheck = False
                        else:
                            name += strData[count]
                            count += 1
            elif strData[i] == ":" and strData[i - 3] == "r":
                scoreCheck = True
                count = i + 2

                while scoreCheck:
                    for z in strData:
                        if strData[count] == "}":
                            scoreCheck = False
                        else:
                            score += (strData[count])
                            count += 1
                i += 1
                score = int(score)
            else:
                i += 1
        
        finalString = (f"Name: {name}, Score: {score}")

        return finalString
# #Debugging and testing

# #name = "Jason"
# newuser = user()
# #newuser.createUserName()
# newuser.updateUserData(500, "Eli")
# print("Successfully updated!")
# #loaded = newuser.loadUserName()
#print(f"Successfully loaded -> {loaded}")