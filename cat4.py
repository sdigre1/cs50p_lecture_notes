def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("How many meows?!"))
        if n > 0:
            return n
        
def meow(n):
    for i in range(n):
        print("meow")


#videoen lecture 2 er på 34:46