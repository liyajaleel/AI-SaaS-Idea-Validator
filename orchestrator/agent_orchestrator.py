# orchestrator/agent_orchestrator.py

from agents.market_agent import market_research
from agents.competitor_agent import competitor_analysis
from agents.monetization_agent import monetization_strategy
from agents.risk_agent import risk_assessment

def run_agents(startup_idea):

    market = market_research(startup_idea)
    competitors = competitor_analysis(startup_idea)
    monetization = monetization_strategy(startup_idea)
    risk = risk_assessment(startup_idea)

    return {
        "market": market,
        "competitors": competitors,
        "monetization": monetization,
        "risk": risk
    }