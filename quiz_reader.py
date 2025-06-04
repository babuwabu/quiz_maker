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
            
# load the quiz
# end