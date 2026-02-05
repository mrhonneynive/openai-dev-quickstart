from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Who is this magnificent and exceptional scholar? (who is just as good as the prophets of Isrealites [not better though)",
                },
                {
                    "type": "input_image",
                    "image_url": "https://img-s1.onedio.com/id-61e08c246c5638aa3849c85a/rev-0/w-600/h-802/f-jpg/s-a3ef597587bcfb9d3f9516178458627a91bc7188.jpg"
                }
            ]
        }
    ]
)

print(response.output_text)