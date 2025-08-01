
class staticproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func()



class Prompts:
    @staticproperty
    def search():
        with open("prompts/search.md", "r") as f:
            return f.read()
    
    @staticproperty
    def assistant():
        with open("prompts/assistant.md", "r") as f:
            return f.read()
    
    @staticproperty
    def spec():
        with open("prompts/spec.md", "r") as f:
            return f.read()

