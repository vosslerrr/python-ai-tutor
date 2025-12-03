import re
from tutor.engine import LlamaEngine
import tutor.modes as modes

class AITutor:
    def __init__(self):
        self.engine = LlamaEngine()
        self.history = []

    # ------------------------------------------------------------------
    # CLEAN OUTPUT
    # ------------------------------------------------------------------
    def _clean_output(self, text):
        text = re.sub(r"^(Tutor|Assistant)\s*[:\-]*\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"(#+\s*Practice Exercise\s*){2,}", "### Practice Exercise\n", text)

        lines = text.split("\n")
        cleaned = []
        for line in lines:
            if not cleaned or cleaned[-1].strip() != line.strip():
                cleaned.append(line)

        return "\n".join(cleaned).strip()

    # ------------------------------------------------------------------
    # PROMPT BUILDER
    # ------------------------------------------------------------------
    def _chat_prompt(self, user_message):
        prompt = (
            "You are a friendly Python tutor. "
            "You explain concepts clearly, give examples, debug code, and create simple exercises. "
            "ALWAYS respond in clean Markdown. "
            "NEVER repeat earlier conversation text. "
            "NEVER include 'User:' or 'Tutor:' in your output.\n\n"
        )

        for msg in self.history:
            prompt += f"User asked: {msg['user']}\n"
            prompt += f"You answered: {msg['tutor']}\n\n"

        prompt += f"User asked: {user_message}\n"
        prompt += "Your answer:\n"

        return prompt

    # ------------------------------------------------------------------
    # MAIN ASK METHOD
    # ------------------------------------------------------------------
    def _ask(self, user_message):
        prompt = self._chat_prompt(user_message)
        raw = self.engine.generate(prompt)
        cleaned = self._clean_output(raw)

        self.history.append({
            "user": user_message,
            "tutor": cleaned
        })

        return cleaned

    # ------------------------------------------------------------------
    # MODE DETECTION
    # ------------------------------------------------------------------
    def auto(self, text):
        t = text.lower()

        if "error" in t or "fix" in t or t.strip().startswith("def"):
            return self._ask(modes.code_debugger(text))

        if "example" in t:
            return self._ask(modes.code_example_generator(text))

        if "exercise" in t or "practice" in t or "problem" in t:
            return self._ask(modes.exercise_creator(text))

        if "what is" in t or "explain" in t:
            return self._ask(modes.concept_explainer(text))

        return self._ask(f"Give helpful feedback:\n{text}")

    def chat(self, message):
        return self.auto(message)
