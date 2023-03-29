import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()
secrets = None

# clear the screen initially
os.system('cls')  

# get OpenAI API credentials
try:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    prompt = ''
    
    while prompt != '2': 
        print("***********************************")
        print("**********OPENAI SEARCH************")
        print("***********************************")
        print("")
        
        prompt = input("Ask OpenAI something (1=cls, 2=end): ")
        
        if prompt == '1':
            os.system('cls')    
        elif (prompt != '2' and prompt != '1'):
            response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=1, max_tokens=200)
            
            print(f"\nresponse: {response.choices[0].text}")
            print("")
        
    print(f"OpenAI discussion ended.")
except Exception as e:
    print(f"An error occurred:{e}")