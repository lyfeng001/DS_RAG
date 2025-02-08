from utils.rag import RAG



if __name__ == "__main__":
    rag = RAG(rag=False)
    question = "9.14和9.3哪个大"
    answer = rag.run(question)
    print(answer)

