from Packages.Connection import get_updates ,get_last_update_id
from Packages.Database import check_database, create_database
from Packages.Decision import decision_making
#from Packages. import *
#from Packages. import *
#from Packages. import *
#from Packages. import *
#from Packages. import *
#from Packages. import *

def main():
    last_update_id = None
    if check_database() == False:
        create_database()
    while True:
        getUpdates = get_updates(last_update_id)
        if getUpdates is not None:
            if len(getUpdates["result"]) > 0:
                last_update_id = get_last_update_id(getUpdates) + 1
                decision_making(getUpdates)

if __name__ == '__main__':
    print("You are now connected to telegram bot!")
    print("And you can stop bot with: ((ctrl+c))")
    print("Good luck!")
    main()
