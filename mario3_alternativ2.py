def main():
    print_squares(3)

def print_squares(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()