from langchain_community.document_loaders import PDFPlumberLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from pathlib import Path
from .llm_base import LLMBase



class LLM_Ollama(LLMBase):
    def __init__(self, rag=True, directory="assets"):
        self.rag = rag
        self.directory = directory
        self.docs = []
        if self.rag:
            pdf_files = Path(directory).glob("*.pdf")
            for pdf_file in pdf_files:
                loader = PDFPlumberLoader(str(pdf_file))
            self.docs.extend(loader.load())

    def split_docs(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
        all_splits = text_splitter.split_documents(self.docs)
        return all_splits

    def create_vectorstore(self):
        all_splits = self.split_docs()
        local_embeddings = OllamaEmbeddings(model="nomic-embed-text")
        vectorstore = Chroma.from_documents(documents=all_splits, embedding=local_embeddings)
        return vectorstore
    
    @staticmethod
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    def create_rag_chain(self):
        # ref: https://github.com/datawhalechina/handy-ollama/blob/main/notebook/C7/DeepSeek_R1_RAG/使用%20DeepSeek%20R1%20和%20Ollama%20实现本地%20RAG%20应用.ipynb
        RAG_TEMPLATE = """
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

            <context>
            {context}
            </context>

            Answer the following question:

            {question}"""
        
        vectorstore = self.create_vectorstore()
        model = ChatOllama(
            model="deepseek-r1",
        )
        rag_prompt = ChatPromptTemplate.from_template(RAG_TEMPLATE)
        retriever = vectorstore.as_retriever()
        qa_chain = (
            {"context": retriever | self.format_docs, "question": RunnablePassthrough()}
            | rag_prompt
            | model
            | StrOutputParser()
        )
        return qa_chain


    def without_rag(self, question):
        model = ChatOllama(
            model="deepseek-r1",
        )
        prompt = ChatPromptTemplate.from_template(
            "Answer the following question concisely: {question}"
        )
        chain = prompt | model | StrOutputParser()
        return chain.invoke({"question": question})


    def run(self, question):
        if self.rag:
            qa_chain = self.create_rag_chain()
            answer = qa_chain.invoke(question)
            return answer
        else:
            answer = self.without_rag(question)
            return answer




