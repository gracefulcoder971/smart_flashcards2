def generate_quiz():
    # Simple static quiz for now
    questions = [
        {
            "id": "q1",
            "question": "What does NLP stand for?",
            "options": ["Natural Language Processing", "Neural Learning Program", "New Logic Protocol"]
        },
        {
            "id": "q2",
            "question": "Which algorithm is used in spaced repetition?",
            "options": ["Leitner System", "Bubble Sort", "Dijkstra's Algorithm"]
        }
    ]
    return questions
