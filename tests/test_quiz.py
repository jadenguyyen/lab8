from unittest.mock import patch, MagicMock
from src.services.quiz_service import QuizService


# Test for creating a new quiz
@patch.object(QuizService, 'create_quiz')
def test_create_quiz(mock_create_quiz, client):
    mock_create_quiz.return_value = 1  

    response = client.post(
        '/api/quizzes',
        json={
            "title": "Sample Quiz",
            "questions": [
                {"text": "What is 2 + 2?", "answer": "4"},
                {"text": "What is the capital of France?", "answer": "Paris"}
            ]
        }
    )

    assert response.status_code == 201
    assert response.json["quiz_id"] == 1
    assert response.json["message"] == "Quiz created"
    mock_create_quiz.assert_called_once()


# Test for retrieving a quiz by ID
@patch.object(QuizService, 'get_quiz')
def test_get_quiz(mock_get_quiz, client):
    mock_quiz = MagicMock()
    mock_quiz.title = "Sample Quiz"
    mock_quiz.questions = [
        {"text": "What is 2 + 2?", "answer": "4"},
        {"text": "What is the capital of France?", "answer": "Paris"}
    ]

    mock_get_quiz.return_value = mock_quiz
    response = client.get('/api/quizzes/1')
    assert response.status_code == 200
    response_json = response.get_json()
    assert response_json['title'] == "Sample Quiz"
    assert response_json['questions'] == [
        {"text": "What is 2 + 2?", "answer": "4"},
        {"text": "What is the capital of France?", "answer": "Paris"}
    ]
    mock_get_quiz.assert_called_once_with(1)


# Test for submitting answers and evaluating a quiz
@patch.object(QuizService, 'evaluate_quiz')
def test_submit_quiz(mock_evaluate_quiz, client):
    mock_evaluate_quiz.return_value = (2, "Quiz evaluated successfully")

    response = client.post(
        '/api/quizzes/1/submit',
        json={"answers": ["4", "Paris"]}
    )

    assert response.status_code == 200
    assert response.json["score"] == 2
    assert response.json["message"] == "Quiz evaluated successfully"
    mock_evaluate_quiz.assert_called_once_with(1, ["4", "Paris"])
