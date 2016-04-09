'''
    Phil and Tom's COM492 Blockchain Research
    Transaction file
'''


class Transaction:
    def __init__(self):
        self.candidates = ["Cruz","Rubio","Trump","Clinton","Sanders"]
        self.vote = 0

    def candidate_list(self):
        print("1) See list - type 'see' or '1'")
        print("2) Edit List - type 'edit' or '2'")
        us_choice = input("What do you want to do: ")
        us_choice = us_choice.lower()

        # Would seperating by parties be helpful?

        if us_choice == "1" or us_choice == "see":
            self.print_candidates()

        # go through list and check user input in lowercase

        elif us_choice == "2" or us_choice == "edit":
            edit_choice = input("Would you like to add or remove: ")
            edit_choice = edit_choice.lower()

            if edit_choice == "add":
                new_name = input("What is the name of the candidate: ")
                new_name = new_name.lower().capitalize()
                list_ind = eval(input("Where do you want to enter this new candidate: "))
                self.candidates.insert(list_ind - 1, new_name)
                self.print_candidates()

            elif edit_choice == "remove":
                self.print_candidates()
                remove = input("Enter the name of the candidate or their number: ")
                if remove.isdigit():
                    remove = eval(remove) - 1
                    print("Removing: ", self.candidates.pop(remove))
                else:
                    remove = remove.lower().capitalize()
                    remove = self.candidates.index(remove)
                    print("Removing: ", self.candidates.pop(remove))
                self.print_candidates()

    def vote(self):
        print("Welcome to the voting menu")
        print("Who would you like to vote for?")
        self.print_candidates()
        us_vote = input("Enter the number of the candidate you want to vote for: ")
        self.vote = us_vote - 1

    def print_candidates(self):
        for i in range(len(self.candidates)):
            print(str(i + 1) + ":", self.candidates[i])
