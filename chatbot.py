from dotenv import load_dotenv
import os
import openai
import google.generativeai as genai

load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")
genai.configure(api_key=os.getenv("GEMINI_AI_API_KEY"))


messages =[{"role":"system","content":"you are a data science tutor who provides short,simple explanations."}]

def chatbot(prompt):
    messages.append({"role": "user", "content": prompt})

    response=openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5
    )
    reply=response.choices[0].message.content
    messages.append({"role":"assistant","content":reply})
    return reply

#gemini
model = genai.GenerativeModel("models/gemini-1.5-pro") 
history=["You are a data science tutor who provides short, simple explanations."]

def gemini_chatbot(prompt):
    history.append(f"User: {prompt}")
    full_prompt= "\n".join(history)
    response= model.generate_content(full_prompt)

    reply= response.text.strip()
    history.append(f"Assistant: {reply}")
    return reply

print("type 1 for open ai, type 2 for gemini")
model_choice = input("Your choice: ").strip()

if(model_choice=="1"):

    while(True):
        user_input= input("you: ")
        if user_input.lower() in ["quit","bye","exit"]:
            print("GoodBye!")
            break
        response=chatbot(user_input)
        print("chat:",response)

if(model_choice=="2"):
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            print("Goodbye!")
            break

        response = gemini_chatbot(user_input)
        print("GeminiBot:", response)







