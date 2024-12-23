import anthropic
import os

client = anthropic.Client(
    api_key=os.environ.get('ANTHROPIC_API_KEY')
)

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    temperature=0.3,
    messages=[
        {
            "role": "user",
            "content": "Can you write a story about a dog getting a great birthday gift",
        }
    ],
    tools=[{
        "name": "responder",
        "description": "Responding to questions without introductory confirmations, concluding remarks, or follow-up questions",
        "input_schema": {
            "type": "object",
            "properties": {
                "response": {
                    "type": "string",
                    "description": "Response, without introductory confirmations, concluding remarks, or follow-up questions"
                }
            }
        }
    }],
    tool_choice={"type": "tool", "name": "responder"}
)

print(message.content[0].input["response"])