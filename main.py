import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts.prompts import system_prompt
from call_functions import available_functions, call_function


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
contents = args.user_prompt
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
)
if args.verbose:
    print(f"User prompt: {contents}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print("Response")
if response.function_calls is None:
    print(response.text)
else:
    for func_call in response.function_calls:
        function_call_result = call_function(func_call, args.verbose)

        if len(function_call_result.parts) == 0:
            raise Exception("Something went wrong")

        if function_call_result.parts[0].function_response is None:
            raise Exception("Something went wrong")

        if function_call_result.parts[0].function_response.response is None:
            raise Exception("Something went wrong")

        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

