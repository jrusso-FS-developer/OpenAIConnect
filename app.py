import openai
import json

secrets = None

# get OpenAI API credentials
try:
    
    openai.api_key = "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"
    
    prompt = ''
    
    while prompt != 'end': 
        prompt = input("Ask OpenAI something (type 'end' to quit): ")
    
        if (prompt != 'end'):
            response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
            
            print(f"response: {json.dumps(response.choices)}")
        
    print(f"OpenAI discussion ended.")
except Exception as e:
    print(f"An error occurred:{e.args[0]}")