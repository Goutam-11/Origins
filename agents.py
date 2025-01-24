from crewai import Agent
from crewai import LLM
import os
from tools import tool
from dotenv import load_dotenv

load_dotenv()
os.environ['GEMINI_API_KEY']=os.getenv('GOOGLE_API_KEY')
llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.7,
    max_tokens=4000,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    seed=42
)

def setup_agents():
    """Initialize and return all agents"""
    code_checker = Agent(
        role="Code Authenticity Analyst",
        goal="Check code originality and identify dependencies",
        verbose=True,
        memory=True,
        backstory="Expert in intellectual property verification and dependency analysis",
        llm=llm,
        tools=[tool],
        allow_delegation=False
    )

    trend_analyzer = Agent(
        role="Future Trends Specialist",
        goal="Analyze emerging technological trends",
        verbose=True,
        memory=True,
        backstory="Technology futurist with pattern recognition capabilities",
        llm=llm,
        tools=[tool],
        allow_delegation=False
    )

    implementation_advisor = Agent(
        role="Implementation Architect",
        goal="Develop future-proof implementation strategies",
        verbose=True,
        memory=True,
        backstory="Expert in sustainable technical solution design",
        llm=llm,
        tools=[tool],
        allow_delegation=False
    )

    return code_checker, trend_analyzer, implementation_advisor