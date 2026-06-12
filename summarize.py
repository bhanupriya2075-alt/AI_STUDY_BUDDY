from gemini_helper import generate_response


def summarize_notes(notes):

    prompt = f"""
    Summarize the following study notes.

    Notes:

    {notes}

    Instructions:

    1. Extract key concepts.
    2. Use bullet points.
    3. Keep important definitions.
    4. Highlight important facts.
    5. Make revision-friendly notes.

    Output should be concise and easy to study.
    """

    return generate_response(prompt)