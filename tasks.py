from crewai import Task
from tools import tool

def create_tasks(user_query, code_checker, trend_analyzer, implementation_advisor):
    """Create tasks with raw text output"""
    originality_task = Task(
        description=f"Analyze originality: {user_query}",
        agent=code_checker,
        tools=[tool],
        expected_output="""Formatted text report with:
        - Originality status header
        - Bullet points of dependencies
        - Plagiarism likelihood estimate""",
        output_file="originality_report.txt"
    )

    trends_task = Task(
        description=f"Analyze trends: {user_query}",
        agent=trend_analyzer,
        tools=[tool],
        expected_output="""Structured text report with:
        ## AI Trends
        - List item 1
        - List item 2
        
        ## ZK Trends
        - List item 1
        - List item 2""",
        output_file="trends_analysis.txt"
    )

    implementation_task = Task(
        description=f"Create implementation: {user_query}",
        agent=implementation_advisor,
        tools=[tool],
        expected_output="""Step-by-step guide:
        1. Phase 1: Description
        2. Phase 2: Description
        
        Technologies:
        - Tech 1
        - Tech 2
        
        Challenges:
        - Challenge 1
        - Challenge 2""",
        output_file="implementation_plan.txt"
    )

    return originality_task, trends_task, implementation_task