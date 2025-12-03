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
            prompt=prompt,
            max_tokens=max_tokens,
            stop=["</assistant>", "</user>"]
        )
        return output["choices"][0]["text"]