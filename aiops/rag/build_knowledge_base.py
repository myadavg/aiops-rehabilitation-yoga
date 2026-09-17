import chromadb

# Create a local ChromaDB database
client = chromadb.PersistentClient(
    path="./rag/chroma_db"
)

collection = client.get_or_create_collection(
    name="aiops_knowledge"
)

# Read the troubleshooting knowledge
with open("./rag/knowledge.txt", "r") as file:
    text = file.read()

# Split knowledge into sections
documents = [
    section.strip()
    for section in text.split("\n\n")
    if section.strip()
]

# Store the knowledge in ChromaDB
collection.add(
    ids=[f"doc-{i}" for i in range(len(documents))],
    documents=documents
)

print(f"Knowledge base created with {len(documents)} documents.")
