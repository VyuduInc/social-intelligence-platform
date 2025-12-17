"""
Tab 3: Social Skills Lab
Actionable communication guidance and body language decoding
"""
import streamlit as st
import json
from components import probability_bar
from design_system import COLORS


def render():
    """Render the Social Skills Lab tab"""
    st.header("🎭 Social Skills Lab")
    st.caption("Actionable guidance for better communication and connection")
    
    # Load skills data
    with open('data/social_skills.json', 'r') as f:
        data = json.load(f)
    
    # Communication tips section
    st.subheader("💬 Communication Effectiveness Guide")
    st.markdown("*Practical do's and don'ts for various dating scenarios*")
    st.markdown("")
    
    for tip in data['communication_tips']:
        with st.expander(f"**{tip['category']}** - Effectiveness: {tip['effectiveness']}/10", expanded=False):
            # Context info
            st.markdown(f"""
            <div style="
                background: {COLORS['bg_secondary']};
                padding: 8px 12px;
                border-radius: 6px;
                margin-bottom: 15px;
            ">
                <span style="color: {COLORS['text_secondary']}; font-size: 12px;">
                    📍 <strong>Best Context:</strong> {tip['context']}
                </span>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                <div style="
                    background: {COLORS['green_primary']}10;
                    border: 2px solid {COLORS['green_primary']};
                    border-radius: 8px;
                    padding: 15px;
                ">
                    <h4 style="color: {COLORS['green_primary']}; margin-top: 0; margin-bottom: 10px;">
                        ✅ DO
                    </h4>
                    <p style="color: {COLORS['text_primary']}; font-size: 14px; margin-bottom: 15px;">
                        {tip['do']}
                    </p>
                    <div style="
                        background: {COLORS['bg_primary']};
                        padding: 12px;
                        border-radius: 6px;
                        font-family: monospace;
                        font-size: 13px;
                        color: {COLORS['text_secondary']};
                        line-height: 1.5;
                    ">
                        "{tip['example_good']}"
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div style="
                    background: {COLORS['red_primary']}10;
                    border: 2px solid {COLORS['red_primary']};
                    border-radius: 8px;
                    padding: 15px;
                ">
                    <h4 style="color: {COLORS['red_primary']}; margin-top: 0; margin-bottom: 10px;">
                        ❌ DON'T
                    </h4>
                    <p style="color: {COLORS['text_primary']}; font-size: 14px; margin-bottom: 15px;">
                        {tip['dont']}
                    </p>
                    <div style="
                        background: {COLORS['bg_primary']};
                        padding: 12px;
                        border-radius: 6px;
                        font-family: monospace;
                        font-size: 13px;
                        color: {COLORS['text_secondary']};
                        line-height: 1.5;
                    ">
                        "{tip['example_bad']}"
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Effectiveness bar
            st.markdown("<br>", unsafe_allow_html=True)
            probability_bar(
                "Effectiveness Rating",
                int(tip['effectiveness'] * 10)
            )
    
    st.markdown("---")
    
    # Body language section
    st.subheader("👁️ Body Language Decoder")
    st.markdown("*Understanding and using non-verbal communication*")
    st.markdown("")
    
    for signal in data['body_language']:
        with st.container():
            # Use native Streamlit components instead of complex HTML
            st.markdown(f"### {signal['signal']}")
            
            # Meaning section
            st.markdown(f"**📍 Meaning**")
            st.write(signal['meaning'])
            
            # How to use section
            st.markdown(f"**✅ How to Use**")
            st.write(signal['how_to_use'])
            
            # Common mistake section
            st.warning(f"**⚠️ Common Mistake:** {signal['common_mistake']}")
            
            st.markdown("---")
    
    st.markdown("---")
    
    # Conversation starters
    st.subheader("🗨️ Conversation Starter Templates")
    st.markdown("*Context-appropriate ways to initiate conversations*")
    st.markdown("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: {COLORS['bg_card']};
            border: 1px solid {COLORS['border_default']};
            border-radius: 8px;
            padding: 16px;
            height: 100%;
        ">
            <h4 style="color: {COLORS['green_primary']}; margin-top: 0;">🎯 Situational</h4>
        """, unsafe_allow_html=True)
        for starter in data['conversation_starters']['situational']:
            st.markdown(f"""
            <div style="
                background: {COLORS['bg_primary']};
                padding: 10px;
                border-radius: 6px;
                margin: 8px 0;
                border-left: 2px solid {COLORS['green_primary']};
            ">
                <p style="color: {COLORS['text_secondary']}; font-size: 13px; margin: 0;">
                    "{starter}"
                </p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: {COLORS['bg_card']};
            border: 1px solid {COLORS['border_default']};
            border-radius: 8px;
            padding: 16px;
            height: 100%;
        ">
            <h4 style="color: {COLORS['info']}; margin-top: 0;">💡 Interest-Based</h4>
        """, unsafe_allow_html=True)
        for starter in data['conversation_starters']['interest_based']:
            st.markdown(f"""
            <div style="
                background: {COLORS['bg_primary']};
                padding: 10px;
                border-radius: 6px;
                margin: 8px 0;
                border-left: 2px solid {COLORS['info']};
            ">
                <p style="color: {COLORS['text_secondary']}; font-size: 13px; margin: 0;">
                    "{starter}"
                </p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="
            background: {COLORS['bg_card']};
            border: 1px solid {COLORS['border_default']};
            border-radius: 8px;
            padding: 16px;
            height: 100%;
        ">
            <h4 style="color: {COLORS['neutral']}; margin-top: 0;">🎪 Direct</h4>
        """, unsafe_allow_html=True)
        for starter in data['conversation_starters']['direct']:
            st.markdown(f"""
            <div style="
                background: {COLORS['bg_primary']};
                padding: 10px;
                border-radius: 6px;
                margin: 8px 0;
                border-left: 2px solid {COLORS['neutral']};
            ">
                <p style="color: {COLORS['text_secondary']}; font-size: 13px; margin: 0;">
                    "{starter}"
                </p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Common mistakes
    st.subheader("⚠️ Common Mistakes to Avoid")
    st.markdown("*Learn from these frequent social missteps*")
    st.markdown("")
    
    for mistake in data['common_mistakes']:
        st.markdown(f"""
        <div style="
            background: {COLORS['bg_card']};
            border: 1px solid {COLORS['red_primary']}40;
            border-radius: 8px;
            padding: 18px;
            margin: 12px 0;
        ">
            <h4 style="color: {COLORS['red_primary']}; margin-top: 0; margin-bottom: 10px;">
                ❌ {mistake['mistake']}
            </h4>
            <p style="color: {COLORS['text_secondary']}; font-size: 14px; margin-bottom: 10px;">
                <strong>Why it fails:</strong> {mistake['why_it_fails']}
            </p>
            <div style="
                background: {COLORS['green_primary']}10;
                border-left: 3px solid {COLORS['green_primary']};
                padding: 10px 15px;
                border-radius: 4px;
            ">
                <p style="color: {COLORS['text_primary']}; font-size: 13px; margin: 0;">
                    <strong>✅ Fix:</strong> {mistake['fix']}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Bottom note
    st.success("💪 Remember: Social skills improve with practice. Start with one or two techniques and gradually expand your toolkit.")
