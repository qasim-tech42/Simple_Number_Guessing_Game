


import random #We use random library for computer to generate  a random number for the user.
# Here you can guess a number between this interval.
computer_choice = random.randint(1,100)
while True:#The while loop is for repetition to repeat the the block of codes.
  try:# Try block is for invalid input.For example, a letter.
  
    user_choice = int(input("Guess a number 1-100: "))
    if user_choice == computer_choice:
      print("Correct!")
      #This part for continuing the loop.
      next_guess = input("Do you want to continue?(Yes/No) ".lower())
      if next_guess == 'no':
        print("You ended the program.\nThank you!") 
        break # When the answer is no the break terminate the loop.
    else:
      if user_choice > computer_choice:
        print("Too high")
      elif user_choice < computer_choice:
        print("Too low")
#It is a part of try block. It is a value error when you enter a letter instead of a number.         
  except ValueError:
    print("Invalid input!\nPlease enter a number.")
    
    