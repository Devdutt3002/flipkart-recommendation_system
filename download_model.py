"""
Script to pre-download the HuggingFace embedding model.
This will download the model to your local cache so it's ready when you run the app.
"""

from langchain_huggingface import HuggingFaceEmbeddings
import sys

print("=" * 60)
print("Downloading BAAI/bge-base-en-v1.5 embedding model...")
print("This may take a few minutes depending on your internet speed.")
print("=" * 60)

try:
    # Initialize embeddings - this will trigger the download
    print("\nInitializing embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
    
    # Test the embeddings with a simple query to ensure it works
    print("\nTesting embeddings...")
    test_embedding = embeddings.embed_query("test")
    print("[SUCCESS] Model downloaded successfully!")
    print(f"[INFO] Embedding dimension: {len(test_embedding)}")
    print(f"\nModel is now cached and ready to use!")
    print(f"Cache location: ~/.cache/huggingface/")
    
except Exception as e:
    print(f"\n[ERROR] Error downloading model: {e}")
    sys.exit(1)

