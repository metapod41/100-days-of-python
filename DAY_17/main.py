from question_bank import qb
from question_model import Question
from quiz_brain import QuizBrain

question_list = []

for questions in qb:
    qt = questions["text"]
    qa = questions["answer"]
    newQuestion = Question(qt,qa)
    question_list.append(newQuestion)

quiz = QuizBrain(question_list)
while(quiz.still_has_questions()):
    quiz.next_question()

print("YOU HAVE COMPLETED THE QUIZ")

print(f"YOUR FINAL SCORE WAS : {quiz.final_score()}/20")