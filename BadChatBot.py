name = input("Hello, what is your name? ")
print("Hi" + " " + name + ", my name is Mr. Chatbot.") 

color = input("What is your favorite color? ")
if color == "Blue":
    print("I also like blue.")
elif color == "blue":
      print("I also like blue.")
else:
    print(color + " " + "is okay")


sport = input("Do you like sports? ")
if sport == "yes":
    sports = input("Which ones? ")
    if sports == "Soccer":
        print("Soccer is very popular.")
    elif sports == "soccer":
        print("Soccer is very popular.")
    else:
     print("That's a great choice") 
elif sport == "Yes":
    sports = input("Which ones? ")
    if sports == "Soccer":
        print("Soccer is very popular.")
    elif sports == "soccer":
        print("Soccer is very popular.")
    else:
     print("That's a great choice")
else:
    hobby = input("How about one of your hobbies? ")
    print("Nice")

food = input("What is your favorite food? ")
if food == "pizza":
    print("Pizza is pretty awesome.")
elif food == "Pizza":
    print("Pizza is pretty awesome.")
else:
    print("I've heard good about " + food + ".")
   
    
if sport == "yes":
    print("So " + name + ", You enjoy " + sports + " and your favorite food is " + food + ".")
elif sport == "Yes":
     print("So, " + name + " You enjoy " + sports + " and your favorite food is " + food + ".")
else:
    print("So, " + name + " You enjoy " + hobby + " and your favorite food is " + food + ".")

print("Very interesting.")

print("Nice to meet you " + name + ".")
