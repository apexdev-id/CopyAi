# app.py
from copyai.cleaner import clean_text
from copyai.formatter import normalize_paragraphs
from copyai.branding import append_branding

def run():
    print("=== CopyAI Text Cleaner ===")
    print("Paste teks AI (akhiri dengan ENTER dua kali):\n")

    lines = []
    empty_count = 0

    while True:
        line = input()
        if line == "":
            empty_count += 1
            if empty_count == 2:
                break
        else:
            empty_count = 0
        lines.append(line)

    raw_text = "\n".join(lines)

    cleaned = clean_text(raw_text)
    formatted = normalize_paragraphs(cleaned)
    final_text = append_branding(formatted)

    print("\n=== HASIL COPYAI ===\n")
    print(final_text)

if __name__ == "__main__":
    run()
