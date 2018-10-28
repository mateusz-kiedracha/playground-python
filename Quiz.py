#Simple quiz program with 10 question about Python basics.If user types answer program informs if it is correct or not.
#If user 'leaves' empty space and type enter, program will move on, but calculate to the answered questions.
#At the end, program shows how many answered questions user had, correct answers and wrong answers with percent' score.


good_answers = 0
wrong_answers = 0
answered = 0
without_answer = 0

input("Hello in my Python quiz!\nPress Enter to continue...")

#questions

question_1 = input("What kind of animal is \"Python\"? ")
if question_1.lower() == "snake":
    print ("Good answer!")
    good_answers += 1
    answered += 1
elif question_1 == "":
    without_answer += 1
else:
    print("Wrong answer!")
    wrong_answers += 1
    answered += 1

question_2 = input("What can be edited: tuple or list? ")
if question_2.lower() == "tuple":
    print ("Good answer!")
    good_answers +=1
    answered += 1
elif question_2 == "":
    without_answer += 1
else:
    print("Wrong answer!")
    wrong_answers += 1
    answered += 1

question_3 = input("Logical operators in Python are: 1)and 2)or 3)? ")
if question_3.lower() == "not":
    print ("Good answer!")
    good_answers +=1
    answered += 1
elif question_3 == "":
    without_answer += 1
else:
    print("Wrong answer!")
    wrong_answers += 1
    answered += 1

question_4 = input("What is the remainder of the division of left operand by the right? ")
if question_4.lower() == "modulo":
    print ("Good answer!")
    good_answers +=1
    answered += 1
elif question_4 == "":
    without_answer += 1
else:
    print("Wrong answer!")
    wrong_answers += 1
    without_answer += 1

question_5 = input("\"x += 5\" operator it is equal to x = x + 5? Type \"yes\" or \"no\" ")
if question_5.lower() == "yes":
    print ("Good answer!")
    good_answers +=1
    answered += 1
elif question_5 == "":
    without_answer += 1
else:
    print("Wrong answer!")
    wrong_answers += 1
    answered += 1

question_6 = input("Which loop in Python you will use to iterate over the whole e.g. list or tuple? ")
if question_6.lower() == "for":
    print ("Good answer!")
    good_answers +=1
    answered += 1
elif question_6 == "":
    without_answer += 1
else:
    print("Wrong answer!")
    wrong_answers += 1
    answered += 1

question_7 = input("What is the mark of exponent? ")
if question_7.lower() == "**":
    print ("Good answer!")
    good_answers +=1
    answered += 1
elif question_7 == "":
    without_answer += 1
else:
    print("Wrong answer!")
    wrong_answers += 1
    answered += 1

question_8 = input("If x=0 and y=0, so x!=y is false or true?")
if question_8.lower() == "false":
    print ("Good answer!")
    good_answers +=1
    answered += 1
elif question_8 == "":
    without_answer += 1
else:
    print("Wrong answer!")
    wrong_answers += 1
    answered += 1

question_9 = input("The newest version of Python 3 is: ?")
if question_9.lower() == "3.7.1":
    print ("Good answer!")
    good_answers +=1
    answered += 1
elif question_9 == "":
    without_answer += 1
else:
    print("Wrong answer!")
    wrong_answers += 1
    answered += 1

question_10 = input("Most powerfull IDE for Python is?")
if question_10.lower() == "pycharm":
    print ("Good answer!")
    good_answers +=1
    answered += 1
elif question_10 == "":
    without_answer += 1
else:
    print("Wrong answer!")
    wrong_answers += 1
    answered += 1

score_in_percent = (good_answers / 10) * 100

print ("You answered to " + str(answered)+(" questions"))
print ("Your score is " + str(good_answers) + " correct answers, " + "it means you got " + str(score_in_percent) +"%.")
print ("You got " + str(wrong_answers) + " wrong answers.")
