

Command_from_users=""
while True:
    Command_from_users=input(":").lower()
    if Command_from_users=="start":
        print("Car started")
    if Command_from_users=="stop":
        print("Car stoped")
    if Command_from_users=="help":
        print("""
    start_to start the car
    stop_ to stop the car
    quit_ to quit""" )
    if Command_from_users=="quit":
        break 
    else:
        print("I don't understand that!")
        
