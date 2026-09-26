import openai

# Set your OpenAI API key
openai.api_key = "sk-proj-jRoUHs7iI4bKRgOh5vCmT3BlbkFJaCFazNP8yV1u25eLeolG"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        model="gpt",  # Adjust the model as per your needs
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Main interaction loop
def main():
    print("Welcome to the Chatbot! Type 'quit', 'bye', or 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            print("Chatbot: Goodbye!")
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
