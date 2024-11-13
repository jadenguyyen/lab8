from src.models.quiz_model import QuizModel


class QuizService:
    def create_quiz(self, quiz_data):
        title = quiz_data.get("title")
        questions = quiz_data.get("questions")

        # Create a new QuizModel instance
        quiz = QuizModel(title=title, questions=questions)

        # Save the quiz and return its ID
        quiz.save()
        return quiz.id

    def get_quiz(self, quiz_id):
        # Retrieve a quiz by its ID using the model
        return QuizModel.get_quiz(quiz_id)

    def evaluate_quiz(self, quiz_id, user_answers):
        # Retrieve the quiz by its ID
        quiz = self.get_quiz(quiz_id)

        # Check if the quiz exists
        if quiz is None:
            return None, "Quiz not found"

        # Calculate the score based on correct answers
        correct_answers = [q["answer"] for q in quiz.questions]
        score = sum(
            1 for correct, user in zip(correct_answers, user_answers) if correct == user
        )
        return score, "Quiz evaluated successfully"
