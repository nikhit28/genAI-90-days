def analyze_text(text):
    word_count=len(text.split())    
    words=text.lower().split()
    unique_words=set(words)

    return {
        "word_count": word_count,
        "unique_words": unique_words
    }


sample_text = input("Enter a sample text for analysis: ")
analysis_result = analyze_text(sample_text)
print(f"Word Count: {analysis_result['word_count']}")
print(f"Unique Words: {analysis_result['unique_words']}")
