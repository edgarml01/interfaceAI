from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from SpeechToText import voice_to_text
from AIService import AIService

MODEL = "all-MiniLM-L6-v2"

def avg_cosine_similarity(userInput, sentences):
    model = SentenceTransformer(MODEL)  # Modelo 
    embeddings = model.encode(sentences)
    uEmbeddings = model.encode(userInput)

    # Calcular similitudes coseno entre uEmbeddings y cada oración en embeddings
    cosine_similarities = [
        cosine_similarity([uEmbeddings], [embeddings[i]])[0][0]
        for i in range(len(sentences))
    ]
    return sum(cosine_similarities) / len(cosine_similarities) if cosine_similarities else 0.0


def exect_order( sentences ) :
    """
        This function takes a dictionary of sentences and their corresponding functions.
        
        parameters:
            sentences: A dictionary where keys are sentences and values are functions to execute.
    """
    aiService = AIService() 
    model = SentenceTransformer(MODEL)  # Modelo 
    oraciones = sentences

    oraciones_texto = list(oraciones.keys())
    userInput = input("escribe la orden")
    averages = []

    for oracion in oraciones_texto:
        prompt = f"Dame un lista con  10 ordenes similares a la siguiente {oracion}. Las ordenes tienen que tener una similitud semantica alta con la orden original. Las ordenes tienen que ser diferentes entre si y no pueden ser iguales a la orden original. "
        list_of_sentences = aiService.ask_gemini_list(prompt)
        print(list_of_sentences)
        avg  = avg_cosine_similarity(userInput, list_of_sentences)
        averages.append(avg)
        print(f"Promedio de la oracion: {oracion} =  {avg}")
    #voice_to_text()

    print(f"Promedios de oraciones: ")
    print(averages)
    # Convertir frases en vectores numéricos
    embeddings = model.encode(oraciones_texto)
    uEmbeddings = model.encode(userInput)

    # Calcular similitudes coseno entre uEmbeddings y cada oración en embeddings
    cosine_similarities = [
        cosine_similarity([uEmbeddings], [embeddings[i]])[0][0]
        for i in range(len(oraciones_texto))
    ]
    cosine_similarities  = averages

    # Encontrar la oración con mayor similitud semántica
    max_similarity_index = cosine_similarities.index(max(cosine_similarities))
    most_similar_sentence = oraciones_texto[max_similarity_index]

    if (max(cosine_similarities) < 0.6):
        print("No se encontro una similitud suficiente")
        return


    # Imprimir resultados
    for i, sim in enumerate(cosine_similarities):
        print(f"Similitud Coseno con semantica entre la entrada del usuario y '{oraciones_texto[i]}': {sim}")

    print(f"La oración con mayor similitud semántica es: '{most_similar_sentence}'")
    print(f"La oración de input: '{userInput}'")

    oraciones[most_similar_sentence]()


