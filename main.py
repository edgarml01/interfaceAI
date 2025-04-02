from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(sentence1, sentence2):
    # Convertir a vectores TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([sentence1, sentence2])

    # Calcular similitud coseno
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return cosine_sim[0][0]
# Oraciones a comparar

sentence1 = "Me gusta programar en python"
sentence2 = "Me gusta programar"

similitud = calculate_cosine_similarity(sentence1, sentence2)

print("Similitud Coseno:", similitud)


