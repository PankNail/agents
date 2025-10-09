from dotenv import load_dotenv
from agents import Agent, Runner, trace

load_dotenv(override=True)

async def main():
    agent = Agent(name="ShortStoryTeller", instructions="You are a short story teller. your story should be maximum 100 words long.", model="gpt-4o-mini")

    with trace("Telling a story"):    
        result = await Runner.run(agent, "Tell a story for 7 year old kid to learn gratefullness")
        print(result.final_output)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

