import streamlit as st
from textblob import TextBlob
import language_tool_python
from utils import readability_score, word_stats, highlight_changes, hinglish_to_english

# Initialize grammar tool
tool = language_tool_python.LanguageToolPublicAPI('en-US')

st.set_page_config(page_title="AI Writing Assistant", layout="centered")

st.title("🧠 AI Writing Assistant")
st.caption("Spell ✔ Grammar ✔ Readability ✔ Tone ✔ Analytics")

# Input
text_input = st.text_area("✍️ Enter your text:")

# Hinglish toggle
use_hinglish = st.checkbox("Convert Hinglish to English (basic)")

if st.button("Analyze Text"):

    if text_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Hinglish conversion
        if use_hinglish:
            text_input = hinglish_to_english(text_input)

        # Spell correction
        blob = TextBlob(text_input)
        corrected = str(blob.correct())

        # Grammar check
        matches = tool.check(corrected)
        grammar_errors = len(matches)

        # Sentiment
        sentiment = blob.sentiment.polarity

        # Readability
        score = readability_score(corrected)

        # Word stats
        word_count, sentence_count, freq = word_stats(corrected)

        # Highlight changes
        highlighted = highlight_changes(text_input, corrected)

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

        # Download
        st.download_button(
            "⬇ Download Corrected Text",
            corrected,
            file_name="corrected_text.txt"
        )
