from app.retrieval.retriever import retrieve
from app.generation.answer_generator import generate_answer

def run():
    query=input('Ask your memory: ')
    docs=retrieve(query)
    answer=generate_answer(query,docs)
    print(answer)

if __name__=='__main__': run()
