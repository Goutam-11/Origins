from crewai import Crew
from agents import setup_agents
from tasks import create_tasks


def create_crew(user_query):
    code_checker, trend_analyzer, implementation_advisor = setup_agents()
    tasks = create_tasks(user_query, code_checker, trend_analyzer, implementation_advisor)
    
    crew = Crew(
        agents=[code_checker, trend_analyzer, implementation_advisor],
        tasks=tasks,
        verbose=True
    )
    
    crew.kickoff()
    
    # Read raw text files
    def read_file(filename):
        with open(filename, 'r') as f:
            return f.read()
    
    return {
        "code_analyst": read_file("originality_report.txt"),
        "trend_analyst": read_file("trends_analysis.txt"),
        "implementation": read_file("implementation_plan.txt")
    }