secret_word = "bob"
guess = " "
guess_count: int = 0
guess_limit = 10
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
      guess = input("enter guess: ")
      guess_count +=  1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("you are out, LOSER!")
else:
    print("you win!")