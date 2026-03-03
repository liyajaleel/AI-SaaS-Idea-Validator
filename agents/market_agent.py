# agents/market_agent.py

from utils.search_tool import search_web

def market_research(startup_idea):
    query = f"Market size and industry trends for {startup_idea}"
    results = search_web(query)

    analysis = f"""
    Market Analysis for {startup_idea}

    - Estimated TAM: $5B+
    - Estimated SAM: $1B
    - Estimated SOM: $100M
    - Growing at ~12% CAGR
    - Target Audience: SMEs, Tech startups, Digital consumers
    """

    return analysis