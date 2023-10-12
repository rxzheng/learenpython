score = 0
def correct():
    global score
    score += 1
    print("""Correct! 
    Score: """ + str(score))

def incorrect(answer):
    print("Incorrect! The answer was " + answer)

print("### QUIZ ###")
answer1 = input(""" What is the captial of Queensland?
a. Townsville
b. Brisbane
c. Noosa
answer: """)
if answer1 == "b":
    correct()
else:
    incorrect("b. Brisbane")

answer2 = input(""" In which Australian state is Birdsville found?
a. NSW
b. SA
c. QLD
answer: """)
if answer2 == 'c':
    correct()
else:
    incorrect("c. QLD")
