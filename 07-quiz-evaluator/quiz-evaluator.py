import random

questions = [
    {"question": "What is the capital of India?", "options": {"a": "Mumbai", "b": "Delhi", "c": "Chennai", "d": "Kolkata"}, "answer": "b"},
    {"question": "Which language is used for web styling?", "options": {"a": "HTML", "b": "Python", "c": "CSS", "d": "Java"}, "answer": "c"},
    {"question": "2 + 2 * 2 = ?", "options": {"a": "8", "b": "6", "c": "4", "d": "2"}, "answer": "b"},
    {"question": "Which planet is known as the Red Planet?", "options": {"a": "Earth", "b": "Venus", "c": "Mars", "d": "Jupiter"}, "answer": "c"},
    {"question": "Who developed Python?", "options": {"a": "Guido van Rossum", "b": "James Gosling", "c": "Dennis Ritchie", "d": "Bjarne Stroustrup"}, "answer": "a"}
]

random.shuffle(questions)

score = 0
marks_per_question = 2
total_marks = len(questions) * marks_per_question
wrong_answers = []

for q in questions:
    print("\n" + q["question"])
    for key in q["options"]:
        print(key, ":", q["options"][key])

    user_answer = input("Your answer (a/b/c/d): ")

    if user_answer.lower() == q["answer"]:
        score = score + marks_per_question
    else:
        wrong_answers.append(q)

percentage = (score / total_marks) * 100

print("\n===== RESULT =====")
print("Score:", score, "/", total_marks)
print("Percentage:", percentage, "%")

if wrong_answers:
    print("\n----- Correct Answers for Wrong Ones -----")
    for q in wrong_answers:
        print(q["question"], "-> Correct answer:", q["answer"])