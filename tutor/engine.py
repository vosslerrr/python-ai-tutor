import re
from llama_cpp import Llama
from tutor.config import MODEL_PATH, N_CTX, N_THREADS, N_GPU_LAYERS, TEMPERATURE, TOP_P, MAX_TOKENS

class LlamaEngine:
    def __init__(self):
        print("Loading GGUF model...")
        self.llm = Llama(
            model_path=MODEL_PATH,
            n_ctx=N_CTX,
            n_threads=N_THREADS,
            n_gpu_layers=N_GPU_LAYERS,
            verbose=False
        )

    def _clean(self, text):
        text = re.sub(r"^llama_perf_context_print.*\n?", "", text, flags=re.MULTILINE)
        return text.strip()

    def generate(self, prompt):
        output = self.llm(
            prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            top_p=TOP_P,
        )
        return self._clean(output["choices"][0]["text"])

    def count_tokens(self, text):
        return len(self.llm.tokenize(text.encode()))
