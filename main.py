from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for i in question_data:
    ztext = i["question"]
    zanswer = i["correct_answer"]
    zquestion = Question(ztext, zanswer)
    question_bank += [zquestion]

newquizbrain = QuizBrain(question_bank)


print(question_bank[1].answer)
print(newquizbrain.temp)
while newquizbrain.question_number < newquizbrain.temp:
    newquizbrain.next_question()
    #print(newquizbrain.question_number)
print("You've compelteted the quiz")
print(f"your final score is {newquizbrain.score}/{newquizbrain.temp}")

print("test")


#print(question_bank[0].text)

