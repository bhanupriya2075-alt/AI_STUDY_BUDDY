from gemini_helper import generate_response


def generate_quiz(content):

    prompt = f"""
    Generate 10 multiple-choice questions
    from the following content.

    Content:

    {content}

    Requirements:

    - Each question should have 4 options.
    - Clearly indicate the correct answer.
    - Questions should test understanding.
    - Use a clean format.

    Example:

    Q1. What is AI?

    A. Artificial Intelligence
    B. Artificial Internet
    C. Automatic Information
    D. None

    Answer: A
    """

    return generate_response(prompt)