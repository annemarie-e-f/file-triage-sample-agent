import re
from llm_interface import LLMInterface
import actions

HELP_TEXT = """
Commands you can try:
  Organize files by type
  Delete files older than 30 days
  Delete files older than 45 days
  Move .pdf files to pdfs
  Move .jpg files to images
  help
  exit
"""

def dispatch(user_input: str, llm):
    text = user_input.lower().strip()

    if text in {"help", "commands"}:
        print(HELP_TEXT)
        return

    if "organize" in text and "type" in text:
        actions.organize_by_type()
        return

    if "delete" in text and "older than" in text:
        m = re.search(r"older than (\\d+) days", text)
        days = int(m.group(1)) if m else 30
        actions.delete_files_older_than(days)
        return

    if text.startswith("move") and " to " in text:
        # pattern: move .pdf files to pdfs
        m = re.search(r"(\\.\\w+) files? to ([\\w\\-]+)", text)
        if m:
            ext, folder = m.groups()
            actions.move_files_by_extension(ext, folder)
        else:
            print("Could not parse move command. Try: move .pdf files to pdfs")
        return

    # Fallback: show placeholder model output
    intent_placeholder = llm.parse_intent(user_input)
    print(f"No mapped action. (Placeholder model output: {intent_placeholder})")
    print("Type 'help' for available commands.")

def main():
    print("Welcome to the File Triage Sample Agent!")
    print("Type 'help' for commands, 'exit' to quit.")
    llm = LLMInterface()
    while True:
        try:
            user_input = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if not user_input:
            continue

        dispatch(user_input, llm)

if __name__ == "__main__":
    main()
