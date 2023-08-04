#Ask user for their name. And make the name output pretty
name = input("What's your name? ").strip().title()

#Split user's name into frist name and last name 
first, last = name.split(" ")

#Say hello to user
print(f"hello, mr. {last}")
