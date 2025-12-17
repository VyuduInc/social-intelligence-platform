# Social Intelligence Platform - Phase 1
**Budget:** ~250 credits  
**Timeline:** 1-2 weeks  
**Deliverable:** Gated Polymarket-style dashboard with 3 curated tabs

---

## Spec Provenance

**Original Brief:** `/Users/jeremywilliams/Downloads/dev_brief.md`  
**Client:** Jeremy Williams / Vyudu Inc  
**Inspiration:** Polymarket (dark theme, market-style metrics)  
**Plan Created:** 2024-12-17

---

## Spec Header

### Name
Social Intelligence Platform - Phase 1 MVP

### Smallest Scope
A password-gated Streamlit dashboard with Polymarket-inspired design featuring 3 tabs:
1. **Social Trends Monitor** - Mock trending topics with sentiment indicators
2. **Attraction Science Hub** - Research-backed insights from dev brief
3. **Social Skills Lab** - Actionable communication guides

All data is curated/static (no live APIs). Focus on beautiful, demo-ready UI.

### Non-Goals (Phase 1)
- ❌ No Reddit/News/YouTube API integrations
- ❌ No SQLite database (use JSON/CSV files)
- ❌ No ML prediction models
- ❌ No NLP processing pipeline
- ❌ Skip Tabs 4-6 (Predictions, Gender Dynamics, Personalization)
- ❌ No user accounts (single shared access code)
- ❌ No real-time data updates

---

## Paths to Supplementary Guidelines

### Design References
- **Polymarket Inspiration:** https://polymarket.com (dark theme, clean metrics, green/red indicators)
- **Streamlit Docs:** https://docs.streamlit.io/library/api-reference
- **Plotly Dark Theme:** https://plotly.com/python/templates/

### Data Sources (For Curation)
- Original dev brief contains all research data
- Manually curate 20-30 trending topics
- Use research-backed statistics from brief

---

## Decision Snapshot

### Tech Stack
**Framework:** Streamlit 1.28+ (Python web framework)  
**Visualization:** Plotly (interactive dark-themed charts)  
**Data Storage:** JSON files + CSV (no database)  
**Styling:** Custom CSS + Streamlit theming  
**Deployment:** Streamlit Cloud (free tier)  
**Version Control:** Git/GitHub

**Why this stack:**
- Streamlit = fastest Python dashboard framework
- JSON/CSV = simplest data storage, no DB overhead
- Plotly = beautiful dark-themed charts out of the box
- Free hosting = no infrastructure costs

### Design Approach
**Polymarket Dark Theme:**
- Background: `#0a0e27` (deep navy)
- Cards: `#1a1f35` (elevated dark)
- Green: `#00e676` (positive metrics)
- Red: `#ff1744` (negative metrics)
- Gender colors: Blue `#1f77b4` (women), Red `#d62728` (men)

**Component Style:**
- Rounded cards (8-12px radius)
- Large metric displays (48px numbers)
- Clean bar charts and gauges
- Minimal text, maximum data density

### Data Strategy
**Tab 1 - Social Trends (Mock):**
- Curate 20 realistic trending topics
- Add mock sentiment scores
- Create gender comparison data
- Store in `data/mock_trends.json`

**Tab 2 - Attraction Science (Static):**
- Extract research from dev brief
- Create structured JSON with studies
- Include citations and key findings
- Store in `data/attraction_research.json`

**Tab 3 - Social Skills (Curated):**
- Write actionable communication tips
- Create scenario-based examples
- Include do's and don'ts
- Store in `data/social_skills.json`

### Authentication
**Simple Password Gate:**
- Single shared access code
- Session-based (no persistence)
- Store code in `.streamlit/secrets.toml`
- Block all content until authenticated
- Clear error messages

---

## Architecture at a Glance

### Project Structure (Minimal)
```
polymarket_dashboard/
├── .gitignore
├── README.md
├── requirements.txt
├── start.sh
│
├── .streamlit/
│   ├── config.toml              # Theme colors
│   └── secrets.toml             # Access code (not in git)
│
├── src/
│   ├── app.py                   # MAIN ENTRY POINT
│   ├── auth.py                  # Access gate logic
│   ├── design_system.py         # Colors, styles constants
│   ├── components.py            # Reusable UI components
│   │
│   └── tabs/
│       ├── tab1_trends.py       # Social Trends
│       ├── tab2_attraction.py   # Attraction Science
│       └── tab3_skills.py       # Social Skills
│
├── data/
│   ├── mock_trends.json         # Curated trending topics
│   ├── attraction_research.json # Research data
│   └── social_skills.json       # Skills content
│
└── assets/
    └── custom.css               # Streamlit overrides
```

### Data Flow (Simplified)
```
1. User visits app URL
2. auth.py checks session state
3. If not authenticated → show access gate
4. If authenticated → load main app
5. User selects tab → load JSON data
6. components.py renders Plotly charts
7. User interacts with visualizations
```

### Component Reusability
**Build Once, Use Everywhere:**
- `metric_card()` - Large metric display
- `mini_metric()` - Small stat card
- `probability_bar()` - Green/red split bar
- `gender_comparison_chart()` - Blue/red bar chart
- `trend_line_chart()` - Time series line
- `styled_table()` - Data table with dark theme

---

## Implementation Plan

### Phase 1.1: Foundation (Days 1-2)
**Goal:** Project setup, access gate, design system

**Files to Create:**
1. **Project setup**
   - Initialize git repo
   - Create folder structure
   - Create `.gitignore` (exclude .venv, secrets, __pycache__)
   - Create `requirements.txt`:
     ```
     streamlit==1.28.0
     plotly==5.17.0
     pandas==2.0.0
     numpy==1.24.0
     ```

2. **`src/auth.py`** - Access gate
   ```python
   import streamlit as st
   
   def check_access():
       """Simple session-based password gate"""
       if 'authenticated' not in st.session_state:
           st.session_state.authenticated = False
       
       if not st.session_state.authenticated:
           # Show login UI
           st.markdown("<div style='text-align: center'>", unsafe_allow_html=True)
           st.title("🔐 Social Intelligence Platform")
           password = st.text_input("Enter Access Code", type="password")
           
           if st.button("Access Dashboard"):
               if password == st.secrets["ACCESS_CODE"]:
                   st.session_state.authenticated = True
                   st.rerun()
               else:
                   st.error("Invalid access code")
           st.stop()
   ```

3. **`src/design_system.py`** - Colors and styles
   ```python
   # Polymarket-inspired colors
   COLORS = {
       'bg_primary': '#0a0e27',
       'bg_card': '#1a1f35',
       'green': '#00e676',
       'red': '#ff1744',
       'women_blue': '#1f77b4',
       'men_red': '#d62728',
       'text_primary': '#ffffff',
       'text_secondary': '#8b92b0',
       'border': '#262b44',
   }
   
   # Plotly layout template
   def get_chart_layout():
       return {
           'paper_bgcolor': COLORS['bg_primary'],
           'plot_bgcolor': COLORS['bg_card'],
           'font': {'color': COLORS['text_primary']},
           # ... etc
       }
   ```

4. **`.streamlit/config.toml`** - Theme config
   ```toml
   [theme]
   primaryColor = "#00e676"
   backgroundColor = "#0a0e27"
   secondaryBackgroundColor = "#1a1f35"
   textColor = "#ffffff"
   font = "sans serif"
   ```

5. **`.streamlit/secrets.toml`** (not in git)
   ```toml
   ACCESS_CODE = "demo2024"
   ```

6. **`src/app.py`** - Basic structure
   ```python
   import streamlit as st
   from auth import check_access
   
   # Configure page
   st.set_page_config(
       page_title="Social Intelligence Platform",
       page_icon="📊",
       layout="wide",
       initial_sidebar_state="collapsed"
   )
   
   # Check access
   check_access()
   
   # Main app
   st.title("Social Intelligence Platform")
   # Tabs will be added next
   ```

**Testing:** Run locally, verify access gate works

---

### Phase 1.2: Components Library (Days 3-4)
**Goal:** Build reusable UI components with Polymarket styling

**Files to Create:**
1. **`src/components.py`** - All reusable components

**Key Components:**

```python
import streamlit as st
import plotly.graph_objects as go
from design_system import COLORS

def metric_card(label, value, change_value, change_label, is_positive=True):
    """Large Polymarket-style metric card"""
    color = COLORS['green'] if is_positive else COLORS['red']
    arrow = "↑" if is_positive else "↓"
    
    st.markdown(f"""
    <div style="
        background: {COLORS['bg_card']};
        border: 1px solid {COLORS['border']};
        border-radius: 12px;
        padding: 24px;
    ">
        <p style="color: {COLORS['text_secondary']}; font-size: 12px; text-transform: uppercase;">
            {label}
        </p>
        <h1 style="color: {COLORS['text_primary']}; font-size: 48px; margin: 10px 0;">
            {value}
        </h1>
        <p style="color: {color}; font-size: 16px;">
            {arrow} {change_value} <span style="color: {COLORS['text_secondary']};">{change_label}</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

def probability_bar(label, yes_prob):
    """Green/Red probability bar"""
    no_prob = 100 - yes_prob
    
    st.markdown(f"""
    <div style="background: {COLORS['bg_card']}; border-radius: 8px; padding: 16px;">
        <p style="color: {COLORS['text_primary']}; margin-bottom: 12px;">{label}</p>
        <div style="display: flex; height: 40px; border-radius: 6px; overflow: hidden;">
            <div style="background: {COLORS['green']}; width: {yes_prob}%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">
                {yes_prob}%
            </div>
            <div style="background: {COLORS['red']}; width: {no_prob}%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">
                {no_prob}%
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def gender_comparison_chart(categories, women_values, men_values, title):
    """Blue/Red gender comparison bar chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Women',
        x=categories,
        y=women_values,
        marker_color=COLORS['women_blue']
    ))
    
    fig.add_trace(go.Bar(
        name='Men',
        x=categories,
        y=men_values,
        marker_color=COLORS['men_red']
    ))
    
    fig.update_layout(
        title=title,
        barmode='group',
        paper_bgcolor=COLORS['bg_primary'],
        plot_bgcolor=COLORS['bg_card'],
        font={'color': COLORS['text_primary']},
        xaxis={'gridcolor': COLORS['border']},
        yaxis={'gridcolor': COLORS['border']}
    )
    
    return fig

def trend_line_chart(data_x, data_y, title, color=None):
    """Line chart for trends"""
    if color is None:
        color = COLORS['green']
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data_x,
        y=data_y,
        mode='lines+markers',
        line=dict(color=color, width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title=title,
        paper_bgcolor=COLORS['bg_primary'],
        plot_bgcolor=COLORS['bg_card'],
        font={'color': COLORS['text_primary']},
        xaxis={'gridcolor': COLORS['border']},
        yaxis={'gridcolor': COLORS['border']},
        showlegend=False
    )
    
    return fig
```

**Testing:** Create test page to preview all components

---

### Phase 1.3: Data Curation (Days 4-5)
**Goal:** Create curated JSON data files for all 3 tabs

**Files to Create:**

1. **`data/mock_trends.json`** - 20 trending topics
   ```json
   {
     "trends": [
       {
         "topic": "First Date Conversation Tips",
         "volume": 1250,
         "sentiment": 0.72,
         "velocity": 15.3,
         "women_interest": 68,
         "men_interest": 45,
         "peak_time": "Evening"
       },
       {
         "topic": "Height Preferences Dating",
         "volume": 980,
         "sentiment": -0.12,
         "velocity": -8.5,
         "women_interest": 34,
         "men_interest": 78,
         "peak_time": "Night"
       },
       // ... 18 more realistic topics
     ],
     "top_keywords": {
       "women": ["communication", "emotional intelligence", "stability"],
       "men": ["attraction", "fitness", "confidence"]
     }
   }
   ```

2. **`data/attraction_research.json`** - Research insights
   ```json
   {
     "physical_factors": [
       {
         "factor": "Height Preference",
         "women_preference": "Taller than self (68%)",
         "men_preference": "Shorter than self (82%)",
         "research": "Stulp et al., 2013",
         "key_finding": "Height preferences are stronger in men than women",
         "practical_tip": "Focus on posture and confidence over actual height"
       },
       // ... more factors
     ],
     "behavioral_factors": [
       {
         "trait": "Confidence",
         "attractiveness_score": 8.7,
         "gender_difference": "Universal appeal",
         "how_to_demonstrate": "Eye contact, clear speech, decisive actions"
       },
       // ... more traits
     ]
   }
   ```

3. **`data/social_skills.json`** - Skills content
   ```json
   {
     "communication_tips": [
       {
         "category": "Opening Lines",
         "do": "Ask open-ended questions about their interests",
         "dont": "Use generic pickup lines or compliments",
         "example_good": "I noticed you're reading [book]. What made you pick that?",
         "example_bad": "You have beautiful eyes.",
         "effectiveness": 7.8
       },
       // ... more tips
     ],
     "body_language": [
       {
         "signal": "Prolonged Eye Contact",
         "meaning": "Interest and engagement",
         "how_to_use": "Maintain 60-70% eye contact during conversation",
         "common_mistake": "Staring too intensely (creepy) or avoiding eyes (disinterest)"
       },
       // ... more signals
     ]
   }
   ```

**Task:** Manually curate all data from original dev brief

---

### Phase 1.4: Tab 1 - Social Trends (Days 5-6)
**Goal:** Build trending topics display with mock data

**Files to Create:**
1. **`src/tabs/tab1_trends.py`**

```python
import streamlit as st
import json
import pandas as pd
from components import metric_card, gender_comparison_chart, trend_line_chart
from design_system import COLORS

def render():
    st.header("🔥 Social Trends Monitor")
    st.caption("Curated trending topics in dating & relationships")
    
    # Load mock data
    with open('data/mock_trends.json', 'r') as f:
        data = json.load(f)
    
    # Top metrics row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        metric_card("Active Topics", "87", "+12", "vs last week", True)
    with col2:
        metric_card("Avg Sentiment", "+0.65", "+0.08", "more positive", True)
    with col3:
        metric_card("Peak Activity", "9-11pm", "2hrs", "window", True)
    with col4:
        metric_card("Engagement", "2.4K", "+18%", "comments", True)
    
    st.markdown("---")
    
    # Trending topics table
    st.subheader("🔥 Top Trending Topics")
    df = pd.DataFrame(data['trends'][:10])
    
    # Color sentiment column
    def color_sentiment(val):
        color = COLORS['green'] if val > 0 else COLORS['red']
        return f'<span style="color: {color}">{"+" if val > 0 else ""}{val:.2f}</span>'
    
    df['sentiment_colored'] = df['sentiment'].apply(color_sentiment)
    
    st.dataframe(
        df[['topic', 'volume', 'sentiment_colored', 'velocity']],
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("---")
    
    # Gender comparison
    st.subheader("⚖️ Gender Interest Comparison")
    
    topics = [t['topic'][:30] for t in data['trends'][:8]]
    women = [t['women_interest'] for t in data['trends'][:8]]
    men = [t['men_interest'] for t in data['trends'][:8]]
    
    fig = gender_comparison_chart(topics, women, men, "Interest by Gender (%)")
    st.plotly_chart(fig, use_container_width=True)
    
    # Keywords by gender
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 👩 Women's Top Keywords")
        for kw in data['top_keywords']['women']:
            st.markdown(f"- {kw}")
    
    with col2:
        st.markdown("### 👨 Men's Top Keywords")
        for kw in data['top_keywords']['men']:
            st.markdown(f"- {kw}")
```

**Testing:** Verify charts render, data displays correctly

---

### Phase 1.5: Tab 2 - Attraction Science (Days 6-7)
**Goal:** Display research-backed insights

**Files to Create:**
1. **`src/tabs/tab2_attraction.py`**

```python
import streamlit as st
import json
import plotly.graph_objects as go
from design_system import COLORS

def render():
    st.header("💡 Attraction Science Hub")
    st.caption("Research-backed insights on what drives attraction")
    
    # Load research data
    with open('data/attraction_research.json', 'r') as f:
        data = json.load(f)
    
    # Physical factors section
    st.subheader("📏 Physical Attraction Factors")
    
    for factor in data['physical_factors'][:5]:
        with st.expander(f"**{factor['factor']}**"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Women prefer:** {factor['women_preference']}")
            with col2:
                st.markdown(f"**Men prefer:** {factor['men_preference']}")
            
            st.markdown(f"**Research:** {factor['research']}")
            st.info(f"💡 {factor['practical_tip']}")
    
    st.markdown("---")
    
    # Behavioral factors section
    st.subheader("🎭 Behavioral Attraction Signals")
    
    # Radar chart of traits
    traits = [b['trait'] for b in data['behavioral_factors']]
    scores = [b['attractiveness_score'] for b in data['behavioral_factors']]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=traits,
        fill='toself',
        fillcolor=f"rgba(0, 230, 118, 0.2)",
        line=dict(color=COLORS['green'], width=2)
    ))
    
    fig.update_layout(
        polar=dict(
            bgcolor=COLORS['bg_card'],
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                gridcolor=COLORS['border']
            ),
            angularaxis=dict(
                gridcolor=COLORS['border']
            )
        ),
        paper_bgcolor=COLORS['bg_primary'],
        font={'color': COLORS['text_primary']},
        title="Attractiveness Ratings by Trait"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # How to demonstrate each trait
    st.subheader("✅ How to Demonstrate These Traits")
    
    for trait_data in data['behavioral_factors']:
        st.markdown(f"**{trait_data['trait']}:** {trait_data['how_to_demonstrate']}")
```

**Testing:** Verify research displays properly, charts work

---

### Phase 1.6: Tab 3 - Social Skills (Days 7-8)
**Goal:** Display actionable communication guides

**Files to Create:**
1. **`src/tabs/tab3_skills.py`**

```python
import streamlit as st
import json
from components import probability_bar
from design_system import COLORS

def render():
    st.header("🎭 Social Skills Lab")
    st.caption("Actionable guidance for better communication")
    
    # Load skills data
    with open('data/social_skills.json', 'r') as f:
        data = json.load(f)
    
    # Communication tips section
    st.subheader("💬 Communication Effectiveness")
    
    for tip in data['communication_tips']:
        with st.expander(f"**{tip['category']}** (Effectiveness: {tip['effectiveness']}/10)"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### ✅ DO")
                st.success(tip['do'])
                st.code(tip['example_good'], language=None)
            
            with col2:
                st.markdown("### ❌ DON'T")
                st.error(tip['dont'])
                st.code(tip['example_bad'], language=None)
            
            # Effectiveness bar
            probability_bar(
                "Effectiveness Rating",
                int(tip['effectiveness'] * 10)
            )
    
    st.markdown("---")
    
    # Body language section
    st.subheader("👁️ Body Language Decoder")
    
    for signal in data['body_language']:
        with st.container():
            st.markdown(f"### {signal['signal']}")
            st.write(f"**Meaning:** {signal['meaning']}")
            st.write(f"**How to use:** {signal['how_to_use']}")
            st.warning(f"⚠️ Common mistake: {signal['common_mistake']}")
            st.markdown("---")
```

**Testing:** Verify all content displays correctly

---

### Phase 1.7: Integration & Polish (Days 9-10)
**Goal:** Connect all tabs, add navigation, polish UI

**Update `src/app.py`:**
```python
import streamlit as st
from auth import check_access
from tabs import tab1_trends, tab2_attraction, tab3_skills

# Configure page
st.set_page_config(
    page_title="Social Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
with open('assets/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Check access
check_access()

# Header
st.title("📊 Social Intelligence Platform")
st.caption("Data-driven insights on dating, attraction, and social dynamics")

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
st.caption("Powered by research-backed insights • Vyudu Inc")
```

**Create `assets/custom.css`:**
```css
/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Dark theme enhancements */
[data-testid="stAppViewContainer"] {
    background-color: #0a0e27;
}

/* Expander styling */
[data-testid="stExpander"] {
    background-color: #1a1f35;
    border: 1px solid #262b44;
    border-radius: 8px;
}

/* Tab styling */
[data-testid="stTab"] {
    background-color: #1a1f35;
    border-radius: 8px 8px 0 0;
}
```

**Testing:**
- [ ] All 3 tabs load without errors
- [ ] Navigation between tabs works
- [ ] Access gate blocks unauthenticated users
- [ ] Charts render correctly
- [ ] Mobile responsive (test on phone)
- [ ] No console errors

---

### Phase 1.8: Deployment (Day 10)
**Goal:** Deploy to Streamlit Cloud

**Steps:**
1. Create `README.md`:
   ```markdown
   # Social Intelligence Platform - Phase 1
   
   Gated dashboard with curated insights on dating & social dynamics.
   
   ## Setup
   1. Clone repo
   2. Install: `pip install -r requirements.txt`
   3. Create `.streamlit/secrets.toml` with `ACCESS_CODE = "your_code"`
   4. Run: `streamlit run src/app.py`
   
   ## Access Code
   Contact admin for access code.
   ```

2. Create `.gitignore`:
   ```
   .venv/
   __pycache__/
   .streamlit/secrets.toml
   .DS_Store
   *.pyc
   ```

3. Push to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Phase 1: Gated dashboard with 3 curated tabs"
   git remote add origin [your-repo-url]
   git push -u origin main
   ```

4. Deploy on Streamlit Cloud:
   - Go to share.streamlit.io
   - Connect GitHub repo
   - Add secret: `ACCESS_CODE = "your_code"`
   - Click "Deploy"
   - Test live URL

**Launch Checklist:**
- [ ] App loads in under 2 seconds
- [ ] Access gate works
- [ ] All tabs functional
- [ ] No errors in logs
- [ ] Mobile responsive
- [ ] Share URL with stakeholders

---

## Verification & Demo Script

### Demo Flow (5 minutes)
1. **Access Gate** (30 sec)
   - Show password entry
   - Enter code, gain access
   - Explain session persistence

2. **Tab 1 - Social Trends** (90 sec)
   - Show top metrics
   - Explain trending topics table
   - Highlight gender comparison chart
   - Point out sentiment indicators (green/red)

3. **Tab 2 - Attraction Science** (90 sec)
   - Review physical factors expanders
   - Show radar chart of behavioral traits
   - Highlight research citations
   - Emphasize practical tips

4. **Tab 3 - Social Skills** (90 sec)
   - Demonstrate do/don't examples
   - Show effectiveness ratings
   - Review body language signals
   - Explain actionable nature

5. **Design Showcase** (30 sec)
   - Point out Polymarket-inspired dark theme
   - Highlight consistent color usage (green/red, blue/red)
   - Show responsive design on mobile

### Key Messages
- "All data is curated from research, not opinion"
- "Polymarket-style design = professional, data-focused"
- "3 tabs cover broadest appeal: trends, science, skills"
- "Ready to add live data in Phase 2"

### Questions to Ask Stakeholders
- Which tab is most valuable?
- Is access gate sufficient or need user accounts?
- Should Phase 2 add Reddit API for real trends?
- Any content gaps in current tabs?

---

## Deploy

### Requirements
- Python 3.11+
- Streamlit Cloud account (free)
- GitHub account
- Access code (shared with users)

### Local Development
```bash
# Clone and setup
cd /Users/jeremywilliams/Workspace/polymarket_dashboard
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Create secrets file
echo 'ACCESS_CODE = "demo2024"' > .streamlit/secrets.toml

# Run locally
streamlit run src/app.py
```

### Production Deployment
```bash
# Push to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# Deploy via Streamlit Cloud UI:
# 1. Go to share.streamlit.io
# 2. Connect GitHub repo
# 3. Add secrets in UI
# 4. Click Deploy
```

### Post-Deployment
- Test on multiple devices
- Share access code with stakeholders
- Monitor Streamlit Cloud logs
- Collect feedback for Phase 2

---

## Future Phases

### Phase 2 (~250 credits)
**Add Real Data:**
- Reddit API integration for Tab 1
- Real-time trending topics
- Live sentiment analysis
- Database storage (SQLite)

### Phase 3 (~250 credits)
**Add 3 More Tabs:**
- Tab 4: Predictions & Probabilities
- Tab 5: Gender Dynamics Analyzer
- Tab 6: Personalization Engine

### Phase 4 (~250 credits)
**Advanced Features:**
- ML prediction models
- User accounts system
- Export reports
- Email alerts

---

## Budget Breakdown

**Estimated Credit Usage:**
- Project setup & access gate: ~30 credits
- Design system & components: ~40 credits
- Data curation: ~20 credits
- Tab 1 implementation: ~40 credits
- Tab 2 implementation: ~40 credits
- Tab 3 implementation: ~40 credits
- Integration & polish: ~30 credits
- Deployment & testing: ~20 credits

**Total: ~260 credits** (slight buffer needed, but optimized for efficiency)

**Credit-Saving Strategies:**
- No API integrations (saves debugging time)
- No database setup (JSON files only)
- Reusable components (write once, use 3x)
- Simple authentication (no user management)
- Curated data (no NLP processing)

---

## Success Metrics

### Phase 1 Complete When:
- [ ] All 3 tabs functional
- [ ] Access gate working
- [ ] Polymarket design applied
- [ ] Deployed to Streamlit Cloud
- [ ] Under 300 credits used
- [ ] Demo-ready for stakeholders

### User Feedback Goals:
- Visual design rating: 8+/10
- Content value rating: 7+/10
- Ease of use: 9+/10
- "Would use again": 80%+

---

**This plan delivers maximum value in Phase 1 while staying credit-efficient. Focus on beautiful UI and curated content, prove value, then decide on Phase 2.**