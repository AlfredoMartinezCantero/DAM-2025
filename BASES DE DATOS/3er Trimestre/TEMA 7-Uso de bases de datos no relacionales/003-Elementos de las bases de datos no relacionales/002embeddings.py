from nomic import embed

# Text to embed
text = "fresa"

# Generate embedding
result = embed.text(
    texts=[text],
    model="nomic-embed-text:v1.5"
)

# Extract the vector
embedding = result["embeddings"][0]

print("Embedding length:", len(embedding))
print("First 10 values:", embedding[:10])
