from app.generation.prompt_builder import build_prompt
from app.generation.local_llm import generate

def generate_answer(q,d): return generate(build_prompt(q,d))
