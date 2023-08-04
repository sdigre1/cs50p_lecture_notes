def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:   
        try:
            x = int(input(prompt))
        
        except ValueError:
            #pass  returnerer ikke linjen under, men tar seg av ValueError
            print("x is not an integer")
        else:
            """break"""    #this is not needed when return is used 
            return x

main()