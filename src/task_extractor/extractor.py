import re
from typing import List

# Regex verlangt zwingend mindestens ein Leerzeichen zwischen Bullet (- oder *) und Checkbox [ ]
TASK_PATTERN = re.compile(r"^\s*[-*]\s+\[\s\]\s+(.+)$", re.MULTILINE)

def extract_tasks(markdown_text: str) -> List[str]:
    """Extrahiert alle offenen Checkbox-Tasks aus einem Markdown-String."""
    if not markdown_text:
        return []
    
    matches = TASK_PATTERN.findall(markdown_text)
    return [match.strip() for match in matches if match.strip()]
