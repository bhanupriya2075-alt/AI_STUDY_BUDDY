from gemini_helper import generate_response


def generate_flashcards(content):

    prompt = f"""
    Create study flashcards from the content below.

    Content:

    {content}

    Format:

    Flashcard 1

    Question:
    What is Cloud Computing?

    Answer:
    Cloud computing is ...

    Flashcard 2

    Question:
    ...

    Answer:
    ...

    Generate at least 10 flashcards.
    """

    return generate_response(prompt)