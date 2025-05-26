from browser_use import Agent
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


async def main():

    agent = Agent(

        task = """
            Open website http://qa.way2automation.com
            Enter name as Ivan Saff
            then Enter phone as 4654654313
            then Enter email as trainer@way2automation.com
        """,
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key="AIzaSyAM4E_VxbUJ3-8dP-UUQ-NYlKoz3Q0i3Xk")

    )
    await agent.run()
asyncio.run(main())
