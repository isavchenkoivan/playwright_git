import json

import pytest
from browser_use import Agent
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from playwright.async_api import async_playwright
from langchain_openai import ChatOpenAI

@pytest.mark.asyncio
async def test_way2automation():
    agent = Agent(

        task="""
                Identify and return the HTML elements locators (CSS or Xpath) in JSON format ONLY
                for the following form fields https://demo.wpeverest.com/user-registration/simple-registration-form/
                THe output should be a valid JSON object without extra text and create CSS with attribute and value,
                like :
                {
                    "First Name": "CSS_SELECTOR",
                    "Last Name": "CSS_SELECTOR",
                    "User email": "CSS_SELECTOR",
                    "User password": "CSS_SELECTOR"
                }
            """,
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key="AIzaSyAM4E_VxbUJ3-8dP-UUQ-NYlKoz3Q0i3Xk")

    )
    result = await agent.run()
    final_result = result.final_result()
    print(final_result)

    try:
        final_result = json.loads(final_result)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON Response from AI: {final_result}")

    print("Extracted Locators are: ", final_result)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await  page.goto("https://demo.wpeverest.com/user-registration/simple-registration-form/")

        await page.fill(final_result["First Name"], "Ivan")
        await page.fill(final_result["Last Name"], "Saff")
        await page.fill(final_result["User email"], "rahul@way2automation.com")
        await page.fill(final_result["User password"], "sssdfdsfsdf")
        await page.wait_for_timeout(3000)
        await browser.close()