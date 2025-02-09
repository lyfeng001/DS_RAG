from utils.llm_factory import LLMFactory

def ollama_llm(question):
    # 使用Ollama本地模型
    llm_local = LLMFactory.create_llm(
        "ollama",
        rag=True,
        directory="assets"
    )
    answer_local = llm_local.run(question)
    print("Local answer:", answer_local)


def api_llm(question):
    # 使用API （暂无RAG）
    llm_api = LLMFactory.create_llm(
        "api",
        api_key="Your API Key",
        model="deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
    )
    answer_api = llm_api.run(question)
    print("API answer:", answer_api)


if __name__ == "__main__":
    
    question = "9.14和9.3哪个大"

    # ollama_llm(question)
    api_llm(question)


