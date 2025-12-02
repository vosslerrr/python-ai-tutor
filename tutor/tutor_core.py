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
        text = re.sub(r"</?(user|assistant)>", "", text)
        text = re.sub(r"^(Tutor|Assistant)\s*[:\-]*\s*", "", text, flags=re.IGNORECASE)

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
            "You help explain concepts, debug code, and create practice exercises. "
            "Always format responses using clean Markdown. "
            "Do NOT repeat earlier conversation. "
            "Do NOT answer previous questions again. "
            "Only answer the most recent user question.\n\n"
        )

        for msg in self.history:
            prompt += f"<user>{msg['user']}</user>\n"
            prompt += f"<assistant>{msg['tutor']}</assistant>\n"

        prompt += f"<user>{user_message}</user>\n"
        prompt += "<assistant>"

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
    
    # ------------------------------------------------------------------
    # STREAM
    # ------------------------------------------------------------------
    def stream(self, user_message):
        prompt = self._chat_prompt(user_message)

        # llama.cpp generator (streaming)
        for chunk in self.engine.generate_stream(prompt):
            text = self._clean_output(chunk)
            if text.strip():
                yield text

        # Save final answer (non-streamed)
        final_answer = self.engine.generate(prompt)
        final_answer = self._clean_output(final_answer)

        self.history.append({
            "user": user_message,
            "tutor": final_answer
        })

