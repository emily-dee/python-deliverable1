# name = user's name
# game = 3 or 6
# hole_number = the hole the user is on currently
# hole_score = user's inputted score for a hole_number
# all_putts = a list of the inputted hole_number values
# final_count = number of putts
# par_score = the number of putts minus par for final score

name = input("Welcome to GC mini golf! What is your name? ")
game = input(f"Hi, {name}! Would you like to play 3 or 6 holes? ")
par = int(game) * 3

hole_number = 1
all_putts = []
while int(hole_number) <= int(game):
     hole_score = input(f"How many putts for hole {hole_number}? (par: 3) ")
     all_putts.append(int(hole_score))
     hole_number += 1

final_count = sum(all_putts)

par_score = int(final_count) - int(par)
if final_count == par:
     print(f"Good game, {name}. Your total score was: {par_score}")
elif final_count > par:
     print(f"Nice try, {name}... Your total score was: +{par_score}")
elif final_count < par:
     print(f"Great job, {name}! Your total score was: {par_score}")
else:
     print("error")