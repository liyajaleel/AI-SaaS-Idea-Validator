# app.py

import streamlit as st
import pandas as pd
from orchestrator.agent_orchestrator import run_agents

# Page Config
st.set_page_config(
    page_title="AI SaaS Idea Validator",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI SaaS Idea Validator")
st.markdown("Validate your startup idea using AI-powered multi-agent analysis.")

# User Input
idea = st.text_input("Enter your Startup Idea")

if st.button("Validate Idea"):

    if not idea.strip():
        st.warning("Please enter a startup idea.")
    else:
        with st.spinner("Running multi-agent analysis..."):
            result = run_agents(idea)

        st.success("Analysis Completed Successfully!")

        # ==============================
        # Executive Summary
        # ==============================
        st.header("Executive Summary")
        st.write(
            f"The startup idea **'{idea}'** aims to address a growing market need "
            f"by leveraging AI-driven automation and digital transformation opportunities."
        )

        st.divider()

        # ==============================
        # Market Research
        # ==============================
        st.header("Market Research")
        st.markdown(result["market"])

        st.divider()

        # ==============================
        # Competitor Analysis
        # ==============================
        st.header("Competitor Landscape")

        competitor_df = pd.DataFrame(result["competitors"])
        st.table(competitor_df)

        st.divider()

        # ==============================
        # Monetization Strategy
        # ==============================
        st.header("Revenue Model Recommendation")
        st.markdown(result["monetization"])

        st.divider()

        # ==============================
        # Risk Assessment
        # ==============================
        st.header("Risk Assessment")

        risk_data = result["risk"]

        col1, col2, col3 = st.columns(3)

        col1.metric("Technical Risk", risk_data["Technical Risk"])
        col2.metric("Market Risk", risk_data["Market Risk"])
        col3.metric("Regulatory Risk", risk_data["Regulatory Risk"])

        st.subheader("Overall Risk Score")

        overall_risk = risk_data["Overall Risk Score"]

        if overall_risk == "Low":
            st.success("Low Risk ✅")
        elif overall_risk == "Medium":
            st.warning("Medium Risk ⚠")
        else:
            st.error("High Risk ❌")

        st.divider()

        # ==============================
        # Final Recommendation
        # ==============================
        st.header("Final Recommendation")

        if overall_risk == "Low":
            st.success("GO ✅ This idea shows strong potential with manageable risks.")
        elif overall_risk == "Medium":
            st.warning("Proceed with Caution ⚠ Consider refining differentiation strategy.")
        else:
            st.error("NO-GO ❌ High risk detected. Re-evaluate the concept.")

        st.divider()

        st.caption("AI SaaS Idea Validator | Multi-Agent System")