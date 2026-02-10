import re

def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove special characters (keep only letters and spaces)
    text = re.sub(r'[^a-z\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    raw_text = read_file("sample_text.txt")
    cleaned_text = clean_text(raw_text)

    print("RAW TEXT:\n", raw_text)
    print("\nCLEANED TEXT:\n", cleaned_text)
