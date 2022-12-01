class user():
    def __init__(self, userName):
        self.userName = userName
        self.userScore = 0

    def createUserName(self, userName):
        import json
        filename = "Class Files/test.json"

        entry = "<" + userName + ">: {" + str(self.userScore) + "}"
        print(entry)
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

        self.userScore = score

        entry = {'score': score}
        #open the file and read it
        with open(filename, "r") as file:
            file_data = json.load(file)
            for x in file_data:
                print(x)
                print(json.dumps(x).strip())
                if json.dumps(x).strip() == "<" + name + ">":
                    file_data[x + 1] = entry
                else:
                    print("nope")

        #write the new info to the file
        with open(filename, "w") as file:
            json.dump(file_data, file)


#Debugging and testing
name = "Marissa"
newuser = user(name)
#newuser.createUserName(name)
newuser.updateUserData(100, name)

print(f"Hello {newuser.userName}")
print(f"Your score is: {newuser.userScore}")