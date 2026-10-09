from langchain_text_splitters import RecursiveCharacterTextSplitter

def make_splitter(chunk_size:int=800, chunk_overlap:int=120):
    return RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap,separators=["\n\n","\n",". "," ",""])

def split_text(text:str,chunk_size:int=800,chunk_overlap:int=120):
    return make_splitter(chunk_size,chunk_overlap).split_text(text)
