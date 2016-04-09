from Block import *
from Transaction import *
from User import *


def main():
    block = Block()
    transaction = Transaction()
    block_user = User()
    running = True

    user_id = block_user.sign_in()

    while running:
        if user_id < 11:
            print("You are an admin. Welcome to the admin page")
            break
        else:
            print("Welcome to the main menu")
            print("1) Create a transaction")
            print("2) Check on the blockchain")
            print("3) look at my account")
            print("Enter the number or word associated with what you want to do "
                  "(i.e. transaction, blockchain, or account")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            us_input = input("What would you like to do: ")
            us_input = us_input.lower()

            if us_input == "exit" or us_input == "done":
                running = False
            elif us_input == "1" or us_input == "transaction":
                transaction.candidate_list()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif us_input == "2" or us_input == "blockchain":
                block.block_size()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif us_input == "3" or us_input == "account":
                block_user.handshake()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                print("Please enter a valid input")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("Byebye")

main()