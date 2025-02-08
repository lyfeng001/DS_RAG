## 1. Model Installation

### ollama

- [ollama](https://github.com/ollama/ollama)

### models


```bash
ollama pull deepseek-r1
ollama pull nomic-embed-text
```

## 2. Requirements Installation

```bash
pip install -r requirements.txt
```

## 3. Run

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
    rag = RAG(rag=True)
    ```

- run the main.py

    ```bash
    python main.py
    ```


### 3.2 run without RAG

- change the question in main.py
- set rag=False in main.py

    ```python
    rag = RAG(rag=False)
    ```

- run the main.py
