#import LLM software
#lookup what is this code doing
from langchain_ollama import OllamaLLM
"""""
#prompt template
#Langchain allows us to more easily interact with LLM
#Create a template that will be passed through llama3 that 
contains our specfiic query or prompt(Giving it more
description and instruction on what it should do)"""

#Template on how the model should behave and respond to my queries
from langchain_core.prompts import ChatPromptTemplate
template = """
Answer the question below.

Here is the conversation history. {context}

Question: {question}

Answer: 
"""

#specify/Call our model
model = OllamaLLM(model="llama3")
prompt =ChatPromptTemplate.from_template(template)
#Chain the model and prompt together

#what does the pipe operate mean in python
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI Chatbot! Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input })
        print("Bot: ", result)

        #Store all the history in the context 
        context += f"\nUser: {user_input} \nAI:{result}"
#calls the mode/use model

#call the conversation
if __name__  == "__main__":
    handle_conversation()