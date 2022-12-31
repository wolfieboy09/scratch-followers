from scratchclient import ScratchSession
from sys import exit

followerNumber = 0

session = ScratchSession("BotTest0910", "Barbarsnarf")

while True:
    try:
        print(session.get_user("SomeoneOnThelnternet").get_followers()[followerNumber].username)
        followerNumber = followerNumber + 1
     except Exception as e:
        exit(f"Error: {e}")
