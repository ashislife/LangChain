# -------------------------<NOT RUNNING ----------------------------->

# ===== CPU-friendly Chat Simulation for LangChain-style code =====
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# --- Small, CPU-friendly model ---
model_id = "TheBloke/mini-llama-1.1B-GPTQ"

# Tokenizer & Model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="cpu",        # CPU-only
    low_cpu_mem_usage=True
)

# Pipeline
llm_pipeline = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
    do_sample=True,
    temperature=0.5,
    max_new_tokens=100
)

# ===== Mimic ChatHuggingFace =====
class ChatHuggingFaceMock:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def invoke(self, prompt_text):
        result = self.pipeline(prompt_text)
        # result is a list of dicts, extract generated_text
        return type("Result", (), {"content": result[0]["generated_text"]})

# ===== Main code (same style as original) =====
llm = llm_pipeline                 # HuggingFacePipeline simulation
model = ChatHuggingFaceMock(llm)   # ChatHuggingFace simulation

# Direct invoke without using extra 'prompt' variable
result = model.invoke("What is the Capital of India?")
print(result.content)
