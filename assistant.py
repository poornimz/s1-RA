import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client pointing to Google AI Studio's OpenAI-compatible endpoint
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def research_assistant():
    print("=== Terminal Research Assistant (Powered by Gemini) ===")
    print("Type your research topic or question (type 'exit' to quit).\n")
    
    while True:
        user_prompt = input("You: ")
        if user_prompt.lower() == 'exit':
            print("Goodbye!")
            break
        
        if not user_prompt.strip():
            continue

        try:
            print("\nThinking...")
            # Using Google's active free model
            response = client.chat.completions.create(
                model="gemini-3.8-flash",
                messages=[
                    {"role": "system", "content": "You are a helpful, concise research assistant."},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,
            )
            
            answer = response.choices[0].message.content
            print(f"\nAssistant:\n{answer}\n")
            print("-" * 50)
            
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")

if __name__ == "__main__":
    research_assistant()