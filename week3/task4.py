def clean_text(paragraph):
    if not paragraph:
        return ""
    paragraph = paragraph.lower()
    punctuation_marks = [".", ",", "!", "?", ":", ";", "-", "'", "\""]
    for mark in punctuation_marks:
        paragraph = paragraph.replace(mark, "")
    return paragraph

def count_word(paragraph):
    cleaned = clean_text(paragraph)
    return len(cleaned.split())

def count_character(paragraph):
    """Count all characters except spaces."""
    return sum(1 for char in paragraph if char != ' ')

def count_vowel_cons(paragraph):
    vowels = "aeiou"
    vowel_count = 0
    consonanat_count = 0

    for char in paragraph.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonanat_count += 1

    return {"vowels": vowel_count, "consonant": consonanat_count}

def find_longest_word(paragraph):
    cleaned = clean_text(paragraph)
    words = cleaned.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest 

def get_word_frequency(paragraph):
    cleaned = clean_text(paragraph)
    words = cleaned.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word,0) + 1
    return word_counts

def get_repeated_words(paragraph):
    freqs =get_word_frequency(paragraph)
    repeated = []
    for word, count in freqs.items(): #.items() gives us a collection of those pairs as tuples, where the word is the key and the count is the value.
        if count > 1:
            repeated.append(word)
    return repeated

def get_top_five_words(paragraph):
    freqs = get_word_frequency(paragraph)
    sorted_words = sorted(freqs.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:5]

def generate_text_report(paragraph):
    """Generate and display the complete text analysis report."""
    print(f"Input Text: \"{paragraph}\"\n")
    print("--- Text Analysis Report ---")
    print(f"Words Count          : {count_word(paragraph)}")
    print(f"Characters (no space): {count_character(paragraph)}")
    
    vc = count_vowel_cons(paragraph)
    print(f"Vowels               : {vc['vowels']}")
    print(f"Consonants           : {vc['consonant']}")
    
    print(f"Longest Word         : {find_longest_word(paragraph)}")
    
    repeated = get_repeated_words(paragraph)
    print(f"Repeated Words       : {', '.join(repeated) if repeated else 'None'}")
    
    print("\n--- Top Frequent Words ---")
    top_5 = get_top_five_words(paragraph)
    for word, count in top_5:
        print(f"'{word}': {count} time(s)")
    print("----------------------------")

if __name__ == "__main__":
    sample_input = "Python is useful and Python is powerful."
    generate_text_report(sample_input)

