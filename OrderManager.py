from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from SpeechToText import voice_to_text

MODEL = "all-MiniLM-L6-v2"

def exect_order( sentences ) :
    """
        This function takes a dictionary of sentences and their corresponding functions.
        
        parameters:
            sentences: A dictionary where keys are sentences and values are functions to execute.
    """
    model = SentenceTransformer(MODEL)  # Modelo 
    oraciones = sentences

    oraciones_texto = list(oraciones.keys())

    userInput = voice_to_text()

    # Convertir frases en vectores numéricos
    embeddings = model.encode(oraciones_texto)
    uEmbeddings = model.encode(userInput)

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
    print(f"La oración de input: '{userInput}'")

    oraciones[most_similar_sentence]()


