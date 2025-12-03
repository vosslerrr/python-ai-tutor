from llama_cpp import Llama
from tutor.config import MODEL_PATH

class LlamaEngine:
    def __init__(self):
        print("[LlamaEngine] Loading model:", MODEL_PATH)

        self.model = Llama(
            model_path=MODEL_PATH,
            n_ctx=4096,
            n_threads=6,
            add_bos_token=True,
            chat_format="qwen2",
            verbose=False
        )

    def generate(self, prompt, max_tokens=300):
        output = self.model(
            prompt,
            max_tokens=max_tokens,
            temperature=0.7,
            top_p=0.9,
            repeat_penalty=1.05,
            stop=["</assistant>", "</user>"],
            echo=False
        )
        text = output["choices"][0]["text"]

        text = text.replace("\\n", "\n").replace("\r", "")

        return text.strip()
