from utils.rag import RAG



if __name__ == "__main__":
    rag = RAG()
    question = "基地什么时候打开"
    answer = rag.run(question)
    print(answer)

