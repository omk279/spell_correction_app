from collections import Counter

def readability_score(text):
    words = text.split()
    sentences = text.count('.') + 1
    syllables = sum([len(word)//3 for word in words])

    if len(words) == 0:
        return 0

    score = 206.835 - (1.015 * (len(words)/sentences)) - (84.6 * (syllables/len(words)))
    return round(score, 2)


def word_stats(text):
    words = text.split()
    word_count = len(words)
    sentence_count = text.count('.') + 1
    freq = Counter(words).most_common(5)

    return word_count, sentence_count, freq


def highlight_changes(original, corrected):
    orig_words = original.split()
    corr_words = corrected.split()

    highlighted = []

    for o, c in zip(orig_words, corr_words):
        if o != c:
            highlighted.append(f"<span style='color:red'>{o}</span> → <span style='color:green'>{c}</span>")
        else:
            highlighted.append(o)

    return " ".join(highlighted)


def hinglish_to_english(text):
    mapping = {
        "mera": "my",
        "tum": "you",
        "hai": "is",
        "nahi": "not",
        "kya": "what",
        "kaise": "how",
        "kyu": "why"
    }

    words = text.split()
    converted = [mapping.get(word.lower(), word) for word in words]

    return " ".join(converted)