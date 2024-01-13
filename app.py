from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()
secrets = None

# clear the screen initially
os.system('cls')  

# get OpenAI API credentials
try:
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.getenv("OPENAI_SECRET_FUCKING_KEY")
    )

    print(f"key: ${os.getenv("OPENAI_SECRET_FUCKING_KEY")}")
    
    prompt = ''
    
    while prompt != '2': 
        print("***********************************")
        print("**********OPENAI SEARCH************")
        print("***********************************\n\n")
        
        prompt = input("Ask OpenAI something (1=cls, 2=end): ")
        
        if prompt == '1':
            os.system('cls')    
        elif (prompt != '2' and prompt != '1'):
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="gpt-3.5-turbo"
            )
            
            print(f"\nresponse: {response.choices[0].message.content}")
            print("")
        
    print(f"OpenAI discussion ended.")
except Exception as e:
    print(f"An error occurred:{e}")