"""
Social Intelligence Platform - Phase 1
Main application entry point with access gate and tab navigation
"""
import streamlit as st
import sys
from pathlib import Path

# Add src directory to path for imports
src_path = Path(__file__).parent
sys.path.insert(0, str(src_path))

from auth import check_access
from tabs import tab1_trends, tab2_attraction, tab3_skills
from design_system import COLORS


# Page configuration
st.set_page_config(
    page_title="Social Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "Social Intelligence Platform - Data-driven insights on dating & relationships"
    }
)

# Load custom CSS
try:
    with open('assets/custom.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    pass  # CSS is optional

# Check access gate
check_access()

# Header
st.markdown(f"""
<div style="
    background: linear-gradient(135deg, {COLORS['bg_secondary']} 0%, {COLORS['bg_primary']} 100%);
    padding: 30px 20px;
    border-radius: 12px;
    margin-bottom: 30px;
    border: 1px solid {COLORS['border_default']};
">
    <h1 style="
        color: {COLORS['text_primary']};
        font-size: 36px;
        font-weight: 700;
        margin: 0 0 10px 0;
    ">
        📊 Social Intelligence Platform
    </h1>
    <p style="
        color: {COLORS['text_secondary']};
        font-size: 16px;
        margin: 0;
    ">
        Data-driven insights on dating, attraction, and social dynamics
    </p>
</div>
""", unsafe_allow_html=True)

# Tab navigation
tab1, tab2, tab3 = st.tabs([
    "🔥 Social Trends",
    "💡 Attraction Science",
    "🎭 Social Skills"
])

with tab1:
    tab1_trends.render()

with tab2:
    tab2_attraction.render()

with tab3:
    tab3_skills.render()

# Footer
st.markdown("---")
st.markdown(f"""
<div style="
    text-align: center;
    padding: 20px;
    color: {COLORS['text_muted']};
    font-size: 13px;
">
    <p style="margin: 0;">
        Powered by research-backed insights • <strong>Vyudu Inc</strong>
    </p>
    <p style="margin: 5px 0 0 0; font-size: 11px;">
        Phase 1: Curated Data • Access Code: vyudu2024
    </p>
</div>
""", unsafe_allow_html=True)
