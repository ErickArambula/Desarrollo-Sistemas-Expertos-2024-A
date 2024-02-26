class ChatBot:
    def __init__(self):
        self.responses = {
            "hola": "¡Hola! ¿Cómo estás?",
            "bien": "Me alegra escuchar eso.",
            "mal": "Espero que te sientas mejor pronto.",
            "de que te gustaría hablar": "Estoy aquí para ayudarte. ¿Sobre qué te gustaría hablar?",
            "default": "Lo siento, no entendí. ¿Me puedes explicar?"
        }
        self.new_knowledge_question = "¿Puedes proporcionarme información adicional sobre eso?"

    def respond(self, user_input):
        if user_input.lower() in self.responses:
            return self.responses[user_input.lower()]
        else:
            return self.new_knowledge_question

def main():
    chatbot = ChatBot()
    print("¡Hola! Soy un chatbot. ¿En qué puedo ayudarte hoy?")
    while True:
        user_input = input("> ")
        response = chatbot.respond(user_input)
        print(response)

if __name__ == "__main__":
    main()
