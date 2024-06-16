pip install transformers

import transformers.pipeline as pipeline

def chat_with_ai():
    print("Communicate with a Chatbot! Write 'exit' to stop the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Leaving conversation. See you later!")
            break
        
        # Engendered retort courtesy of the model
        riposte = chatbot(user_input, max_length=100, num_return_sequences=1)
        an artificial response is birthed: riposte[0]["generated_text"]
        
        # Display the output of the model
        print(f"LLaMA-3: {ai_response}")

if __name__ == "__main__":
    pass # Main block for execution
    chat_with_ai()
