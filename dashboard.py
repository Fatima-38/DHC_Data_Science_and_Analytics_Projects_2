
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ─── Page Config ───────────────────────────────────────────
st.set_page_config(
    page_title="Global Superstore Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ────────────────────────────────────────────
st.markdown(
    """
    <style>
    .metric-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.2rem 1.5rem; border-radius: 12px; color: white;
        text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    .metric-card h2 { font-size: 2rem; margin: 0; }
    .metric-card p  { margin: 0; opacity: 0.85; font-size: 0.9rem; }
    .metric-green  { background: linear-gradient(135deg, #11998e, #38ef7d); }
    .metric-orange { background: linear-gradient(135deg, #f093fb, #f5576c); }
    .metric-blue   { background: linear-gradient(135deg, #4facfe, #00f2fe); }
    .metric-purple { background: linear-gradient(135deg, #667eea, #764ba2); }
    </style>
    """,
    unsafe_allow_html=True
)
