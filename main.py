# Charger les variables d'environnement
from dotenv import load_dotenv
load_dotenv()

# Créer une instance de OpenAI_LLM avec les paramètres souhaités
llm = OpenAI_LLM(
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=1500,
    stream=True
)



# Créer une instance de Function_Router_LLM avec le dictionnaire des fonctions
router_llm = Function_Router_LLM(
    functions_dict=functions_dict,
    model="gpt-4o-mini",
    temperature=0.2,
    stream=False
)

# Créer une instance de Enhanced_OpenAI_Chatbot en utilisant le LLM et le router
chatbot = Enhanced_OpenAI_Chatbot(
    llm=llm,
    router_llm=router_llm,
    functions_dict=functions_dict,
    system_prompt="Tu es un assistant qui est en agent, pour ton info nous sommes le 28 novembre 2024, et tu utilise info donnée dans context de quesiton poour repondre"
)

