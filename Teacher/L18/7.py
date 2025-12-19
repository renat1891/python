from openai import OpenAI, AsyncOpenAI
import asyncio  # Added import for asyncio



async def main():  # Fixed async function definition
    api_keys = {
        "github1": "f0af93f61ad44ceeb26a4aca6be8e75c",
        "github3": "74b0c0abd2294719ba29967c27bde367",
        "github5": "0710951b319a4cd79e155a8e40413658",
    }

    AIMLAPI_BASE_URL = "https://api.aimlapi.com/v1"

    client = AsyncOpenAI(
        base_url=AIMLAPI_BASE_URL,
        api_key=api_keys["github1"],
    )

    response = await asyncio.wait_for(
        client.chat.completions.create(
            model="openai/gpt-5-2",
            messages=[{"role": "user", "content": "Say OK"}],
            max_tokens=5
        ),
        timeout=15
    )
    print(response)  # Added print to display the response
    print(response.choices[0].message.content)  # Print the content of the message

# Run the async function
asyncio.run(main())