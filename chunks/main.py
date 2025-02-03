from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import asyncio

file_path = "attention.pdf"
loader = PyPDFLoader(file_path)
# Lists to store pages and text data
pages = []
texts = []

# Async function to load PDF content with logging
async def PdfReader():
    async for page in loader.alazy_load():
        pages.append(page)
    return pages

def Chunks():
    text_splitter = RecursiveCharacterTextSplitter(
        separators=[
        "\n\n",
        # "\n",
        # " ",
        ".",
        # ",",
        # "\u200b",  # Zero-width space
        # "\uff0c",  # Fullwidth comma
        # "\u3001",  # Ideographic comma
        # "\uff0e",  # Fullwidth full stop
        # "\u3002",  # Ideographic full stop
        # "",
    ],
        chunk_size=100,  # Set a small chunk size
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False
    )

    # Extract text content from the loaded pages and split it into chunks
    # Create chunks from the page content
    texts = text_splitter.create_documents([page.page_content for page in pages])

    return texts

async def main():
    # First, load the PDF content
    await PdfReader()
    
    # Then split the loaded pages into chunks
    chunks = Chunks()
    print(f"Chunks created: {len(chunks)}")
    
    # Print out some of the chunks
    for chunk in chunks:
        print(chunk)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
