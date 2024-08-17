# Rock, paper, scissors game project

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random

choices = [rock, paper, scissors]
# print()
player_input = input(
    "What do you choose? Type 0 for Rock, 1 for Paper ans 2 for Scissors.\n"
)
p_hit = int(player_input)
pc_hit = random.SystemRandom().choice(range(0, 3))
if p_hit > 2 or p_hit < 0:
    print("Wrong choice, try again.")
else:
    print(choices[int(player_input)])
    print(f"Computer chose: {choices[pc_hit]}")
    if p_hit == 0 and pc_hit == 2:
        print("You win")
    elif p_hit == 2 and pc_hit == 0:
        print("You lose")
    elif p_hit < pc_hit:
        print("You lose")
    elif p_hit > pc_hit:
        print("You win")
    elif p_hit == pc_hit:
        print("It's a draw")
