import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="prompt helper")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    api_key = os.environ.get("OPENROUTER_API_KEY")
    
    if not api_key:
        raise RuntimeError("API_KEY not found")
    
    
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key,)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    
    generate_content(client, messages, args.verbose)

def generate_content(client, messages, verbose):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
    )

    if not response.usage:
        raise RuntimeError("failed API request for usage")
    
    
        

    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    response_text = response.choices[0].message.content
    user_prompt = messages[1]["content"]
    
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {completion_tokens}")
        
    print(f"Response: {response_text}")
        

if __name__ == "__main__":
    main()
    

