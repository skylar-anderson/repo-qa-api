import os
import openai
from langchain.llms import OpenAI
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.docstore.document import Document
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import CharacterTextSplitter
from get_github_docs import get_github_docs 
from prompt import PROMPT

owner = os.getenv('OWNER', 'primer')
repo = os.getenv('REPO', 'design')
sources = get_github_docs(owner, repo)

source_chunks = []
splitter = CharacterTextSplitter(separator=" ", chunk_size=1024, chunk_overlap=0)

for source in sources:
    for chunk in splitter.split_text(source.page_content):
        source_chunks.append(Document(page_content=chunk, metadata=source.metadata))

search_index = FAISS.from_documents(source_chunks, OpenAIEmbeddings())

# Temperature refers to the amount of entropy tolerated from
# answer generation.  0 = no entropy.  1 = max entropy.
# a higher temp will result in riskier and more creative
# responses.
temp = .1

# k refers to how many results should be returned from
# vector DB when searching. Also known as a "k-nearest
# neighbors" (KNN) search
max_sources = 4

chain = load_qa_with_sources_chain(OpenAI(temperature=temp), chain_type="stuff", prompt=PROMPT)
def get_answer(question):
    return chain(
        {
            "input_documents": search_index.similarity_search(question, k=max_sources),
            "question": question,
        },
        return_only_outputs=True,
    )["output_text"]
    

def print_answer(question):
    print(get_answer(question))
