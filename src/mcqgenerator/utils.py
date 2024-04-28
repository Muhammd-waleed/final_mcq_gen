from langchain_community.document_loaders import PyPDFLoader

def pdf_text(address):
    loader = PyPDFLoader(address)
    pages = loader.load_and_split()
    text=""
    for count,page in enumerate(pages):
        text+=page.page_content
    
    return text