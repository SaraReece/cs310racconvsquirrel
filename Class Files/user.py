class user():
    def __init__(self, userName):
        import json
        filename = "Class Files/test.json"
        self.userName = userName
        self.userScore = 0
        self.combined = userName + " Score: " + str(self.userScore)

        #CreateUserName
        #json_object = json.dumps(self.combined)
        entry = {'user': userName, 'score': self.userScore}

        with open(filename, "r") as file:
            file_data = json.load(file)
            file_data.append(entry)
        with open(filename, "w") as file:
            json.dump(file_data, file)

    def updateUserData(self, score):
        self.userScore = score

#Debugging and testing
name = "Marissa"
newuser = user(name)
newuser.updateUserData(100)

print(f"Hello {newuser.userName}")
print(f"Your score is: {newuser.userScore}")