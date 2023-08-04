def main():
    print_squares(3)

def print_squares(size):

    #For each firkant in the rows
    for i in range(size):
            
        #For each firkant in the line
        for j in range(size):
            print("#", end="")
            
        print("", end="\n")

main()