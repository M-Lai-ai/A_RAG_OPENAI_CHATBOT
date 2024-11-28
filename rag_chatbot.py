class Enhanced_OpenAI_Chatbot(OpenAI_Chatbot):
    def __init__(
        self,
        llm: OpenAI_LLM,
        router_llm: Function_Router_LLM,
        functions_dict: Dict[int, Dict],
        **kwargs
    ):
        super().__init__(llm=llm, **kwargs)
        self.router_llm = router_llm
        self.functions_dict = functions_dict

    def execute_function(self, function_id: int, function_input: Dict) -> str:
        """Exécute la fonction spécifiée avec les paramètres donnés"""
        if function_id not in self.functions_dict:
            return f"Erreur: Fonction {function_id} non trouvée"
        
        try:
            func = self.functions_dict[function_id]["function"]
            result = func(**function_input)
            return str(result)
        except Exception as e:
            return f"Erreur lors de l'exécution de la fonction {function_id}: {e}"

    def __call__(self, message: str) -> str:
        # Utiliser le router pour déterminer quelle fonction utiliser
        route_result = self.router_llm.route_question(message)
        function_id = route_result.get("function_id", 0)
        function_input = route_result.get("input")

        # Si function_id est 0, traiter normalement
        if function_id == 0:
            return super().__call__(message)

        # Sinon, exécuter la fonction et inclure le résultat dans le contexte
        function_result = self.execute_function(function_id, function_input)
        enhanced_message = f"""Question: {message}
Résultat de la fonction {function_id}: {function_result}
Veuillez répondre à la question en utilisant ces informations."""

        return super().__call__(enhanced_message)
