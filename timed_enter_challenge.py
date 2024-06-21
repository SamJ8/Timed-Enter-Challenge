from colorama import Fore, init
import time

print(Fore.GREEN + """
                                                                                                           

 ██╗ ██████╗     ███████╗███████╗ ██████╗ ██████╗ ███╗   ██╗██████╗      ██████╗██╗  ██╗ █████╗ ██╗     ██╗     ███████╗███╗   ██╗ ██████╗ ███████╗
███║██╔═████╗    ██╔════╝██╔════╝██╔════╝██╔═══██╗████╗  ██║██╔══██╗    ██╔════╝██║  ██║██╔══██╗██║     ██║     ██╔════╝████╗  ██║██╔════╝ ██╔════╝
╚██║██║██╔██║    ███████╗█████╗  ██║     ██║   ██║██╔██╗ ██║██║  ██║    ██║     ███████║███████║██║     ██║     █████╗  ██╔██╗ ██║██║  ███╗█████╗  
 ██║████╔╝██║    ╚════██║██╔══╝  ██║     ██║   ██║██║╚██╗██║██║  ██║    ██║     ██╔══██║██╔══██║██║     ██║     ██╔══╝  ██║╚██╗██║██║   ██║██╔══╝  
 ██║╚██████╔╝    ███████║███████╗╚██████╗╚██████╔╝██║ ╚████║██████╔╝    ╚██████╗██║  ██║██║  ██║███████╗███████╗███████╗██║ ╚████║╚██████╔╝███████╗
 ╚═╝ ╚═════╝     ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                                                                                                                   

                                                                                                           
""")

print(Fore.BLUE + "Test your skills with this game!\n".center(200))
print(Fore.BLUE + "Press enter twice and try to hit 10 seconds between each enter!".center(200))

while True:
    start = time.time()
    print("\n")
    print(Fore.GREEN+ "PRESS ENTER TO START: ".center(200))
    first_input = input(" ".center(100))
    print("\n")
    print(Fore.GREEN + "PRESS ENTER AGAIN: ".center(200))
    second_input = input(" ".center(100))

    end = time.time()

    elapsed = end-start

    print(Fore.MAGENTA + f"\nThat took you: {elapsed:.2f} seconds!")
    
    if elapsed <10:
        print(Fore.MAGENTA + "\nToo fast!")
    else:
        print(Fore.MAGENTA + "\nWow, that was just too slow!")


    replay = (input(Fore.GREEN + "\nWould you like to play again? Y/N? ".lower()))

    if replay != "y":
        break
