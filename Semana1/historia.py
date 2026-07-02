# Paso 1, generar una historia corta 100 palabras como mucho y guardarla en una variable.

# Paso 2, ir generando instrucciones para responder de cirta forma sobre la pregunta

# ir agregando items

# - quiero una respuesta concisa
# - responde ademas del texto utilizando emojis que resuman la respuesta
# - responde en tercera persona
# - responde en el idioma que te pregunta el usuario



import cohere
## bloque variables de entorno
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

api_key = os.getenv("COHERE_API_KEY")


co = cohere.ClientV2(api_key=api_key)


historia = """Ian, un hombre de las cavernas inteligente, vivía en Bedrock con su familia./
             mañana soleada, descubrió una huella misteriosa que conducía a un cañón oculto./
            , Ian siguió el rastro, encontrando un cristal brillante que brillaba en la noche./
            Lo llevó a casa, y el cristal alimentó su televisor de piedra, mostrando dinosaurios danzantes./
             vecinos se reunieron, asombrados, mientras Ian usaba el cristal para iluminar todo el pueblo./
            El Gran Gazoo apareció, ofreciendo un trueque: un club dorado a cambio del cristal. /
            Ian, sabiamente, se negó, compartiendo la luz del cristal con todos, haciendo que Bedrock fuera más brillante que nunca. /
             pueblo celebró la amabilidad de Ian, y la paz floreció bajo las estrellas centelleantes para siempre./"""


system_prompt = f"""Respondele al usuario en base a la siguient historia = {historia}.
                     Segui las siguientes instrucciones
                     - Responde de manera conrta y concisa
                     - Responde usando emojis"""


response = co.chat(
    model="command-a-plus-05-2026",
    messages=[{"role": "system", "content": system_prompt},
    {"role": "user", "content": "Quien es Ian?"},
    ],
)

print(response.message.content[1].text)