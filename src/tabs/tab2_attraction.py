"""
Tab 2: Attraction Science Hub
Research-backed insights on physical and behavioral attraction factors
"""
import streamlit as st
import json
import plotly.graph_objects as go
from design_system import COLORS, get_plotly_layout


def render():
    """Render the Attraction Science Hub tab"""
    st.header("💡 Attraction Science Hub")
    st.caption("Research-backed insights on what drives attraction")
    
    # Load research data
    with open('data/attraction_research.json', 'r') as f:
        data = json.load(f)
    
    # Physical factors section
    st.subheader("📏 Physical Attraction Factors")
    st.markdown("*Based on peer-reviewed research*")
    st.markdown("")
    
    for factor in data['physical_factors']:
        with st.expander(f"**{factor['factor']}**", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                <div style="
                    background: {COLORS['women_blue']}15;
                    border-left: 3px solid {COLORS['women_blue']};
                    padding: 15px;
                    border-radius: 6px;
                    margin-bottom: 10px;
                ">
                    <p style="color: {COLORS['women_blue']}; font-size: 12px; font-weight: 600; text-transform: uppercase; margin-bottom: 5px;">
                        👩 Women Prefer
                    </p>
                    <p style="color: {COLORS['text_primary']}; font-size: 14px; margin: 0;">
                        {factor['women_preference']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div style="
                    background: {COLORS['men_red']}15;
                    border-left: 3px solid {COLORS['men_red']};
                    padding: 15px;
                    border-radius: 6px;
                    margin-bottom: 10px;
                ">
                    <p style="color: {COLORS['men_red']}; font-size: 12px; font-weight: 600; text-transform: uppercase; margin-bottom: 5px;">
                        👨 Men Prefer
                    </p>
                    <p style="color: {COLORS['text_primary']}; font-size: 14px; margin: 0;">
                        {factor['men_preference']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"**📚 Research:** {factor['research']}")
            st.markdown(f"**🔍 Key Finding:** {factor['key_finding']}")
            st.info(f"💡 **Practical Tip:** {factor['practical_tip']}")
    
    st.markdown("---")
    
    # Behavioral factors section
    st.subheader("🎭 Behavioral Attraction Signals")
    st.markdown("*Traits that enhance interpersonal attraction*")
    st.markdown("")
    
    # Create radar chart
    traits = [item['trait'] for item in data['behavioral_factors']]
    scores = [item['attractiveness_score'] for item in data['behavioral_factors']]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=traits,
        fill='toself',
        fillcolor=f"rgba(0, 230, 118, 0.15)",
        line=dict(color=COLORS['green_primary'], width=3),
        marker=dict(size=8, color=COLORS['green_primary']),
        name='Attractiveness Score',
        hovertemplate='<b>%{theta}</b><br>Score: %{r}/10<extra></extra>'
    ))
    
    layout = get_plotly_layout()
    layout.update({
        'polar': {
            'bgcolor': COLORS['bg_card'],
            'radialaxis': {
                'visible': True,
                'range': [0, 10],
                'gridcolor': COLORS['border_default'],
                'tickfont': {'color': COLORS['text_secondary'], 'size': 10}
            },
            'angularaxis': {
                'gridcolor': COLORS['border_default'],
                'tickfont': {'color': COLORS['text_primary'], 'size': 11}
            }
        },
        'showlegend': False,
        'title': {
            'text': 'Attractiveness Ratings by Trait (0-10 scale)',
            'font': {'size': 18, 'color': COLORS['text_primary']},
            'x': 0.5,
            'xanchor': 'center'
        },
        'height': 500
    })
    
    fig.update_layout(**layout)
    st.plotly_chart(fig, use_container_width=True)
    
    # Behavioral traits details
    st.markdown("### ✅ How to Demonstrate These Traits")
    st.markdown("")
    
    for trait_data in data['behavioral_factors']:
        st.markdown(f"""
        <div style="
            background: {COLORS['bg_card']};
            border: 1px solid {COLORS['border_default']};
            border-radius: 8px;
            padding: 16px;
            margin: 10px 0;
        ">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h4 style="color: {COLORS['text_primary']}; margin: 0;">
                    {trait_data['trait']}
                </h4>
                <span style="
                    background: {COLORS['green_primary']}20;
                    color: {COLORS['green_primary']};
                    padding: 4px 12px;
                    border-radius: 12px;
                    font-size: 13px;
                    font-weight: 600;
                ">
                    {trait_data['attractiveness_score']}/10
                </span>
            </div>
            <p style="color: {COLORS['text_secondary']}; font-size: 13px; margin-bottom: 8px;">
                <strong>How to demonstrate:</strong> {trait_data['how_to_demonstrate']}
            </p>
            <p style="color: {COLORS['text_muted']}; font-size: 12px; margin: 0;">
                <em>{trait_data['gender_difference']}</em>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Key psychological principles
    st.subheader("🧠 Key Psychological Principles")
    st.markdown("*Fundamental concepts in attraction research*")
    st.markdown("")
    
    for insight in data['key_insights']:
        st.markdown(f"""
        <div style="
            background: {COLORS['bg_card']};
            border-left: 4px solid {COLORS['info']};
            padding: 16px;
            margin: 10px 0;
            border-radius: 0 8px 8px 0;
        ">
            <h4 style="color: {COLORS['text_primary']}; margin-top: 0; margin-bottom: 8px;">
                {insight['insight']}
            </h4>
            <p style="color: {COLORS['text_secondary']}; font-size: 14px; margin-bottom: 10px;">
                {insight['description']}
            </p>
            <div style="
                background: {COLORS['bg_primary']};
                padding: 10px;
                border-radius: 6px;
            ">
                <p style="color: {COLORS['green_primary']}; font-size: 13px; margin: 0;">
                    <strong>💡 Implication:</strong> {insight['implication']}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Bottom info
    st.info("📖 All insights are based on peer-reviewed research in psychology and behavioral science. Individual experiences may vary.")
