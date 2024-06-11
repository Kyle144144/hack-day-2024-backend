# Note: The openai-python library support for Azure OpenAI is in preview.
# Note: This code sample requires OpenAI Python library version 1.0.0 or higher.
import os
from openai import AzureOpenAI
from azure.identity import ClientSecretCredential
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"],
)

# Token Scope
access_token = credential.get_token(
    "api://1ebe33bb-be81-4076-8064-a2e5d124fd7f/.default"
)

headers = {
    "Authorization": f"Bearer {access_token.token}",
    "content_type": "application/json",
}

client = AzureOpenAI(
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    default_headers=headers,
)


message_text = [
    {"role": "system", "message": "You are an AI assistant."},
    {
        "role": "user",
        "content": "write me a story about the fastest dog on planet earth.",
    },
]

completion = client.chat.completions.create(
    model="gpt-4o",  # model
    messages=message_text,
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
)


print(completion)
