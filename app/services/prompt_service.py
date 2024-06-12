


class PromptService:
    def __init__(self):
        self.prompt_template = ""
        self.prompt_input = ""
        self.prompt_examples = ""
        self.prompt_output = ""

    def set_prompt_template(self, template):
        self.prompt_template = template

    def set_prompt_input(self, input):
        self.prompt_input = input

    def set_prompt_examples(self, examples):
        self.prompt_examples = examples

    def generate_prompt(self):
        if '{}' in self.prompt_template:  # Checking if the template has placeholders
            self.prompt_output = self.prompt_template.format(self.prompt_input, self.prompt_examples)
        else:
            raise ValueError("Template must include placeholders for input and examples")
        return self.prompt_output
        
