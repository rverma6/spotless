import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

def test_api_key():
    # Get the API key
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ API key not found! Check your .env file.")
        return
    
    # Initialize OpenAI client
    try:
        client = OpenAI(api_key=api_key)
        
        # Test a simple API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello!"}],
            max_tokens=10
        )
        
        print("✅ API key is valid and working!")
        print("Test response received:", response.choices[0].message.content)
        
    except Exception as e:
        print("❌ Error testing API key:", str(e))

if __name__ == "__main__":
    test_api_key() 