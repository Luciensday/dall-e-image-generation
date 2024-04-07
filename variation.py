from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.images.create_variation(
  image=open("Coconut.png", "rb"),
  n=1,
  size="1024x1024"
)

print(f"Variation: {response.data[0].url}")