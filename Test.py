
## Calculating probability of events
# Sample Space
num_cards = 52
# Favorable Outcomes
num_aces = 4
num_hearts = 13
num_diamonds = 13
# Divide favorable outcomes by the total number of elements in the sample space
prob_ace = num_aces / num_cards
prob_red_card = (num_hearts+ num_diamonds) / num_cards
# Print probability rounded to two decimal places
print("The probability of getting an ace =", round (prob_ace, 3))
print("The probability of getting a red card =", round (prob_red_card, 3))
# to print the probability in percentage
prob_ace_percent= prob_ace * 100
prob_red_percent= prob_red_card * 100
print("\nThe probability of getting an ace in percentage =", str(round(prob_ace_percent, 1)) + '%')
print('The probability of getting a red card in percentage =', str(round(prob_red_percent, 1)) + '%')

