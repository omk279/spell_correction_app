import streamlit as st
from textblob import TextBlob
from utils import (
    readability_score,
    word_stats,
    highlight_changes,
    hinglish_to_english,
    simple_grammar_check,
    smart_replace
)

st.set_page_config(page_title="AI Writing Assistant", layout="centered")

st.title("🧠 AI Writing Assistant")
st.caption("Spell ✔ Grammar ✔ Readability ✔ Tone ✔ Hinglish Support")

text_input = st.text_area("✍️ Enter your text:")
use_hinglish = st.checkbox("Convert Hinglish to English")

if st.button("Analyze Text"):

    if text_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        original_text = text_input

        # Step 1: Hinglish
        if use_hinglish:
            text_input = hinglish_to_english(text_input)

        # Step 2: Smart Replace (IMPORTANT)
        text_input = smart_replace(text_input)

        # Step 3: Spell correction
        blob = TextBlob(text_input)
        corrected = str(blob.correct())

        # Step 4: Grammar (simple rules)
        grammar_errors = simple_grammar_check(corrected)

        # Step 5: Sentiment
        sentiment = blob.sentiment.polarity

        # Step 6: Readability
        score = readability_score(corrected)

        # Step 7: Word stats
        word_count, sentence_count, freq = word_stats(corrected)

        # Step 8: Highlight changes
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

        st.download_button(
            "⬇ Download Corrected Text",
            corrected,
            file_name="corrected_text.txt"
        )
