def main():
    hello()
    name = input("Hva er navnet ditt? ")
    hello(name)



def hello(x = "world"):
    print("hello ", x)

main()