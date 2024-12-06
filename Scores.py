"""This file calculate and adjust the marks of the student."""


def adjust_student_marks():
    """Prompt user to adjust list of student marks."""
    try:
        score = input("get the student marks")
        new_scores = [20]

        for score in score:
            new_scores.append(score + 20)
        return new_scores
    except ValueError:
        print("Please enter valid integer scores.")
        return [20]
