from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(sentence1, sentence2):
    # Convertir a vectores TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([sentence1, sentence2])

    # Calcular similitud coseno
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return cosine_sim[0][0]
# Oraciones a comparar

sentence1 = "Presiona el boton continuar"
sentence2 = "Presiona el boton para avazar"

similitud = calculate_cosine_similarity(sentence1, sentence2)
print("Similitud Coseno sin similitud semantica:", similitud)

model = SentenceTransformer("all-MiniLM-L6-v2")  # Modelo ligero pero preciso

# Frases a comparar
sentences = ["Presiona el botón continuar", "Presiona el botón para avanzar"]

# Convertir frases en vectores numéricos
embeddings = model.encode(sentences)

# Calcular similitud coseno
cosine_sim = cosine_similarity([embeddings[0]], [embeddings[1]])

print("Similitud Coseno con semantica:", cosine_sim[0][0])



