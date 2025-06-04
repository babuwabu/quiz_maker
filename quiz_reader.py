# import all things
import random

# load questions from file
def load_quiz(filename):
    """Loads questions from the quiz file."""
    questions = []

    with open(filename, "r") as file:
        content = file.read().split("::END::\n\n")  # Split questions
        for block in content:
            lines = [line.strip() for line in block.split("\n") if line.strip()]
        if len(lines) >= 7:
                q_data = {
                    "question": lines[1],
                    "choices": {
                        "a": lines[2][3:].strip(),
                        "b": lines[3][3:].strip(),
                        "c": lines[4][3:].strip(),
                        "d": lines[5][3:].strip(),
                    },
                    "answer": lines[6][-1].strip().lower()
                }
                questions.append(q_data)
    return questions

# load the quiz
quiz_filename = "quiz.txt"  # Change to match the actual filename
questions = load_quiz(quiz_filename)

if not questions:
    print("No questions found. Please check the file format.")
else:
    score = 0
    asked_questions = []

    while True:
        # Pick a new random question only if needed
        if len(asked_questions) == len(questions):  
            print("\n🎉 You've completed all questions! Final Score:", score, "/", len(questions))
            break

        current_question = random.choice(questions)
        while current_question in asked_questions:
            current_question = random.choice(questions)

        print("\n" + "=" * 50)
        print(f"📌 Question: {current_question['question']}")
        print("=" * 50)

        for key, value in current_question["choices"].items():
            print(f"   {key.upper()}) {value}")

        print("=" * 50)

        while True:  # Keep asking until a valid answer is given
            user_answer = input("Your answer (A/B/C/D, or 'Q' to quit): ").strip().lower()

            if user_answer == 'q':
                print("\n📊 Final Score:", score, "/", len(questions))
                print("Thanks for playing!")
                exit()
            elif user_answer in current_question["choices"]:
                if user_answer == current_question["answer"]:
                    print("✅ Correct! 🎉")
                    score += 1
                else:
                    print(f"❌ Wrong! 😢 The correct answer was {current_question['answer'].upper()}.")

                # end
                asked_questions.add(current_question)  # Mark question as answered
                break  # Move to the next question
            else:
                print("⚠️ Invalid choice. Please enter A, B, C, or D.")