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

def test1():
    print("Ejecutando orden 1")
def test2():
    print("Ejecutando orden 2")
def test3():
    print("Ejecutando orden 3")

# Oraciones a comparar
sentence1 = "Presiona el boton continuar"
sentence2 = "Presiona el boton para avazar"

similitud = calculate_cosine_similarity(sentence1, sentence2)
print("Similitud Coseno sin similitud semantica:", similitud)

model = SentenceTransformer("all-MiniLM-L6-v2")  # Modelo 

# Frases a comparar
oraciones = {
    "Presiona el botón continuar":test1,
    "Presiona el botón para retroceder":test2,
    "Cierra el programa":test3
}
oraciones_texto = list(oraciones.keys())

uinput = input("Escribe la orden: ")

# Convertir frases en vectores numéricos
embeddings = model.encode(oraciones_texto)
uEmbeddings = model.encode(uinput)

# Calcular similitudes coseno entre uEmbeddings y cada oración en embeddings
cosine_similarities = [
    cosine_similarity([uEmbeddings], [embeddings[i]])[0][0]
    for i in range(len(oraciones_texto))
]

# Encontrar la oración con mayor similitud semántica
max_similarity_index = cosine_similarities.index(max(cosine_similarities))
most_similar_sentence = oraciones_texto[max_similarity_index]

# Imprimir resultados
for i, sim in enumerate(cosine_similarities):
    print(f"Similitud Coseno con semantica entre la entrada del usuario y '{oraciones_texto[i]}': {sim}")

print(f"La oración con mayor similitud semántica es: '{most_similar_sentence}'")
print(f"La oración de input: '{uinput}'")

oraciones[most_similar_sentence]()




