## 1. Requirements Installation

```bash
pip install -r requirements.txt
```


## 2. Model Installation ([optional] if run the llm locally)

### ollama

- [ollama](https://github.com/ollama/ollama)

### models


```bash
ollama pull deepseek-r1
ollama pull nomic-embed-text
```


## 3. Run locally

### 3.1 run with RAG

- run the ollama in bash

    ```bash
    ollama serve
    ```

- make a new folder named assets in the root directory

- put files in assets folder

- change the question in main.py

- set rag=True in main.py

    ```python
    llm_local = LLMFactory.create_llm(
        "ollama",
        rag=True,
        directory="assets"
    )
    ```

- run the main.py

    ```bash
    python main.py
    ```


### 3.2 run without RAG

- change the question in main.py
- set rag=False in main.py

    ```python
    llm_local = LLMFactory.create_llm(
        "ollama",
        rag=False,
    )
    ```

- run the main.py



## 4. Run with API

- change the question in main.py
- set api_key and model in main.py
    
    ```python
    llm_api = LLMFactory.create_llm(
        "api",
        api_key="Your API Key",
        model="deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
    )
    ```
