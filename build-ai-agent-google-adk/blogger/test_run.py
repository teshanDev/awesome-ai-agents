import asyncio
import os
from agent import root_agent
from google.adk.engine import LlmEngine
from google.adk.context import RunContext

async def main():
    print("Running the Blogger agent...")
    result = await root_agent.run("Write a blog post about the benefits of using AI agents for automating repetitive tasks. Keep it concise.")
    print("Agent Result:\n", result)

if __name__ == "__main__":
    asyncio.run(main())
