import argparse
import json
import sys
from pathlib import Path
from .extractor import extract_tasks

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extrahiert offene Markdown Tasks (- [ ] oder * [ ])."
    )
    parser.add_argument(
        "file", 
        nargs="?", 
        help="Pfad zur Markdown-Datei (falls weggelassen, wird von Stdin gelesen)"
    )
    parser.add_argument(
        "--json", 
        action="store_true", 
        help="Ausgabe als JSON-Array"
    )

    args = parser.parse_args()

    content = ""
    if args.file:
        file_path = Path(args.file)
        if not file_path.exists() or not file_path.is_file():
            sys.stderr.write(f"Error: File '{args.file}' not found.\n")
            return 1
        content = file_path.read_text(encoding="utf-8")
    else:
        if sys.stdin.isatty():
            parser.print_help(sys.stderr)
            return 1
        content = sys.stdin.read()

    tasks = extract_tasks(content)

    if args.json:
        print(json.dumps(tasks, indent=2 if not sys.stdout.isatty() else None))
    else:
        if not tasks:
            print("Keine offenen Tasks gefunden.")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
