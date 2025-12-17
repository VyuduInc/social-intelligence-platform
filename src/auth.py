"""
Authentication module - Simple session-based access gate
"""
import streamlit as st
from design_system import COLORS


def check_access():
    """
    Simple session-based password gate
    Blocks all content until user enters correct access code
    """
    # Initialize session state
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    
    # If not authenticated, show login screen
    if not st.session_state['authenticated']:
        show_login_screen()
        st.stop()


def show_login_screen():
    """
    Display the Polymarket-style login screen
    """
    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Logo/Icon
        st.markdown(f"""
        <div style="text-align: center; margin-top: 80px; margin-bottom: 40px;">
            <div style="
                width: 80px;
                height: 80px;
                background: linear-gradient(135deg, {COLORS['green_primary']} 0%, {COLORS['green_secondary']} 100%);
                border-radius: 16px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                font-size: 40px;
                margin-bottom: 24px;
            ">
                🔐
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Title
        st.markdown(f"""
        <h1 style="
            color: {COLORS['text_primary']};
            font-size: 32px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 8px;
        ">
            Social Intelligence Platform
        </h1>
        """, unsafe_allow_html=True)
        
        # Subtitle
        st.markdown(f"""
        <p style="
            color: {COLORS['text_secondary']};
            font-size: 16px;
            text-align: center;
            margin-bottom: 40px;
        ">
            Data-driven insights on dating, attraction, and social dynamics
        </p>
        """, unsafe_allow_html=True)
        
        # Access code input
        password = st.text_input(
            "Enter Access Code",
            type="password",
            key="access_code_input",
            label_visibility="visible"
        )
        
        # Login button
        if st.button("🚀 Access Dashboard", use_container_width=True, type="primary"):
            if password == st.secrets["ACCESS_CODE"]:
                st.session_state['authenticated'] = True
                st.rerun()
            else:
                st.error("❌ Invalid access code. Please try again.")
        
        # Footer hint
        st.markdown(f"""
        <p style="
            color: {COLORS['text_muted']};
            font-size: 12px;
            text-align: center;
            margin-top: 40px;
        ">
            Don't have an access code? Contact the administrator.
        </p>
        """, unsafe_allow_html=True)
