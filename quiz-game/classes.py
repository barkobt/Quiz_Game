class User:
    def __init__(self,user_id,name): # we have to use these init's when we're creating our objects.
        self.id = user_id
        self.name = name 
        self.followers = 0 # we set as zero, we don't actually have to initialize
        self.following = 0

    def follow(self,user): ## basic following method in for example instagram
        user.followers += 1
        self.following += 1



user_1 = User(440,"Barko")
user_2 = User(899,"Baran")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

