import streamlit as st

from database import (
    save_history,
    get_history,
    clear_history
)

from modules.explain import explain_topic
from modules.summarize import summarize_notes
from modules.quiz import generate_quiz
from modules.flashcards import generate_flashcards

st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Powered Study Buddy")

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Feature",
    [
        "Explain Topic",
        "Summarize Notes",
        "Generate Quiz",
        "Generate Flashcards",
        "History"
    ]
)

# --------------------------------
# EXPLAIN TOPIC
# --------------------------------

if menu == "Explain Topic":

    st.header("Topic Explanation")

    topic = st.text_input(
        "Enter Topic"
    )

    if st.button("Explain"):

        if topic:

            result = explain_topic(topic)

            st.success("Explanation Generated")

            st.write(result)

            save_history(
                "Explain Topic",
                topic,
                result
            )

# --------------------------------
# SUMMARIZE
# --------------------------------

elif menu == "Summarize Notes":

    st.header("Notes Summarizer")

    notes = st.text_area(
        "Paste Notes"
    )

    if st.button("Summarize"):

        if notes:

            result = summarize_notes(
                notes
            )

            st.success("Summary Generated")

            st.write(result)

            save_history(
                "Summarize",
                notes,
                result
            )

# --------------------------------
# QUIZ
# --------------------------------

elif menu == "Generate Quiz":

    st.header("Quiz Generator")

    content = st.text_area(
        "Enter Content"
    )

    if st.button("Generate Quiz"):

        if content:

            result = generate_quiz(
                content
            )

            st.success("Quiz Generated")

            st.write(result)

            save_history(
                "Quiz",
                content,
                result
            )

# --------------------------------
# FLASHCARDS
# --------------------------------

elif menu == "Generate Flashcards":

    st.header("Flashcard Generator")

    content = st.text_area(
        "Enter Content"
    )

    if st.button(
        "Generate Flashcards"
    ):

        if content:

            result = generate_flashcards(
                content
            )

            st.success(
                "Flashcards Generated"
            )

            st.write(result)

            save_history(
                "Flashcards",
                content,
                result
            )

# --------------------------------
# HISTORY
# --------------------------------

elif menu == "History":

    st.header("History")

    history = get_history()

    if len(history) == 0:

        st.info(
            "No history available"
        )

    else:

        for item in history:

            st.subheader(
                item[1]
            )

            st.write(
                "Input:"
            )

            st.write(
                item[2]
            )

            st.write(
                "Output:"
            )

            st.write(
                item[3]
            )

            st.divider()

    if st.button(
        "Clear History"
    ):

        clear_history()

        st.success(
            "History Cleared"
        )
