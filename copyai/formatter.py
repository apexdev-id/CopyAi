# copyai/formatter.py
def normalize_paragraphs(text: str) -> str:
    paragraphs = text.split("\n\n")
    cleaned_paragraphs = []

    for para in paragraphs:
        para = para.replace("\n", " ")   # gabungkan baris
        para = para.strip()

        if para:
            cleaned_paragraphs.append(para)

    return "\n\n".join(cleaned_paragraphs)