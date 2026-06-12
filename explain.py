from gemini_helper import generate_response


def explain_topic(topic):

    prompt = f"""
    You are an expert teacher.

    Explain the topic:

    {topic}

    Requirements:

    1. Use simple language.
    2. Give definitions.
    3. Explain step-by-step.
    4. Provide examples.
    5. Include important points.
    6. Make it suitable for college students.

    Format:

    Introduction
    Explanation
    Example
    Key Points
    Conclusion
    """

    return generate_response(prompt)