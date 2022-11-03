class user():
    def __init__(self, userName):
        import json
        self.userName = userName
        self.userScore = 0
        self.combined = userName + " Score: " + str(self.userScore)

        #CreateUserName
        json_object = json.dumps(self.combined, indent=4)

        with open("Class Files/test.json", "w") as outfile:
            outfile.write(json_object)

    def updateUserData(self, score):
        self.userScore = score

#Debugging and testing
name = "Joseph"
newuser = user(name)
newuser.updateUserData(100)

print(f"Hello {newuser.userName}")
print(f"Your score is: {newuser.userScore}")