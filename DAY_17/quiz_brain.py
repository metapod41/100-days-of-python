class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.qlist = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number != len(self.qlist)

    def next_question(self):
        currq = self.qlist[self.question_number]
        self.question_number+=1
        ans = input(f"Q{self.question_number}. {currq.text}: ")
        self.check_ans(ans)

    def check_ans(self,ans):
        currr = self.qlist[self.question_number-1]
        answer = currr.answer
        if(ans.lower()==answer.lower()):
            print("YAYY! ITS A CORRECT ANSWER")
            self.score+=1
        else:
            print("OOPS! ITS A WRONG ANSWER")
            print(f"CORRECT ANSWER IS : {self.qlist[self.question_number-1].answer.lower()}")
        print(f"SCORE: {self.score}/{self.question_number}")

    def final_score(self):
        return self.score
        
