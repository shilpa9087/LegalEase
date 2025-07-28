import re

def highlight_keywords(text):
    keywords = ["deadline", "payment", "breach", "penalty", "obligation", "termination"]
    
    for word in keywords:
        pattern = re.compile(rf'\b({word})\b', flags=re.IGNORECASE)
        text = pattern.sub(r'**\1**', text)

    return text
