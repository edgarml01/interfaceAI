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
sentences = [
    "Presiona el botón continuar",
    "Presiona el botón para avanzar",
    "Haz clic en el boton de la esquina infrerior derecha",
    "Cierra el programa"
]

# Convertir frases en vectores numéricos
embeddings = model.encode(sentences)

# Calcular similitudes coseno
cosine_similarities = [
    cosine_similarity([embeddings[0]], [embeddings[i]])[0][0]
    for i in range(1, len(sentences))
]

# Encontrar la oración con mayor similitud semántica
max_similarity_index = cosine_similarities.index(max(cosine_similarities)) + 1
most_similar_sentence = sentences[max_similarity_index]

# Imprimir resultados
for i, sim in enumerate(cosine_similarities, start=1):
    print(f"Similitud Coseno con semantica entre '{sentences[0]}' y '{sentences[i]}': {sim}")

print(f"La oración con mayor similitud semántica es: '{most_similar_sentence}'")



