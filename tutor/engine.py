from llama_cpp import Llama
from tutor.config import MODEL_PATH

class LlamaEngine:
    def __init__(self):
        print("[LlamaEngine] Loading model:", MODEL_PATH)
        
        self.model = Llama(
            model_path=MODEL_PATH,
            n_ctx=4096,
            n_threads=6,
            n_gpu_layers=0,
            verbose=False
        )

    def generate(self, prompt, max_tokens=300):
        output = self.model(
            prompt,
            max_tokens=max_tokens,
            stop=["</assistant>", "</user>"]
        )
        return output["choices"][0]["text"]

    def generate_stream(self, prompt):
        for chunk in self.model(prompt, stream=True):
            token = chunk["choices"][0]["text"]
            yield token