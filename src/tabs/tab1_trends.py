"""
Tab 1: Social Trends Monitor
Displays curated trending topics with sentiment analysis and gender comparisons
"""
import streamlit as st
import json
import pandas as pd
from components import metric_card, gender_comparison_chart, sentiment_indicator
from design_system import COLORS


def render():
    """Render the Social Trends Monitor tab"""
    st.header("🔥 Social Trends Monitor")
    st.caption("Curated trending topics in dating & relationships")
    
    # Load mock data
    with open('data/mock_trends.json', 'r') as f:
        data = json.load(f)
    
    # Top metrics row
    st.markdown("### Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        metric_card(
            "Active Topics",
            str(data['engagement_stats']['total_discussions']),
            f"+{data['engagement_stats']['weekly_growth']}",
            "vs last week",
            True
        )
    
    with col2:
        avg_sent = data['engagement_stats']['avg_sentiment']
        metric_card(
            "Avg Sentiment",
            f"{avg_sent:+.2f}",
            f"{abs(avg_sent - 0.25):.2f}",
            "vs baseline",
            avg_sent > 0.25
        )
    
    with col3:
        metric_card(
            "Peak Activity",
            data['engagement_stats']['peak_hours'],
            "2 hrs",
            "window",
            True
        )
    
    with col4:
        metric_card(
            "Engagement",
            "2.4K",
            "+18%",
            "comments",
            True
        )
    
    st.markdown("---")
    
    # Trending topics table
    st.subheader("📊 Top Trending Topics")
    st.caption("Ranked by discussion volume and velocity")
    
    # Prepare data
    df = pd.DataFrame(data['trends'][:15])
    
    # Create display dataframe
    display_df = pd.DataFrame({
        'Rank': range(1, len(df) + 1),
        'Topic': df['topic'],
        'Volume': df['volume'],
        'Sentiment': df['sentiment'].apply(lambda x: f"{x:+.2f}"),
        'Velocity': df['velocity'].apply(lambda x: f"{x:+.1f}%"),
        'Peak Time': df['peak_time']
    })
    
    # Style the dataframe
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Rank": st.column_config.NumberColumn(
                "Rank",
                width="small"
            ),
            "Topic": st.column_config.TextColumn(
                "Topic",
                width="large"
            ),
            "Volume": st.column_config.NumberColumn(
                "Volume",
                format="%d"
            ),
            "Sentiment": st.column_config.TextColumn(
                "Sentiment"
            ),
            "Velocity": st.column_config.TextColumn(
                "Velocity"
            ),
            "Peak Time": st.column_config.TextColumn(
                "Peak Time",
                width="small"
            )
        }
    )
    
    st.markdown("---")
    
    # Gender interest comparison
    st.subheader("⚖️ Gender Interest Comparison")
    st.caption("Which topics resonate more with women vs men")
    
    # Select top 8 topics for visualization
    topics_sample = df.iloc[:8]
    topics = [t[:30] + '...' if len(t) > 30 else t for t in topics_sample['topic']]
    women = topics_sample['women_interest'].tolist()
    men = topics_sample['men_interest'].tolist()
    
    fig = gender_comparison_chart(
        topics,
        women,
        men,
        "Interest Level by Gender (%)"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Top keywords by gender
    st.subheader("🔑 Top Keywords by Gender")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: {COLORS['bg_card']};
            border: 2px solid {COLORS['women_blue']};
            border-radius: 12px;
            padding: 20px;
        ">
            <h3 style="color: {COLORS['women_blue']}; margin-top: 0;">👩 Women's Interests</h3>
        """, unsafe_allow_html=True)
        
        for i, keyword in enumerate(data['top_keywords']['women'], 1):
            st.markdown(f"""
            <div style="
                background: {COLORS['bg_primary']};
                padding: 10px 15px;
                margin: 8px 0;
                border-radius: 6px;
                border-left: 3px solid {COLORS['women_blue']};
            ">
                <span style="color: {COLORS['text_secondary']}; font-size: 12px;">#{i}</span>
                <span style="color: {COLORS['text_primary']}; font-size: 14px; margin-left: 10px; font-weight: 500;">
                    {keyword}
                </span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: {COLORS['bg_card']};
            border: 2px solid {COLORS['men_red']};
            border-radius: 12px;
            padding: 20px;
        ">
            <h3 style="color: {COLORS['men_red']}; margin-top: 0;">👨 Men's Interests</h3>
        """, unsafe_allow_html=True)
        
        for i, keyword in enumerate(data['top_keywords']['men'], 1):
            st.markdown(f"""
            <div style="
                background: {COLORS['bg_primary']};
                padding: 10px 15px;
                margin: 8px 0;
                border-radius: 6px;
                border-left: 3px solid {COLORS['men_red']};
            ">
                <span style="color: {COLORS['text_secondary']}; font-size: 12px;">#{i}</span>
                <span style="color: {COLORS['text_primary']}; font-size: 14px; margin-left: 10px; font-weight: 500;">
                    {keyword}
                </span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Insights section
    st.subheader("💡 Key Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="
            background: {COLORS['bg_card']};
            border: 1px solid {COLORS['border_default']};
            border-radius: 8px;
            padding: 16px;
        ">
            <h4 style="color: {COLORS['text_primary']}; margin-top: 0;">📈 Most Positive Sentiment</h4>
            <p style="color: {COLORS['text_secondary']};">Topics around emotional intelligence and vulnerability show the highest positive sentiment (+0.85), suggesting growing value on emotional connection.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: {COLORS['bg_card']};
            border: 1px solid {COLORS['border_default']};
            border-radius: 8px;
            padding: 16px;
        ">
            <h4 style="color: {COLORS['text_primary']}; margin-top: 0;">🔍 Biggest Gender Gap</h4>
            <p style="color: {COLORS['text_secondary']};">Physical fitness discussions show 84% male interest vs 38% female, indicating different priorities in early attraction signals.</p>
        </div>
        """, unsafe_allow_html=True)
