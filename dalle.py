from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.images.generate(
    model="dall-e-2",
    prompt=input("Describe the image you want to generate:"),
    size="512x512",
    n=1,
 )

print(response.data[0].url)