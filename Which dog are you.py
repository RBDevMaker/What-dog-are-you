while True:
    try:

        canine_age = int(input("Which dog are you? (Enter your age): "))

        if 0 <= canine_age <=17:
            print ("You are a Puppy Chihuahua!")

        elif 18 <= canine_age <=21:
            print ("You are a Yorkie!")   

        elif 22 <= canine_age <=29:
            print ("You are a Poodle!")

        elif 30 <= canine_age <=39:
            print ("You are a Golden Retriever!")

        elif 40 <= canine_age <=49:
            print ("You are a Labrador Retriever!") 

        elif 50 <= canine_age <=59:
            print ("You are a German Shepard!") 

        elif 60 <= canine_age <=68:
            print ("You are a Pit Bull!")

        elif canine_age ==69:
            print ("You are a Atomic Dog!") 

        elif 70 <= canine_age <=79:
            print ("You are a Doberman!")

        elif 80 <= canine_age <=89:
            print ("You are a Service Dog!")

        elif 90 <= canine_age <=99:
            print ("You are a Retired Grey Hound!")

        elif canine_age ==100:
            print ("You are a Cane Corso!")                   

        else:
            print("Sorry, I can only categorize ages from 0 to 100.")
        
        # Ask again for age after displaying the category
        continue_input = input("Would you like to enter another age? (yes/no): ").lower()
        
        if continue_input != "yes":
        
            break
            
    except ValueError:
            print("Please enter a valid number for your age.")
    