"""
Design System - Polymarket-inspired colors and styling
"""

# Polymarket-inspired color palette
COLORS = {
    # Backgrounds
    'bg_primary': '#0a0e27',        # Main app background
    'bg_secondary': '#0f1420',      # Secondary sections
    'bg_card': '#1a1f35',           # Elevated cards
    'bg_card_hover': '#1e2438',     # Card hover state
    'bg_input': '#141829',          # Input fields
    
    # Market Colors (Polymarket style)
    'green_primary': '#00e676',     # Positive, "Yes", Gains
    'green_secondary': '#00c853',   # Hover, secondary green
    'green_muted': '#1b5e20',       # Background tints
    'red_primary': '#ff1744',       # Negative, "No", Losses
    'red_secondary': '#d50000',     # Hover, secondary red
    'red_muted': '#8b0000',         # Background tints
    
    # Gender Colors (from original brief)
    'women_blue': '#1f77b4',        # Female data
    'men_red': '#d62728',           # Male data
    'neutral': '#9575cd',           # Non-binary/neutral
    
    # Text Colors
    'text_primary': '#ffffff',      # Primary text (90% opacity)
    'text_secondary': '#8b92b0',    # Secondary text (60% opacity)
    'text_muted': '#5a5f7d',        # Muted text (40% opacity)
    'text_disabled': '#3a3f5d',     # Disabled text (20% opacity)
    
    # Borders & Dividers
    'border_default': '#262b44',    # Default borders
    'border_hover': '#363b64',      # Hover state borders
    'border_focus': '#4a4f84',      # Focus state borders
    'divider': '#1e2438',           # Section dividers
    
    # Semantic Colors
    'success': '#00e676',           # Success messages
    'warning': '#ffc107',           # Warning messages
    'error': '#ff1744',             # Error messages
    'info': '#2196f3',              # Info messages
}

def get_plotly_layout():
    """
    Standard Plotly layout for consistent theming across all charts
    """
    return {
        'paper_bgcolor': COLORS['bg_primary'],
        'plot_bgcolor': COLORS['bg_card'],
        'font': {
            'family': 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
            'color': COLORS['text_primary'],
            'size': 12
        },
        'xaxis': {
            'gridcolor': COLORS['border_default'],
            'linecolor': COLORS['border_default'],
            'tickfont': {'color': COLORS['text_secondary'], 'size': 11},
            'titlefont': {'color': COLORS['text_primary'], 'size': 13}
        },
        'yaxis': {
            'gridcolor': COLORS['border_default'],
            'linecolor': COLORS['border_default'],
            'tickfont': {'color': COLORS['text_secondary'], 'size': 11},
            'titlefont': {'color': COLORS['text_primary'], 'size': 13}
        },
        'legend': {
            'bgcolor': COLORS['bg_card'],
            'bordercolor': COLORS['border_default'],
            'borderwidth': 1,
            'font': {'color': COLORS['text_primary'], 'size': 11}
        },
        'hovermode': 'x unified',
        'hoverlabel': {
            'bgcolor': COLORS['bg_card'],
            'bordercolor': COLORS['border_default'],
            'font': {'color': COLORS['text_primary'], 'size': 12}
        },
        'margin': dict(l=50, r=30, t=60, b=50)
    }
