# copyai/cleaner.py
import re

def remove_emojis(text: str) -> str:
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F"
        "\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FAFF"
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub("", text)


def remove_ai_artifacts(text: str) -> str:
    patterns = [
        r"[—–―]{1,}",        # semua jenis dash panjang
        r"[-_=]{3,}",        # garis ascii panjang
        r"[#*~`]{2,}",       # dekorasi markdown
        r"\s{2,}",           # spasi berlebihan
    ]

    for pattern in patterns:
        text = re.sub(pattern, " ", text)

    return text


def clean_text(text: str) -> str:
    text = remove_emojis(text)
    text = remove_ai_artifacts(text)
    return text.strip()
