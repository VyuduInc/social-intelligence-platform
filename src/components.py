"""
Reusable UI Components - Polymarket-style design
"""
import streamlit as st
import plotly.graph_objects as go
from design_system import COLORS, get_plotly_layout


def metric_card(label, value, change_value, change_label, is_positive=True):
    """
    Large Polymarket-style metric card
    Args:
        label: Metric label (e.g., "Active Topics")
        value: Main value to display (e.g., "87")
        change_value: Change indicator (e.g., "+12")
        change_label: Change context (e.g., "vs last week")
        is_positive: True for green (positive), False for red (negative)
    """
    color = COLORS['green_primary'] if is_positive else COLORS['red_primary']
    arrow = "↑" if is_positive else "↓"
    
    st.markdown(f"""
    <div style="
        background: {COLORS['bg_card']};
        border: 1px solid {COLORS['border_default']};
        border-radius: 12px;
        padding: 20px;
        height: 140px;
    ">
        <p style="
            color: {COLORS['text_secondary']};
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
            font-weight: 500;
        ">
            {label}
        </p>
        <h1 style="
            color: {COLORS['text_primary']};
            font-size: 40px;
            font-weight: 700;
            line-height: 1;
            margin: 8px 0 12px 0;
        ">
            {value}
        </h1>
        <div style="display: flex; align-items: center; gap: 6px;">
            <span style="
                color: {color};
                font-size: 16px;
                font-weight: 600;
            ">
                {arrow} {change_value}
            </span>
            <span style="
                color: {COLORS['text_muted']};
                font-size: 12px;
            ">
                {change_label}
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def probability_bar(label, yes_prob):
    """
    Green/Red probability bar - Polymarket style
    Args:
        label: Description of what's being measured
        yes_prob: Percentage for favorable outcome (0-100)
    """
    no_prob = 100 - yes_prob
    
    st.markdown(f"""
    <div style="
        background: {COLORS['bg_card']};
        border: 1px solid {COLORS['border_default']};
        border-radius: 8px;
        padding: 16px;
        margin: 8px 0;
    ">
        <p style="
            color: {COLORS['text_primary']};
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 12px;
        ">
            {label}
        </p>
        <div style="
            display: flex;
            height: 40px;
            border-radius: 6px;
            overflow: hidden;
        ">
            <div style="
                background: {COLORS['green_primary']};
                width: {yes_prob}%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 16px;
                font-weight: 700;
                transition: width 0.3s ease;
            ">
                {yes_prob}%
            </div>
            <div style="
                background: {COLORS['red_primary']};
                width: {no_prob}%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-size: 16px;
                font-weight: 700;
                transition: width 0.3s ease;
            ">
                {no_prob}%
            </div>
        </div>
        <div style="
            display: flex;
            justify-content: space-between;
            margin-top: 8px;
        ">
            <span style="color: {COLORS['green_primary']}; font-size: 11px; text-transform: uppercase;">Favorable</span>
            <span style="color: {COLORS['red_primary']}; font-size: 11px; text-transform: uppercase;">Unfavorable</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def gender_comparison_chart(categories, women_values, men_values, title):
    """
    Side-by-side gender comparison bar chart
    Args:
        categories: List of category labels
        women_values: List of values for women
        men_values: List of values for men
        title: Chart title
    """
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Women',
        x=categories,
        y=women_values,
        marker_color=COLORS['women_blue'],
        hovertemplate='<b>Women</b><br>%{x}: %{y}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Men',
        x=categories,
        y=men_values,
        marker_color=COLORS['men_red'],
        hovertemplate='<b>Men</b><br>%{x}: %{y}%<extra></extra>'
    ))
    
    layout = get_plotly_layout()
    layout.update({
        'title': {
            'text': title,
            'font': {'size': 18, 'color': COLORS['text_primary'], 'family': 'Inter'},
            'x': 0.05
        },
        'barmode': 'group',
        'bargap': 0.15,
        'bargroupgap': 0.1,
        'showlegend': True,
        'legend': {
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': 1.02,
            'xanchor': 'right',
            'x': 1,
            'bgcolor': COLORS['bg_card'],
            'bordercolor': COLORS['border_default'],
            'borderwidth': 1
        },
        'height': 400
    })
    
    fig.update_layout(**layout)
    return fig


def trend_line_chart(data_x, data_y, title, color=None):
    """
    Smooth line chart for trend analysis
    Args:
        data_x: X-axis values
        data_y: Y-axis values
        title: Chart title
        color: Line color (defaults to green)
    """
    if color is None:
        color = COLORS['green_primary']
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data_x,
        y=data_y,
        mode='lines+markers',
        line=dict(color=color, width=3),
        marker=dict(size=8, color=color),
        fill='tozeroy',
        fillcolor=f"rgba(0, 230, 118, 0.1)",
        hovertemplate='<b>%{x}</b><br>Value: %{y}<extra></extra>'
    ))
    
    layout = get_plotly_layout()
    layout.update({
        'title': {
            'text': title,
            'font': {'size': 18, 'color': COLORS['text_primary']},
            'x': 0.05
        },
        'showlegend': False,
        'height': 350
    })
    
    fig.update_layout(**layout)
    return fig


def sentiment_indicator(sentiment_score):
    """
    Display sentiment with colored indicator
    Args:
        sentiment_score: Float between -1 and 1
    Returns:
        HTML for sentiment display
    """
    if sentiment_score > 0.3:
        color = COLORS['green_primary']
        label = "Positive"
        emoji = "😊"
    elif sentiment_score < -0.3:
        color = COLORS['red_primary']
        label = "Negative"
        emoji = "😟"
    else:
        color = COLORS['neutral']
        label = "Neutral"
        emoji = "😐"
    
    return f"""
    <span style="
        background: {color}20;
        color: {color};
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
    ">
        {emoji} {label} ({sentiment_score:+.2f})
    </span>
    """


def info_card(title, content, icon="ℹ️"):
    """
    Information card with icon
    Args:
        title: Card title
        content: Card content text
        icon: Emoji icon
    """
    st.markdown(f"""
    <div style="
        background: {COLORS['bg_card']};
        border: 1px solid {COLORS['border_default']};
        border-radius: 8px;
        padding: 16px;
        margin: 8px 0;
    ">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <span style="font-size: 24px;">{icon}</span>
            <h3 style="
                color: {COLORS['text_primary']};
                font-size: 16px;
                font-weight: 600;
                margin: 0;
            ">
                {title}
            </h3>
        </div>
        <p style="
            color: {COLORS['text_secondary']};
            font-size: 14px;
            line-height: 1.6;
            margin: 0;
        ">
            {content}
        </p>
    </div>
    """, unsafe_allow_html=True)
