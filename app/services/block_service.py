from services.prompt_service import PromptService
from services.llm_service import LLMService

class LMBlock ():
    def __init__(self, model_name, prompt, rag):
        self.model_name = model_name
        self.prompt = prompt
        self.rag = rag
        

        def createPrompt(self):
            prompt = PromptService()
            self.prompt = prompt
            


        def createLLM(self):
            llm = LLMService(self.model_name, self.prompt)
           