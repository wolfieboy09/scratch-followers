from scratchclient import ScratchSession

followerNumber = 0

session = ScratchSession("BotTest0910", "Barbarsnarf")

while 3 == 3:
    print(session.get_user("SomeoneOnThelnternet").get_followers()[followerNumber].username)
    followerNumber = followerNumber + 1
