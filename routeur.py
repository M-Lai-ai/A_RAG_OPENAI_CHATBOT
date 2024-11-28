class Function_Router_LLM(OpenAI_LLM):
    def __init__(self, functions_dict: Dict[int, Dict], **kwargs):
        super().__init__(**kwargs)
        self.functions_dict = functions_dict
        # Créer le prompt pour décrire les fonctions disponibles
        self.functions_description = self._create_functions_description()

    def _create_functions_description(self) -> str:
        description = "Vous êtes un routeur qui analyse les questions et décide quelle fonction utiliser.\n"
        description += "Répondez uniquement avec un dictionnaire JSON contenant:\n"
        description += "- 'function_id': le numéro de la fonction à utiliser (0 si aucune fonction nécessaire)\n"
        description += "- 'input': les paramètres d'entrée pour la fonction si applicable\n\n"
        description += "Fonctions disponibles:\n"
        description += "0: Aucune fonction - répondre directement à la question\n"
        
        for func_id, func_info in self.functions_dict.items():
            description += f"{func_id}: {func_info['description']}\n"
            description += f"   Paramètres attendus: {func_info['parameters']}\n"
        
        return description

    def route_question(self, question: str) -> Dict:
        """Analyse la question et retourne l'ID de la fonction à utiliser et ses paramètres pour ton info nous sommes le 28 novembre 2024"""
        messages = [
            {"role": "system", "content": self.functions_description},
            {"role": "user", "content": question}
        ]
        
        # Désactiver le streaming pour cette requête
        original_stream = self.stream
        self.stream = False
        
        try:
            response = self._make_request(messages)
            response_data = response.json()
            response_text = response_data["choices"][0]["message"]["content"]
            return json.loads(response_text)
        except Exception as e:
            print(f"Erreur lors du routage: {e}")
            return {"function_id": 0, "input": None}
        finally:
            self.stream = original_stream
