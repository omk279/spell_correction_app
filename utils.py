from collections import Counter

# 🔹 Smart Replace (MOST IMPORTANT)
def smart_replace(text):
    mapping = {
        "ur": "your",
        "ther": "there",
        "err": "error",
        "iss": "is",
        "u": "you"
    }

    words = text.split()
    corrected = [mapping.get(word.lower(), word) for word in words]

    return " ".join(corrected)


# 🔹 Readability Score
def readability_score(text):
    words = text.split()
    sentences = text.count('.') + 1
    syllables = sum([len(word)//3 for word in words])

    if len(words) == 0:
        return 0

    score = 206.835 - (1.015 * (len(words)/sentences)) - (84.6 * (syllables/len(words)))
    return round(score, 2)


# 🔹 Word Stats
def word_stats(text):
    words = text.split()
    word_count = len(words)
    sentence_count = text.count('.') + 1
    freq = Counter(words).most_common(5)

    return word_count, sentence_count, freq


# 🔹 Highlight Changes
def highlight_changes(original, corrected):
    orig_words = original.split()
    corr_words = corrected.split()

    highlighted = []
    min_len = min(len(orig_words), len(corr_words))

    for i in range(min_len):
        o = orig_words[i]
        c = corr_words[i]

        if o != c:
            highlighted.append(
                f"<span style='color:red'>{o}</span> → <span style='color:green'>{c}</span>"
            )
        else:
            highlighted.append(o)

    if len(corr_words) > min_len:
        highlighted.extend(corr_words[min_len:])

    return " ".join(highlighted)


# 🔹 Hinglish Converter
def hinglish_to_english(text):

    mapping = {
        "mera": "my",
        "meri": "my",
        "mere": "my",
        "mai": "I",
        "main": "I",
        "tum": "you",
        "tu": "you",
        "hai": "is",
        "tha": "was",
        "thi": "was",
        "the": "were",
        "nahi": "not",
        "kyu": "why",
        "kya": "what",
        "kaise": "how",
        "kab": "when",
        "kaha": "where",
        "dost": "friend",
        "ghar": "home",
        "khana": "food",
        "aaya": "came",
        "gaya": "went",
        "kar": "do",
        "raha": "doing",
        "rahi": "doing",
        "rahe": "doing",
        "kal": "yesterday",
        "aaj": "today"
    }

    words = text.lower().split()
    return " ".join([mapping.get(word, word) for word in words])


# 🔹 Simple Grammar Check
def simple_grammar_check(text):
    errors = 0
    words = text.split()

    for i in range(len(words) - 1):

        if words[i].lower() in ["he", "she", "it"] and words[i+1].lower() == "go":
            errors += 1

        if words[i].lower() == words[i+1].lower():
            errors += 1

    return errors
