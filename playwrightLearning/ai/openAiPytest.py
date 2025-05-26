import pytest
from browser_use import Agent
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

@pytest.mark.asyncio
async def test_way2automation():
    agent = Agent(

        task="""
                Open website http://qa.way2automation.com
                Enter name as Ivan Saff
                then Enter phone as 4654654313
                then Enter email as trainer@way2automation.com
                then select country as Japan
                then Enter city as Tokyo
                then Enter username as trainer@way2automation.com
                then ENter password kjslkdfjsl
                then click on Submit button
                then verify the message contains "This is just a dummy form, you just clicked SUBMIT BUTTON"
            """,
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key="AIzaSyAM4E_VxbUJ3-8dP-UUQ-NYlKoz3Q0i3Xk")

    )
    result = await agent.run()
    final_result = result.final_result()
    print(final_result)

    expected_message = "This is just a dummy form, you just clicked SUBMIT BUTTON"
    assert expected_message in final_result, f"Expected message not found! Actual result is: {final_result}"