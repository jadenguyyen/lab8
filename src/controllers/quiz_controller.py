# src/controllers/quiz_controller.py
from flask import Blueprint, request, jsonify
from src.services.quiz_service import QuizService

quiz_bp = Blueprint('quiz', __name__, url_prefix='/api/quizzes')


@quiz_bp.route('', methods=['POST'])
def create_quiz():
    # Initialize an instance of QuizService
    service = QuizService()

    # Get JSON data from the request
    data = request.json

    quiz_id = service.create_quiz(data)

    return jsonify(
        {"message": "Quiz created", "quiz_id": quiz_id}
    ), 201


@quiz_bp.route('/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    # Initialize an instance of QuizService
    service = QuizService()

    # Call the `get_quiz` method with `quiz_id` and store the result in `quiz`
    quiz = service.get_quiz(quiz_id)

    # Check if the quiz exists and return a JSON response
    if quiz:
        quiz_dict = {
            "title": quiz.title,
            "questions": quiz.questions
        }
        return jsonify(quiz_dict), 200
    else:
        return jsonify({"error": "Quiz not found"}), 404


@quiz_bp.route('/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    # Initialize an instance of QuizService
    service = QuizService()

    # Get the answers from the request using `request.json.get('answers')`
    user_answers = request.json.get('answers')

    score, message = service.evaluate_quiz(quiz_id, user_answers)

    # Check if evaluation was successful and return the response
    if score is None:
        return jsonify({"error": "Quiz not found"}), 404
    else:
        return jsonify(
            {"score": score, "message": message}
        ), 200
