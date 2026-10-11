import asyncio, os, logging
logging.getLogger("agent_framework").setLevel(logging.ERROR)
from agent_framework import Agent, tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

client = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

@tool(approval_mode="never_require")
def get_destinations() -> list[str]:
    """Get a list of popular vacation destinations."""
    print("  [tool] get_destinations() được gọi")
    return ["Barcelona", "Paris", "Berlin", "Tokyo", "Sydney",
            "New York City", "Cairo", "Cape Town", "Rio de Janeiro", "Bali"]

agent = Agent(
    client=client,
    name="TravelAgent",
    instructions=("You are a helpful travel agent. Help users find their perfect vacation "
                  "destination based on their preferences. Use the get_destinations tool "
                  "to see available destinations."),
    tools=[get_destinations],
)

async def main():
    print("=== run ===")
    r = await agent.run("I'm looking for a warm beach destination. What do you recommend?")
    print(r)
    print("usage:", getattr(r, "usage_details", None))
    print("\n=== stream ===")
    async for chunk in agent.run("Tell me about Tokyo as a travel destination in 3 sentences", stream=True):
        print(chunk, end="", flush=True)
    print()

asyncio.run(main())
