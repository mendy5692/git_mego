class Instegram:
    count = 0
    count_follow = 0
    def __init__(self, user_name, user_id):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0
        Instegram.count += 1

    def follow(self, frind_name):
        self.following += 1
        frind_name.followers += 1
        Instegram.count_follow += 1

def check(name):
    if name.lower() == "user1":
        return user1
    elif name.lower() == "user2":
        return user2
    elif name.lower() == "user3":
        return user3
    else:
        return "error"

user1 = Instegram("mendy", 111111111)
user2 = Instegram("yossi", 222222222)
user3 = Instegram("moty", 333333333)

continue_Y_N = "yes"

while continue_Y_N.lower()[0] == "y":
    you = check(input("\nEnter your name: (user1/user2/user3)"))
    frind = check(input("Enter a frind name: (user1/user2/user3)"))

    if you == "error" or frind == "error":
        continue

    you.follow(frind)

    print(f"user1 = following:{user1.following}, followers:{user1.followers}")
    print(f"user2 = following:{user2.following}, followers:{user2.followers}")
    print(f"user3 = following:{user3.following}, followers:{user3.followers}")

    continue_Y_N = input("\nDo you want to add another follower? (yes/no) ")

print(f"{Instegram.count}")
print(Instegram.count_follow)