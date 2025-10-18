import logging
import aiohttp  # Add this import at the top if not already there
import random
import asyncio
from supabase import create_client, Client
import os

from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    MetricsCollectedEvent,
    RoomInputOptions,
    RunContext,
    WorkerOptions,
    cli,
    function_tool,
    metrics,
)
from livekit.plugins import noise_cancellation, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

logger = logging.getLogger("agent")

load_dotenv(".env.local")
supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))



class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are a helpful voice AI assistant name Redef AI, you help people in productivity. The user is interacting with you via voice, even if you perceive the conversation as text.
            You eagerly assist users with their questions by providing information from your extensive knowledge.
            Your responses are concise, to the point, and without any complex formatting or punctuation including emojis, asterisks, or other symbols.
            You are curious, friendly, and have a sense of humor.""",
        )

    # To add tools, use the @function_tool decorator.
    # Here's an example that adds a simple weather tool.
    # You also have to add `from livekit.agents import function_tool, RunContext` to the top of this file
    @function_tool
    async def list_users(self):
        """Fetch a list of users from the Supabase 'users' table."""
        try:
            data = supabase.table("users").select("email").limit(5).execute()
            print(f"\n\n{data}\n\n")
            if not data.data:
                return "No users found in the database."
            return f"Found {len(data.data)} users. Example: {data.data}"
        except Exception as e:
            return f"Error fetching users: {str(e)}"

    @function_tool
    async def list_tasks(self):
        """Fetch a list of users tasks left """
        user_id = "01711181-d5f2-48ae-bf1e-ef7ad99f752a"
        try:
            data = supabase.table("tasks").select("id,name,category").eq("is_completed", False).limit(5).execute()
            print(f"\n\n{data}\n\n")
            if not data.data:
                return "No tasks found in the database."
            return f"Found {len(data.data)} tasks. Example: {data.data}"
        except Exception as e:
            return f"Error fetching tasks: {str(e)}"
    @function_tool
    async def list_deepwork(self):
        """Fetch how much time has the user worked in hours, user can call it like pomodoro also """
        try:
            data = supabase.table("pomodoros").select('focus_time').execute()
            total = 0
            print(data)
            for a in data.data:
                total += a['focus_time']
            
            print(f"\n\n{total}\n\n")
            if not data.data:
                return "No tasks found in the database."
            return f"total hours {int(total)/60}"
        except Exception as e:
            return f"Error fetching work hours: {str(e)}"

   
    @function_tool
    async def random_fact(self):
        """Fetches a random useless fact from a public API."""
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
        print("💕💕💕💕💕💕💕💕💕")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return "Sorry, I couldn't fetch a random fact right now."
                
                data = await response.json()
                print(data,"😘😘😘😘😘")
                return data.get("text", "No fact found.")

    @function_tool
    async def crypto_price(self, symbol: str = "bitcoin"):
        """Fetches the current price of a cryptocurrency (default: Bitcoin) in USD."""
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return f"Couldn't fetch price for {symbol}."
                data = await response.json()
                if symbol.lower() not in data:
                    return f"Symbol {symbol} not found."
                price = data[symbol.lower()]["usd"]
                return f"The current price of {symbol.capitalize()} is ${price}."


    # @function_tool
    # async def math_test(self, a: int, b: int):
    #     """A simple math test tool to confirm local computation works."""
    #     await asyncio.sleep(0.2)  # simulate some processing delay
    #     ops = ["+", "-", "*"]
    #     op = random.choice(ops)
    #     result = eval(f"{a}{op}{b}")
    #     return f"{a} {op} {b} = {result}"

    @function_tool
    async def lookup_weather(self, location: str):
        """Use this tool to look up current weather information in the given location.
    
        If the location is not supported by the weather service, the tool will indicate this. You must tell the user the location's weather is unavailable.
    
        Args:
            location: The location to look up weather information for (e.g. city name)
        """
    
        # logger.info(f"Looking up weather for {location}")
    
        return "sunny with a temperature of 70 degrees."


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    # Logging setup
    # Add any other context you want in all log entries here
    ctx.log_context_fields = {
        "room": ctx.room.name,
    }

    # Set up a voice AI pipeline using OpenAI, Cartesia, AssemblyAI, and the LiveKit turn detector
    session = AgentSession(
        # Speech-to-text (STT) is your agent's ears, turning the user's speech into text that the LLM can understand
        # See all available models at https://docs.livekit.io/agents/models/stt/
        stt="assemblyai/universal-streaming:en",
        # A Large Language Model (LLM) is your agent's brain, processing user input and generating a response
        # See all available models at https://docs.livekit.io/agents/models/llm/
        llm="openai/gpt-4.1-mini",
        # Text-to-speech (TTS) is your agent's voice, turning the LLM's text into speech that the user can hear
        # See all available models as well as voice selections at https://docs.livekit.io/agents/models/tts/
        tts="cartesia/sonic-2:9626c31c-bec5-4cca-baa8-f8ba9e84c8bc",
        # VAD and turn detection are used to determine when the user is speaking and when the agent should respond
        # See more at https://docs.livekit.io/agents/build/turns
        turn_detection=MultilingualModel(),
        vad=ctx.proc.userdata["vad"],
        # allow the LLM to generate a response while waiting for the end of turn
        # See more at https://docs.livekit.io/agents/build/audio/#preemptive-generation
        preemptive_generation=True,
    )

    # To use a realtime model instead of a voice pipeline, use the following session setup instead.
    # (Note: This is for the OpenAI Realtime API. For other providers, see https://docs.livekit.io/agents/models/realtime/))
    # 1. Install livekit-agents[openai]
    # 2. Set OPENAI_API_KEY in .env.local
    # 3. Add `from livekit.plugins import openai` to the top of this file
    # 4. Use the following session setup instead of the version above
    # session = AgentSession(
    #     llm=openai.realtime.RealtimeModel(voice="marin")
    # )

    # Metrics collection, to measure pipeline performance
    # For more information, see https://docs.livekit.io/agents/build/metrics/
    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage: {summary}")

    ctx.add_shutdown_callback(log_usage)

    # # Add a virtual avatar to the session, if desired
    # # For other providers, see https://docs.livekit.io/agents/models/avatar/
    # avatar = hedra.AvatarSession(
    #   avatar_id="...",  # See https://docs.livekit.io/agents/models/avatar/plugins/hedra
    # )
    # # Start the avatar and wait for it to join
    # await avatar.start(session, room=ctx.room)

    # Start the session, which initializes the voice pipeline and warms up the models
    await session.start(
        agent=Assistant(),
        room=ctx.room,
        room_input_options=RoomInputOptions(
            # For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    # Join the room and connect to the user
    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
