from pathlib import Path


class Utils:
    def load_prompt(self, prompt_name: str):
        base_dir = Path(__file__).resolve().parent.parent
        prompt_path = base_dir / "prompts" / prompt_name

        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()