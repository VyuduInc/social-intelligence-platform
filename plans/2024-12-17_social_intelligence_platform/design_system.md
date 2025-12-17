# Design System - Polymarket-Inspired Social Intelligence Platform

## Overview
This design system creates a premium, data-focused experience inspired by Polymarket's sophisticated interface while maintaining the social intelligence platform's unique gender-comparative insights.

---

## Color System

### Base Palette
```python
# Dark Theme Foundation
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
```

### Color Usage Guidelines

**Green (Positive Metrics)**
- Upward trends
- Probability > 50%
- Positive sentiment scores
- "Favorable" outcomes
- Increased engagement

**Red (Negative Metrics)**
- Downward trends
- Probability < 50%
- Negative sentiment scores
- "Unfavorable" outcomes
- Decreased engagement

**Blue (Women's Data)**
- All female-specific metrics
- Women's preferences
- Female-dominated topics

**Red (Men's Data)** *(Yes, using red twice)*
- All male-specific metrics
- Men's preferences
- Male-dominated topics

**Purple (Neutral)**
- Combined/aggregate data
- Non-gendered topics
- Universal insights

---

## Typography

### Font Stack
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
             'Helvetica Neue', Arial, sans-serif;
```

### Font Sizes & Weights
```python
TYPOGRAPHY = {
    # Headings
    'h1': {'size': '32px', 'weight': 700, 'line_height': 1.2},
    'h2': {'size': '24px', 'weight': 600, 'line_height': 1.3},
    'h3': {'size': '20px', 'weight': 600, 'line_height': 1.4},
    'h4': {'size': '16px', 'weight': 600, 'line_height': 1.5},
    
    # Body Text
    'body_large': {'size': '16px', 'weight': 400, 'line_height': 1.6},
    'body': {'size': '14px', 'weight': 400, 'line_height': 1.6},
    'body_small': {'size': '12px', 'weight': 400, 'line_height': 1.5},
    
    # Display Numbers
    'display_large': {'size': '48px', 'weight': 700, 'line_height': 1.0},
    'display': {'size': '36px', 'weight': 700, 'line_height': 1.1},
    'display_small': {'size': '28px', 'weight': 600, 'line_height': 1.2},
    
    # Labels & Captions
    'label': {'size': '12px', 'weight': 500, 'line_height': 1.4},
    'caption': {'size': '11px', 'weight': 400, 'line_height': 1.4},
    'overline': {'size': '10px', 'weight': 600, 'line_height': 1.2, 'transform': 'uppercase'},
}
```

---

## Component Library

### 1. Metric Cards (Polymarket Style)

#### Large Metric Card
```python
def large_metric_card(label, value, change_value, change_label, is_positive=True):
    """
    Primary metric display - Polymarket style
    Used for: Key KPIs, probability displays, main statistics
    """
    color = COLORS['green_primary'] if is_positive else COLORS['red_primary']
    arrow = "↑" if is_positive else "↓"
    
    html = f"""
    <div style="
        background: {COLORS['bg_card']};
        border: 1px solid {COLORS['border_default']};
        border-radius: 12px;
        padding: 24px;
        transition: all 0.2s ease;
    ">
        <!-- Label -->
        <div style="
            color: {COLORS['text_secondary']};
            font-size: 12px;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
        ">
            {label}
        </div>
        
        <!-- Main Value -->
        <div style="
            color: {COLORS['text_primary']};
            font-size: 48px;
            font-weight: 700;
            line-height: 1;
            margin-bottom: 12px;
        ">
            {value}
        </div>
        
        <!-- Change Indicator -->
        <div style="
            display: flex;
            align-items: center;
            gap: 6px;
        ">
            <span style="
                color: {color};
                font-size: 20px;
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
    """
    return html
```

#### Mini Metric Card
```python
def mini_metric_card(label, value, icon=None):
    """
    Compact metric display
    Used for: Secondary metrics, comparison data, grid layouts
    """
    html = f"""
    <div style="
        background: {COLORS['bg_card']};
        border: 1px solid {COLORS['border_default']};
        border-radius: 8px;
        padding: 16px;
        text-align: center;
    ">
        {f'<div style="font-size: 24px; margin-bottom: 8px;">{icon}</div>' if icon else ''}
        <div style="
            color: {COLORS['text_secondary']};
            font-size: 11px;
            text-transform: uppercase;
            margin-bottom: 6px;
        ">
            {label}
        </div>
        <div style="
            color: {COLORS['text_primary']};
            font-size: 24px;
            font-weight: 700;
        ">
            {value}
        </div>
    </div>
    """
    return html
```

### 2. Probability Displays (Market Style)

#### Probability Gauge
```python
def probability_gauge(probability, label, confidence_interval=None):
    """
    Circular probability gauge - Polymarket style
    Shows: Probability percentage, confidence band, visual indicator
    """
    import plotly.graph_objects as go
    
    color = COLORS['green_primary'] if probability > 50 else COLORS['red_primary']
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = probability,
        number = {
            'suffix': "%",
            'font': {'size': 48, 'color': COLORS['text_primary']},
        },
        title = {
            'text': label,
            'font': {'size': 14, 'color': COLORS['text_secondary']}
        },
        gauge = {
            'axis': {
                'range': [0, 100],
                'tickwidth': 1,
                'tickcolor': COLORS['border_default'],
                'tickfont': {'color': COLORS['text_muted'], 'size': 10}
            },
            'bar': {'color': color, 'thickness': 0.7},
            'bgcolor': COLORS['bg_secondary'],
            'borderwidth': 2,
            'bordercolor': COLORS['border_default'],
            'steps': [
                {'range': [0, 50], 'color': COLORS['red_muted']},
                {'range': [50, 100], 'color': COLORS['green_muted']}
            ],
        }
    ))
    
    fig.update_layout(
        paper_bgcolor=COLORS['bg_primary'],
        plot_bgcolor=COLORS['bg_primary'],
        font={'color': COLORS['text_primary'], 'family': 'Inter'},
        height=250,
        margin=dict(l=20, r=20, t=60, b=20)
    )
    
    return fig
```

#### Probability Bar
```python
def probability_bar(label, yes_prob, no_prob=None):
    """
    Horizontal probability bar - Polymarket style
    Shows: Yes/No probabilities as opposing bars
    """
    if no_prob is None:
        no_prob = 100 - yes_prob
    
    html = f"""
    <div style="
        background: {COLORS['bg_card']};
        border: 1px solid {COLORS['border_default']};
        border-radius: 8px;
        padding: 16px;
    ">
        <!-- Label -->
        <div style="
            color: {COLORS['text_primary']};
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 12px;
        ">
            {label}
        </div>
        
        <!-- Probability Bar -->
        <div style="
            display: flex;
            height: 40px;
            border-radius: 6px;
            overflow: hidden;
            position: relative;
        ">
            <!-- Yes/Green Section -->
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
            
            <!-- No/Red Section -->
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
        
        <!-- Labels -->
        <div style="
            display: flex;
            justify-content: space-between;
            margin-top: 8px;
        ">
            <span style="color: {COLORS['green_primary']}; font-size: 12px;">Favorable</span>
            <span style="color: {COLORS['red_primary']}; font-size: 12px;">Unfavorable</span>
        </div>
    </div>
    """
    return html
```

### 3. Charts (Plotly Configurations)

#### Base Chart Configuration
```python
def get_base_chart_layout():
    """
    Standard Plotly layout for all charts
    Ensures consistent Polymarket styling
    """
    return {
        'paper_bgcolor': COLORS['bg_primary'],
        'plot_bgcolor': COLORS['bg_card'],
        'font': {
            'family': 'Inter, sans-serif',
            'color': COLORS['text_primary'],
            'size': 12
        },
        'xaxis': {
            'gridcolor': COLORS['border_default'],
            'linecolor': COLORS['border_default'],
            'tickfont': {'color': COLORS['text_secondary']},
            'titlefont': {'color': COLORS['text_primary'], 'size': 14}
        },
        'yaxis': {
            'gridcolor': COLORS['border_default'],
            'linecolor': COLORS['border_default'],
            'tickfont': {'color': COLORS['text_secondary']},
            'titlefont': {'color': COLORS['text_primary'], 'size': 14}
        },
        'legend': {
            'bgcolor': COLORS['bg_card'],
            'bordercolor': COLORS['border_default'],
            'borderwidth': 1,
            'font': {'color': COLORS['text_primary']}
        },
        'hovermode': 'x unified',
        'hoverlabel': {
            'bgcolor': COLORS['bg_card'],
            'bordercolor': COLORS['border_default'],
            'font': {'color': COLORS['text_primary']}
        }
    }
```

#### Line Chart (Trend Analysis)
```python
def trend_line_chart(data, x_col, y_col, title, color=None):
    """
    Sleek line chart for trend analysis
    Used for: Time series, topic velocity, engagement over time
    """
    import plotly.graph_objects as go
    
    if color is None:
        color = COLORS['green_primary']
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data[x_col],
        y=data[y_col],
        mode='lines+markers',
        line=dict(color=color, width=3),
        marker=dict(size=6, color=color),
        fill='tozeroy',
        fillcolor=f"rgba{tuple(list(int(color[i:i+2], 16) for i in (1, 3, 5)) + [0.1])}",
        hovertemplate='<b>%{x}</b><br>%{y}<extra></extra>'
    ))
    
    layout = get_base_chart_layout()
    layout.update({
        'title': {
            'text': title,
            'font': {'size': 18, 'color': COLORS['text_primary']},
            'x': 0.05
        },
        'showlegend': False,
        'margin': dict(l=50, r=30, t=60, b=50)
    })
    
    fig.update_layout(**layout)
    return fig
```

#### Gender Comparison Chart
```python
def gender_comparison_chart(data, categories, women_values, men_values, title):
    """
    Side-by-side comparison bar chart
    Used for: Gender dynamics, preference differences, behavioral patterns
    """
    import plotly.graph_objects as go
    
    fig = go.Figure()
    
    # Women (Blue)
    fig.add_trace(go.Bar(
        name='Women',
        x=categories,
        y=women_values,
        marker_color=COLORS['women_blue'],
        hovertemplate='<b>Women</b><br>%{x}: %{y}<extra></extra>'
    ))
    
    # Men (Red)
    fig.add_trace(go.Bar(
        name='Men',
        x=categories,
        y=men_values,
        marker_color=COLORS['men_red'],
        hovertemplate='<b>Men</b><br>%{x}: %{y}<extra></extra>'
    ))
    
    layout = get_base_chart_layout()
    layout.update({
        'title': {
            'text': title,
            'font': {'size': 18, 'color': COLORS['text_primary']},
            'x': 0.05
        },
        'barmode': 'group',
        'bargap': 0.2,
        'bargroupgap': 0.1,
        'showlegend': True,
        'legend': {'orientation': 'h', 'yanchor': 'bottom', 'y': 1.02, 'xanchor': 'right', 'x': 1}
    })
    
    fig.update_layout(**layout)
    return fig
```

### 4. Tables (Polymarket Style)

#### Data Table
```python
def styled_table(df, title=None):
    """
    Clean, striped data table
    Used for: Rankings, lists, detailed data
    """
    import plotly.graph_objects as go
    
    # Determine cell colors (striped rows)
    row_colors = [COLORS['bg_card'] if i % 2 == 0 else COLORS['bg_secondary'] 
                  for i in range(len(df))]
    
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=[f"<b>{col}</b>" for col in df.columns],
            fill_color=COLORS['bg_secondary'],
            line_color=COLORS['border_default'],
            font=dict(color=COLORS['text_primary'], size=13, family='Inter'),
            align='left',
            height=40
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            fill_color=[row_colors],
            line_color=COLORS['border_default'],
            font=dict(color=COLORS['text_primary'], size=12, family='Inter'),
            align='left',
            height=35
        )
    )])
    
    layout_config = {
        'paper_bgcolor': COLORS['bg_primary'],
        'margin': dict(l=0, r=0, t=40 if title else 0, b=0)
    }
    
    if title:
        layout_config['title'] = {
            'text': title,
            'font': {'size': 16, 'color': COLORS['text_primary']},
            'x': 0.05
        }
    
    fig.update_layout(**layout_config)
    return fig
```

### 5. Buttons & Inputs

#### Primary Button
```css
.primary-button {
    background: linear-gradient(135deg, #00e676 0%, #00c853 100%);
    border: none;
    border-radius: 8px;
    color: white;
    font-size: 14px;
    font-weight: 600;
    padding: 12px 24px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.primary-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 230, 118, 0.3);
}

.primary-button:active {
    transform: translateY(0);
}
```

#### Input Field
```css
.custom-input {
    background: #141829;
    border: 1px solid #262b44;
    border-radius: 8px;
    color: #ffffff;
    font-size: 14px;
    padding: 12px 16px;
    width: 100%;
    transition: all 0.2s ease;
}

.custom-input:focus {
    border-color: #00e676;
    outline: none;
    box-shadow: 0 0 0 3px rgba(0, 230, 118, 0.1);
}

.custom-input::placeholder {
    color: #5a5f7d;
}
```

### 6. Access Gate UI

#### Login Screen
```python
def access_gate_ui():
    """
    Polymarket-style access gate
    Clean, centered, professional
    """
    html = f"""
    <div style="
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
        background: {COLORS['bg_primary']};
    ">
        <!-- Logo/Icon -->
        <div style="
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, {COLORS['green_primary']} 0%, {COLORS['green_secondary']} 100%);
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 24px;
            font-size: 40px;
        ">
            🔐
        </div>
        
        <!-- Title -->
        <h1 style="
            color: {COLORS['text_primary']};
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 8px;
        ">
            Social Intelligence Platform
        </h1>
        
        <!-- Subtitle -->
        <p style="
            color: {COLORS['text_secondary']};
            font-size: 16px;
            margin-bottom: 32px;
            text-align: center;
            max-width: 400px;
        ">
            Data-driven insights on dating, attraction, and social dynamics
        </p>
        
        <!-- Access Code Input (rendered via Streamlit) -->
    </div>
    """
    return html
```

---

## Layout Guidelines

### Grid System
- **Desktop:** 12-column grid, 24px gutters
- **Tablet:** 8-column grid, 16px gutters
- **Mobile:** 4-column grid, 12px gutters

### Spacing Scale
```python
SPACING = {
    'xs': '4px',
    'sm': '8px',
    'md': '16px',
    'lg': '24px',
    'xl': '32px',
    'xxl': '48px',
}
```

### Component Spacing
- Card padding: 24px
- Section spacing: 48px
- Element spacing: 16px
- Grid gap: 24px

### Border Radius
- Small components: 6px
- Cards: 8-12px
- Modals: 16px
- Buttons: 8px

---

## Responsive Breakpoints

```python
BREAKPOINTS = {
    'mobile': '0-767px',
    'tablet': '768-1023px',
    'desktop': '1024-1439px',
    'wide': '1440px+'
}
```

### Responsive Behavior
- **Mobile:** Single column, stacked metrics
- **Tablet:** 2-column grid where appropriate
- **Desktop:** Full 3-4 column grid layouts
- **Wide:** Maximum content width 1600px, centered

---

## Animation & Transitions

### Standard Transitions
```css
/* Smooth transitions for interactive elements */
transition: all 0.2s ease;

/* Hover effects */
transform: translateY(-2px);

/* Loading states */
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}
```

### Loading Skeleton
```python
def skeleton_loader():
    """
    Animated loading placeholder
    """
    html = f"""
    <div style="
        background: linear-gradient(
            90deg,
            {COLORS['bg_card']} 0%,
            {COLORS['bg_card_hover']} 50%,
            {COLORS['bg_card']} 100%
        );
        background-size: 200% 100%;
        animation: shimmer 1.5s infinite;
        border-radius: 8px;
        height: 100px;
    "></div>
    
    <style>
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    </style>
    """
    return html
```

---

## Accessibility

### Color Contrast
- All text meets WCAG AA standards (4.5:1 for body, 3:1 for large text)
- Critical actions use high contrast colors

### Keyboard Navigation
- All interactive elements keyboard accessible
- Clear focus states (border + shadow)
- Logical tab order

### Screen Readers
- Semantic HTML structure
- ARIA labels for charts
- Alt text for icons

---

## Custom CSS for Streamlit

```css
/* Custom Streamlit styling */
[data-testid="stAppViewContainer"] {
    background-color: #0a0e27;
}

[data-testid="stSidebar"] {
    background-color: #0f1420;
    border-right: 1px solid #262b44;
}

[data-testid="stHeader"] {
    background-color: rgba(10, 14, 39, 0.95);
    backdrop-filter: blur(10px);
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Custom metric styling */
[data-testid="stMetric"] {
    background-color: #1a1f35;
    border: 1px solid #262b44;
    border-radius: 12px;
    padding: 20px;
}

/* Custom tabs */
[data-testid="stTabs"] {
    gap: 16px;
}

[data-testid="stTab"] {
    background-color: #1a1f35;
    border-radius: 8px;
    padding: 12px 24px;
}
```

---

## Implementation Checklist

### Setup Phase
- [ ] Create `design_system.py` with all color constants
- [ ] Create `components.py` with reusable component functions
- [ ] Create `custom.css` with Streamlit overrides
- [ ] Setup Plotly defaults for consistent charting

### Component Development
- [ ] Build metric card components
- [ ] Build probability display components
- [ ] Build chart templates
- [ ] Build table components
- [ ] Build access gate UI

### Integration
- [ ] Apply design system across all tabs
- [ ] Test responsive behavior
- [ ] Verify color consistency
- [ ] Check accessibility standards

---

**This design system provides a comprehensive foundation for building a premium, Polymarket-inspired social intelligence platform while maintaining brand identity and usability.**
