from strands import Agent
import logging

logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s", handlers=[logging.StreamHandler()]
)

agent = Agent(system_prompt=("You are a game master for a Dungeon & Dragon game"))

agent("Hi, I am an adventurer ready for adventure!")
