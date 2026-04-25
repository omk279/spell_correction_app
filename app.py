import streamlit as st
from textblob import TextBlob
from utils import (
    readability_score,
    word_stats,
    highlight_changes,
    hinglish_to_english,
    simple_grammar_check
)

# Page config
st.set_page_config(page_title="AI Writing Assistant", layout="centered")

# Title
st.title("🧠 AI Writing Assistant")
st.caption("Spell ✔ Grammar ✔ Readability ✔ Tone ✔ Hinglish Support")

# Input
text_input = st.text_area("✍️ Enter your text:")

# Hinglish option
use_hinglish = st.checkbox("Convert Hinglish to English")

# Button
if st.button("Analyze Text"):

    if text_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        original_text = text_input

        # Step 1: Hinglish conversion
        if use_hinglish:
            text_input = hinglish_to_english(text_input)

        # Step 2: Spell correction
        blob = TextBlob(text_input)
        corrected = str(blob.correct())

        # Step 3: Simple grammar check
        grammar_errors = simple_grammar_check(corrected)

        # Step 4: Sentiment analysis
        sentiment = blob.sentiment.polarity

        # Step 5: Readability
        score = readability_score(corrected)

        # Step 6: Word stats
        word_count, sentence_count, freq = word_stats(corrected)

        # Step 7: Highlight changes
        highlighted = highlight_changes(original_text, corrected)

        # OUTPUT
        st.subheader("✅ Corrected Text")
        st.success(corrected)

        st.subheader("🔍 Highlighted Changes")
        st.markdown(highlighted, unsafe_allow_html=True)

        st.subheader("📊 Analysis Dashboard")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Word Count", word_count)
            st.metric("Sentence Count", sentence_count)
            st.metric("Grammar Issues", grammar_errors)

        with col2:
            st.metric("Readability Score", score)

            if sentiment > 0:
                st.success("😊 Positive Tone")
            elif sentiment < 0:
                st.error("😠 Negative Tone")
            else:
                st.info("😐 Neutral Tone")

        st.subheader("🔥 Top Frequent Words")
        for word, count in freq:
            st.write(f"{word} → {count}")

        # Download option
        st.download_button(
            "⬇ Download Corrected Text",
            corrected,
            file_name="corrected_text.txt"
        )
