from src.database import db
from sqlalchemy.types import PickleType


class QuizModel(db.Model):
    __tablename__ = 'quizzes'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    questions = db.Column(PickleType, nullable=False)

    def __init__(self, title, questions):
        # Initialize the model with title and questions
        self.title = title
        self.questions = questions

    def save(self):
        # Save the quiz to the database
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_quiz(cls, quiz_id):
        # Retrieve a quiz by its ID
        return cls.query.get(quiz_id)
