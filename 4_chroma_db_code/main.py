import chromadb

client = chromadb.PersistentClient(path="./db")

collection = client.get_or_create_collection("Testing")

collection.upsert(
    documents=[
        "Python is a versatile programming language used in AI.",
        "The quick brown fox jumps over the lazy dog.",
        "Vector databases store numerical representations of data."
    ],
    metadatas=[{"source": "tech"}, {"source": "idiom"}, {"source": "data"}],
    ids=["doc1", "doc2", "doc3"]
)

def main(query):
    result = collection.query(  
                query_texts = [query],
                n_results=1 
                )

    print(result)
    
    return result.get("documents", []), result.get("metadatas", []) if result else "No results found."

user_query = input("Enter your query:")

documents, metadatas = main(user_query)

print("Documents:", documents)
print("Metadatas:", metadatas)

