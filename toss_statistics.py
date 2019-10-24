##  Get the number of toss..
def numberOfTosses():
    return input("How many times would you like to flip the coin? ")

##  Get the percentage of tossed head and tail..
def tossedPercentage(number_of_tosses, total_head, total_tail):
    heads_percentage = (total_head / number_of_tosses) * 100
    tails_percentage = (total_tail / number_of_tosses) * 100
    print("Percentage heads:", heads_percentage)
    print("Percentage tails:", tails_percentage)

##  Get the number of tossed head and tail..
def tossedNumber(total_head, total_tail):
    print("Number of heads:", total_head)
    print("Number of tails:", total_tail)

##  Start tossing...
def Tosses():
    head = 0
    tail = 0
    number_of_tosses = int(numberOfTosses())
    print('Please enter the outcome of each toss as "h" for heads or "t" for tails.')
    for x in range(number_of_tosses):
        clone = input(f"Toss { x + 1 }: ")
        ## Return a message if input is not valid
        if clone is not "h" and clone is not "t":
            print('Please enter the outcome of each toss as "h" for heads or "t" for tails.')
            clone = input(f"Toss { x + 1 }: ")

        if clone == "h":
            head += 1
        elif clone == "t":
            tail += 1
        else:
            print('Please enter the outcome of each toss as "h" for heads or "t" for tails.')
            clone = input(f"Toss { x + 1 }: ")
            
    return [number_of_tosses, head, tail] ## Return value on lists[]
    
def Main():
    tossed = Tosses()
    tossedPercentage(tossed[0], tossed[1], tossed[2])
    tossedNumber(tossed[1], tossed[2])


if __name__ == "__main__":
    Main()