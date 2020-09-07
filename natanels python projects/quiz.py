import time
from question import Question

question_prompts = [
    " What is the longest that an elephant has lived? (That we know of)\n (a) 17 years\n (b) 49 years\n (c) 86 years\n\n",
    " How many rings are on the Olympic flag?\n (a) none\n (b) 4\n (c) 5\n\n",
    " What is a tarsier?\n (a) A primate \n (b) A rodent\n (c) A lizard\n\n",
    " How did Spider-Man get his powers?\n (a) Military experiment gone awry\n (b) Bitten by a radioactive spider\n (c) Born with them\n\n",
    " In darts, what's the most points you can score with a single throw?\n (a) 20\n (b) 50\n (c) 60\n\n",
    " Which of these animals does NOT appear in the Chinese zodiac?\n (a) Bear\n (b) Rabbit\n (c) Dog\n\n",
    " Who are known as Brahmins?\n (a) Surfers in California\n (b) Nepali soldiers \n (c) Members of India's highest caste\n\n",
    " How many holes are on a standard bowling ball?\n (a) 2\n (b) 3\n (c) 5\n\n",
    " What are the main colors on the flag of Spain?\n (a) Black and yellow\n (b) Green and white\n (c) Red and yellow\n\n",
    " Who killed Greedo?\n (a) Hannibal Lecter\n (b) Han Solo\n (c) Luke Skywalker\n\n",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "c"),
    Question(question_prompts[9], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("correct")
            time.sleep(0.5)
        else:
            print("wronge")
            time.sleep(0.5)

    print("you got "+ str(score) +"/" + str(len(questions))+ " correct")

    int(score)

    if score >= 8:
        time.sleep(0.5)
        print("  you are a genius")
    elif score <= 3:
        time.sleep(0.5)
        print(" you are rubbish")
    elif score == 5 or score == 6 or score == 7 or score == 4:
        time.sleep(0.5)
        print("average score")


run_test(questions)











