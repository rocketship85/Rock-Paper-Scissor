#User enter his/her name (raw_input)
users_name = raw_input("What's your name?")
users_name = users_name.upper()

#A greeting and instructions display for user

print "Hello " + users_name + "!"
print "Rock breaks Scissors, Scissors cuts Paper, Paper beats Rock"
print "Select *R* for rock, *P* for paper, or *S* for scissors"

#storing the score

users_score = 0
computers_score = 0

#The computer chooses the random letter (R, P or S)

from random import choice

rock_paper_scissors = ["R", "P", "S"]

computers_choice = choice(rock_paper_scissors)


#User enter his/her item of choice (R, P or S)

users_choice = raw_input("Enter your choice:")
users_choice = users_choice.upper()

#If the user input is same as the random number, display the tie
while True:
	
	if users_choice == computers_choice:
	
		print users_name + " ,you chose ",users_choice
		print "Computer chose ",computers_choice
		print "Tie!"

#If the user input is rock and the computer choice is scissors, display that the user won
	
	elif users_choice == 'R' and computers_choice == 'S':
		print users_name + " ,you entered Rock. Computer had Scissor. Rock smashes Scissors. You win!"
#storing the score
		users_score = users_score + 1


#If the user input is rock and the computer choice is paper, display that the computer won

	elif users_choice == 'R' and computers_choice == 'P':
		print users_name + " ,you entered Rock. Computer had Paper. Paper covers Rock. You lose!"

#storing the score

		computers_score = computers_score + 1

#If the user input is paper and the computer choice is scissors, display that the user won

	elif users_choice == 'P' and computers_choice == 'S':
		print users_name + " ,you entered Paper. Computer had Scissors. Scissors cut Paper. You lose!"

#storing the score

		computers_score = computers_score + 1


	elif users_choice == 'P' and computers_choice == 'R':
		print users_name + " ,you entered Paper. Computer had Rock. Paper covers Rock. You win!"

#storing the score
		users_score = users_score + 1

	elif users_choice == 'S' and computers_choice == 'P':
		print users_name + " ,you entered Scissors. Computer had Paper. Scissors cut Paper. You win!"

#storing the score

		users_score = users_score + 1

	elif users_choice == 'S' and computers_choice == 'R':
		print users_name + " ,you entered Scissors. Computer had Rock. Rock smashes Scissors. You lose!"
#storing the score
		computers_score = computers_score + 1
	else:
		print "Invalid input! You have not entered rock(R), paper(P) or scissors(P), try again."


#winner

	if users_score == 5:
			 #Print computer wins the game
		print "Congratulations " + users_name + " ,you've reached 5 points! You win!"
		break
    #Provide proper conditions for elif in case user getting 5 points:
	else:
		#Congratulate the user on winning along with their name
		print users_name + " ,Computer's reached 5 points! You lose!"
		break



