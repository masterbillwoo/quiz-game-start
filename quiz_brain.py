class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.temp = 0
        self.score = 0
        for i in self.questions_list:
            self.temp += 1

    def still_has_questions(self):
        if self.question_number < self.temp:
            return True
        else:
            return False

    def check_answer(self, userAnswer, realAnswer):
        if userAnswer.lower() == realAnswer.lower():
            print("correct answer")
            self.score += 1
        else:
            print("wrong answer")
        print(f"your current score is {self.score}")
        print(f"correct answer is {realAnswer}")


    def next_question(self):
        userAnswer = input(f"{self.questions_list[self.question_number].text} true or false")
        temp1 =  self.questions_list[self.question_number].answer
        self.check_answer(userAnswer, temp1)
        self.question_number += 1