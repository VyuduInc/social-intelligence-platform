# Social Intelligence Platform - Gated Dashboard
**Created:** 2024-12-17  
**Project:** Polymarket-inspired Social Intelligence Dashboard with Access Gate  
**Timeline:** 4 weeks to production-ready MVP

---

## EXECUTIVE SUMMARY

Build a gated Streamlit dashboard that provides data-driven insights on dating, attraction, and social dynamics. The platform will feature 6 comprehensive tabs with Polymarket-inspired design (dark theme, market-style metrics, green/red color scheme).

### Key Requirements
- **Access Gate:** Simple password/code entry before dashboard access
- **Design System:** Dark theme, Polymarket-style cards, green/red metrics
- **6 Core Tabs:** Trends, Attraction Science, Gender Dynamics, Predictions, Social Skills, Personalization
- **Data Sources:** Reddit API, News API, YouTube API, research-backed datasets
- **Tech Stack:** Streamlit, Plotly, PRAW, scikit-learn
- **Deployment:** Streamlit Cloud (free tier)

---

## DESIGN SYSTEM (Polymarket-Inspired)

### Color Palette
```python
# Primary Colors
BACKGROUND_PRIMARY = "#0a0e27"      # Deep navy background
BACKGROUND_SECONDARY = "#0f1420"    # Card backgrounds
BACKGROUND_CARD = "#1a1f35"         # Elevated cards

# Accent Colors
GREEN_PRIMARY = "#00e676"           # Positive metrics, gains
GREEN_SECONDARY = "#00c853"         # Hover states
RED_PRIMARY = "#ff1744"             # Negative metrics, losses
RED_SECONDARY = "#d50000"           # Hover states

# Gender Colors (maintained from brief)
WOMEN_COLOR = "#1f77b4"             # Blue
MEN_COLOR = "#d62728"               # Red

# Text Colors
TEXT_PRIMARY = "#ffffff"            # Primary text
TEXT_SECONDARY = "#8b92b0"          # Secondary text
TEXT_MUTED = "#5a5f7d"              # Muted text

# Border & Dividers
BORDER_COLOR = "#262b44"
DIVIDER_COLOR = "#1e2438"
```

### Typography
```python
# Font Stack
FONT_FAMILY = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"

# Font Sizes
FONT_SIZE_H1 = "32px"
FONT_SIZE_H2 = "24px"
FONT_SIZE_H3 = "20px"
FONT_SIZE_BODY = "14px"
FONT_SIZE_SMALL = "12px"
```

### Component Styles
- **Cards:** Rounded corners (8px), subtle shadow, dark background
- **Metrics:** Large numbers, percentage changes with green/red indicators
- **Charts:** Dark background, neon accent colors, clean grid lines
- **Buttons:** Rounded, hover states, primary green accent
- **Tables:** Striped rows, dark theme, sortable columns

---

## AUTHENTICATION & ACCESS GATE

### Phase 1: Simple Password Gate (MVP)
```python
# Implementation approach
def check_access():
    """Simple session-based password gate"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        password = st.text_input("Enter Access Code", type="password")
        if st.button("Access Dashboard"):
            if password == st.secrets["ACCESS_CODE"]:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid access code")
        st.stop()
```

### Access Code Storage
- Store in `.streamlit/secrets.toml` (not in repo)
- Use environment variables for Streamlit Cloud
- Single shared code for MVP (can add user management later)

### Future Enhancements (Post-MVP)
- Individual user accounts
- Email-based access requests
- Time-limited access codes
- Usage analytics per user

---

## PLATFORM ARCHITECTURE

### Tab Structure (6 Tabs)

#### Tab 1: 🔥 Social Trends Monitor
**Purpose:** Real-time pulse on dating & social dynamics

**Components:**
1. **Trending Topics Dashboard**
   - Top 10 trending topics from r/dating, r/relationships
   - Heat map of discussion volume
   - Sentiment indicators (green=positive, red=negative)

2. **Gender Interest Comparison**
   - Side-by-side topic comparison (Women=Blue, Men=Red)
   - Venn diagram of shared vs. unique interests

3. **Conversation Velocity**
   - Real-time activity metrics
   - Peak discussion times by topic
   - Engagement rates

**Data Sources:**
- Reddit API (PRAW): r/dating, r/relationships, r/dating_advice, r/seduction
- News API: Dating-related news articles
- Refresh: Every 6 hours

**Key Visualizations:**
- Line charts: Topic trends over time
- Bar charts: Comparison metrics
- Heat maps: Discussion intensity
- Gauge charts: Sentiment scores

---

#### Tab 2: 💡 Attraction Science Hub
**Purpose:** Research-backed insights on what drives attraction

**Components:**
1. **Physical Attraction Factors**
   - Height preferences distribution
   - Body type preferences by gender
   - First impression factors ranked

2. **Behavioral Attraction Signals**
   - Most attractive personality traits
   - Communication style effectiveness
   - Confidence vs. arrogance spectrum

3. **Research Summary Cards**
   - Key studies with citations
   - Practical implications
   - Action items

**Data Sources:**
- Curated research database (from `research_backed_predictions.md`)
- Academic journals (pre-loaded data)
- Survey results aggregation

**Key Visualizations:**
- Radar charts: Multi-dimensional attraction factors
- Stacked bars: Gender-comparative preferences
- Scatter plots: Correlation analyses
- Info cards: Research highlights

---

#### Tab 3: ⚖️ Gender Dynamics Analyzer
**Purpose:** Comparative insights on male/female perspectives

**Components:**
1. **Communication Style Differences**
   - Directness vs. subtlety by gender
   - Emoji usage patterns
   - Response time expectations

2. **Dating Expectations Gap**
   - Who pays expectations
   - Timeline expectations (exclusivity, meeting family, etc.)
   - Deal-breakers comparison

3. **Emotional Intelligence Metrics**
   - Emotional expression patterns
   - Conflict resolution approaches
   - Vulnerability comfort levels

**Data Sources:**
- Reddit sentiment analysis
- Survey data compilation
- YouTube comment analysis

**Key Visualizations:**
- Dual-axis charts: Male vs. Female metrics
- Diverging bar charts: Preference gaps
- Network graphs: Interaction patterns
- Distribution curves: Expectation ranges

---

#### Tab 4: 🎯 Predictions & Probabilities
**Purpose:** Data-driven predictions on dating success factors

**Components:**
1. **Success Probability Calculator**
   - Input: Age, location, interests
   - Output: Match probability score
   - Confidence intervals displayed

2. **Timeline Predictions**
   - Expected time to first date
   - Relationship progression timeline
   - Seasonal trends in dating activity

3. **Market-Style Odds Display**
   - "Probability of..." style metrics
   - Green/red indicators for favorable/unfavorable
   - Historical trend comparison

**Data Sources:**
- ML models trained on Reddit data
- Historical dating statistics
- User behavior patterns

**Key Visualizations:**
- Probability gauges: 0-100% with confidence bands
- Timeline charts: Expected progression
- Odds comparison tables: Factor impacts
- Prediction intervals: Upper/lower bounds

---

#### Tab 5: 🎭 Social Skills Lab
**Purpose:** Actionable guidance on improving social effectiveness

**Components:**
1. **Communication Effectiveness Analyzer**
   - Message tone analysis
   - Response rate predictions
   - Conversation starter effectiveness

2. **Body Language Decoder**
   - Common signals and interpretations
   - Gender-specific differences
   - Cultural considerations

3. **Social Calibration Tool**
   - Context-appropriate behavior guides
   - Social faux pas to avoid
   - Recovery strategies

**Data Sources:**
- Text analysis of successful conversations
- Social psychology research database
- User-submitted examples (anonymized)

**Key Visualizations:**
- Flow diagrams: Conversation paths
- Heat maps: Effectiveness scores
- Decision trees: Situation-based guidance
- Before/after comparisons: Message improvements

---

#### Tab 6: 🧬 Personalization Engine
**Purpose:** Customized insights based on user profile

**Components:**
1. **Profile Input Form**
   - Age, gender, location
   - Dating goals
   - Interests and preferences

2. **Custom Recommendations Dashboard**
   - Personalized success predictions
   - Tailored action items
   - Relevant research highlights

3. **Progress Tracker**
   - Goals setting
   - Milestone tracking
   - Comparison to benchmarks

**Data Sources:**
- User input data (session-based, no storage in MVP)
- ML recommendation engine
- Filtered dataset based on profile

**Key Visualizations:**
- Profile summary cards
- Custom metric displays
- Progress bars and milestones
- Personalized charts

---

## TECHNICAL IMPLEMENTATION

### Project Structure
```
polymarket_gated_dashboard/
├── .gitignore
├── README.md
├── requirements.txt
├── start.sh                          # Startup script
│
├── .streamlit/
│   ├── config.toml                   # Streamlit config, theme
│   └── secrets.toml                  # API keys, access code (not in repo)
│
├── src/
│   ├── __init__.py
│   ├── app.py                        # MAIN ENTRY POINT
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   └── access_gate.py            # Authentication logic
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── design_system.py          # Polymarket theme colors/styles
│   │   └── constants.py              # App constants
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   ├── collectors/
│   │   │   ├── __init__.py
│   │   │   ├── reddit_collector.py   # PRAW integration
│   │   │   ├── news_collector.py     # News API integration
│   │   │   └── youtube_collector.py  # YouTube API integration
│   │   ├── processors/
│   │   │   ├── __init__.py
│   │   │   ├── nlp_processor.py      # Text analysis
│   │   │   ├── sentiment_analyzer.py # VADER sentiment
│   │   │   └── data_cleaner.py       # Data cleaning
│   │   └── database/
│   │       ├── __init__.py
│   │       └── db_manager.py         # SQLite operations
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── prediction_engine.py      # ML predictions
│   │   └── recommendation_engine.py  # Personalization
│   │
│   ├── visualizations/
│   │   ├── __init__.py
│   │   ├── charts.py                 # Reusable Plotly charts
│   │   ├── metrics.py                # Metric card components
│   │   └── tables.py                 # Table components
│   │
│   ├── tabs/
│   │   ├── __init__.py
│   │   ├── tab1_trends.py            # Social Trends Monitor
│   │   ├── tab2_attraction.py        # Attraction Science Hub
│   │   ├── tab3_gender.py            # Gender Dynamics Analyzer
│   │   ├── tab4_predictions.py       # Predictions & Probabilities
│   │   ├── tab5_social.py            # Social Skills Lab
│   │   └── tab6_personalization.py   # Personalization Engine
│   │
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py                # Utility functions
│       └── cache_manager.py          # Caching strategies
│
├── data/
│   ├── raw/                          # Raw API responses
│   ├── processed/                    # Cleaned data
│   ├── research/                     # Research database
│   └── database.db                   # SQLite database
│
├── assets/
│   ├── images/                       # Icons, logos
│   └── styles/                       # Custom CSS
│
└── tests/
    ├── __init__.py
    └── test_collectors.py            # Basic tests
```

### Key Dependencies
```txt
# requirements.txt
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0
altair>=5.0.0
scikit-learn>=1.3.0
praw>=7.7.0
requests>=2.31.0
nltk>=3.8.0
textblob>=0.17.0
vaderSentiment>=3.3.2
python-dotenv>=1.0.0
```

### Streamlit Configuration
```toml
# .streamlit/config.toml
[theme]
primaryColor = "#00e676"
backgroundColor = "#0a0e27"
secondaryBackgroundColor = "#1a1f35"
textColor = "#ffffff"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
```

### Secrets Management
```toml
# .streamlit/secrets.toml (NEVER commit to repo)
ACCESS_CODE = "your_secure_code_here"

[reddit]
client_id = "your_reddit_client_id"
client_secret = "your_reddit_client_secret"
user_agent = "social-intelligence-platform"

[news_api]
api_key = "your_news_api_key"

[youtube]
api_key = "your_youtube_api_key"
```

---

## DATA PIPELINE

### Data Collection Strategy

#### Reddit Data (PRAW)
```python
# Subreddits to monitor
TARGET_SUBREDDITS = [
    'dating',
    'relationships',
    'dating_advice',
    'AskMen',
    'AskWomen',
    'seduction',
    'relationship_advice'
]

# Collection parameters
- Time range: Past 7 days
- Post types: Hot, top, new
- Limit: 100 posts per subreddit
- Comments: Top 50 per post
- Refresh interval: 6 hours
```

#### News API
```python
# Query parameters
KEYWORDS = [
    'dating trends',
    'relationship advice',
    'attraction psychology',
    'social dynamics'
]

# Collection parameters
- Language: English
- Sort by: Relevance, date
- Time range: Past 30 days
- Refresh interval: 24 hours
```

#### YouTube API
```python
# Search parameters
SEARCH_QUERIES = [
    'dating advice',
    'attraction explained',
    'relationship tips'
]

# Collection parameters
- Video type: Any
- Order: Relevance
- Limit: 50 videos per query
- Analyze: Comments sentiment
- Refresh interval: 24 hours
```

### Data Processing Pipeline
1. **Collection:** API calls via scheduled jobs
2. **Cleaning:** Remove duplicates, filter spam
3. **NLP Processing:** Sentiment analysis, topic extraction
4. **Aggregation:** Summary statistics, trends
5. **Storage:** SQLite database
6. **Caching:** Streamlit cache for performance

### Database Schema
```sql
-- Posts table
CREATE TABLE posts (
    id TEXT PRIMARY KEY,
    source TEXT,
    title TEXT,
    content TEXT,
    author TEXT,
    timestamp INTEGER,
    score INTEGER,
    sentiment_score REAL,
    gender_tag TEXT
);

-- Topics table
CREATE TABLE topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    count INTEGER,
    avg_sentiment REAL,
    date TEXT
);

-- Trends table
CREATE TABLE trends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    velocity REAL,
    gender TEXT,
    timestamp INTEGER
);
```

---

## DEVELOPMENT PHASES

### Phase 1: Foundation (Week 1)
**Goal:** Project setup, access gate, design system

**Tasks:**
- [phase1-1] Project structure setup
- [phase1-2] Install dependencies, configure environment
- [phase1-3] Implement access gate with session management
- [phase1-4] Create Polymarket design system (colors, components)
- [phase1-5] Build reusable chart components
- [phase1-6] Setup Streamlit config with dark theme

**Deliverable:** Gated app with design system, no data yet

---

### Phase 2: Data Pipeline (Week 2)
**Goal:** Data collection, processing, and storage

**Tasks:**
- [phase2-1] Reddit API integration (PRAW)
- [phase2-2] News API integration
- [phase2-3] YouTube API integration
- [phase2-4] NLP processing (sentiment, topics)
- [phase2-5] SQLite database setup
- [phase2-6] Data caching strategy
- [phase2-7] Initial data collection and verification

**Deliverable:** Working data pipeline with populated database

---

### Phase 3: Core Tabs (Week 3)
**Goal:** Build Tabs 1-3 with live data

**Tasks:**
- [phase3-1] Tab 1: Social Trends Monitor (trending topics, heat maps)
- [phase3-2] Tab 1: Gender comparison visualizations
- [phase3-3] Tab 2: Attraction Science Hub (research cards)
- [phase3-4] Tab 2: Factor analysis charts
- [phase3-5] Tab 3: Gender Dynamics Analyzer (communication styles)
- [phase3-6] Tab 3: Expectations gap visualizations

**Deliverable:** 3 fully functional tabs with Polymarket styling

---

### Phase 4: Advanced Features (Week 4)
**Goal:** Complete Tabs 4-6, polish, and deploy

**Tasks:**
- [phase4-1] Tab 4: Predictions engine (ML models)
- [phase4-2] Tab 4: Probability displays, market-style odds
- [phase4-3] Tab 5: Social Skills Lab (effectiveness analyzer)
- [phase4-4] Tab 5: Body language decoder
- [phase4-5] Tab 6: Personalization Engine (input forms)
- [phase4-6] Tab 6: Custom recommendations
- [phase4-7] Performance optimization
- [phase4-8] Mobile responsiveness
- [phase4-9] Deployment to Streamlit Cloud
- [phase4-10] User testing and bug fixes

**Deliverable:** Production-ready platform, all 6 tabs live

---

## POLYMARKET-STYLE COMPONENTS

### Metric Card Template
```python
def metric_card(title, value, change, positive=True):
    """Polymarket-style metric card"""
    color = GREEN_PRIMARY if positive else RED_PRIMARY
    arrow = "↑" if positive else "↓"
    
    return f"""
    <div style="
        background: {BACKGROUND_CARD};
        border: 1px solid {BORDER_COLOR};
        border-radius: 8px;
        padding: 20px;
        margin: 10px 0;
    ">
        <p style="color: {TEXT_SECONDARY}; font-size: 12px; margin: 0;">
            {title}
        </p>
        <h2 style="color: {TEXT_PRIMARY}; font-size: 32px; margin: 10px 0;">
            {value}
        </h2>
        <p style="color: {color}; font-size: 14px; margin: 0;">
            {arrow} {change}
        </p>
    </div>
    """
```

### Probability Display
```python
def probability_gauge(label, probability, confidence_low, confidence_high):
    """Market-style probability gauge with confidence interval"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = probability,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': label, 'font': {'color': TEXT_PRIMARY}},
        delta = {'reference': 50, 'increasing': {'color': GREEN_PRIMARY}},
        gauge = {
            'axis': {'range': [None, 100], 'tickcolor': TEXT_SECONDARY},
            'bar': {'color': GREEN_PRIMARY if probability > 50 else RED_PRIMARY},
            'bgcolor': BACKGROUND_SECONDARY,
            'bordercolor': BORDER_COLOR,
            'steps': [
                {'range': [confidence_low, confidence_high], 'color': BACKGROUND_CARD}
            ],
            'threshold': {
                'line': {'color': TEXT_PRIMARY, 'width': 4},
                'thickness': 0.75,
                'value': probability
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor=BACKGROUND_PRIMARY,
        font={'color': TEXT_PRIMARY}
    )
    
    return fig
```

### Market-Style Table
```python
def market_table(data):
    """Polymarket-style data table"""
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=list(data.columns),
            fill_color=BACKGROUND_SECONDARY,
            line_color=BORDER_COLOR,
            font=dict(color=TEXT_PRIMARY, size=12),
            align='left'
        ),
        cells=dict(
            values=[data[col] for col in data.columns],
            fill_color=[
                [BACKGROUND_CARD if i % 2 == 0 else BACKGROUND_PRIMARY 
                 for i in range(len(data))]
            ],
            line_color=BORDER_COLOR,
            font=dict(color=TEXT_PRIMARY, size=11),
            align='left'
        )
    )])
    
    fig.update_layout(
        paper_bgcolor=BACKGROUND_PRIMARY,
        margin=dict(l=0, r=0, t=0, b=0)
    )
    
    return fig
```

---

## PERFORMANCE OPTIMIZATION

### Caching Strategy
```python
# Cache API calls for 6 hours
@st.cache_data(ttl=21600)
def fetch_reddit_data():
    pass

# Cache processed data for 1 hour
@st.cache_data(ttl=3600)
def process_sentiment_data():
    pass

# Cache visualizations
@st.cache_resource
def create_trend_chart():
    pass
```

### Loading States
- Show skeleton loaders during data fetch
- Progressive rendering (load tabs on demand)
- Lazy loading for images and heavy components

### Data Optimization
- Paginate large datasets
- Aggregate data for visualizations
- Use efficient data structures (numpy arrays)
- Compress stored data

---

## DEPLOYMENT CHECKLIST

### Pre-Deployment
- [ ] All API keys in secrets
- [ ] Access code configured
- [ ] Database populated with initial data
- [ ] All 6 tabs functional
- [ ] Mobile responsive design verified
- [ ] Performance testing completed
- [ ] Error handling implemented
- [ ] Loading states added

### Streamlit Cloud Deployment
1. Push code to GitHub (exclude secrets)
2. Connect repository to Streamlit Cloud
3. Add secrets via Streamlit Cloud UI
4. Configure resources (memory, CPU)
5. Deploy and monitor

### Post-Deployment
- [ ] Verify all features work in production
- [ ] Check API rate limits
- [ ] Monitor performance metrics
- [ ] Test access gate functionality
- [ ] Collect initial user feedback
- [ ] Setup error logging
- [ ] Document known issues

---

## SUCCESS METRICS

### Technical Metrics
- Page load time: < 2 seconds
- API response time: < 500ms
- Database query time: < 100ms
- Uptime: > 99%
- Mobile responsiveness score: > 90

### User Metrics
- Session duration: > 5 minutes
- Tab exploration rate: > 3 tabs per session
- Return rate: > 30%
- Access code success rate: > 95%
- Feature usage: All tabs used within first week

### Business Metrics
- Daily active users (DAU)
- User retention (D1, D7, D30)
- Feature adoption rates
- User feedback scores
- Conversion to personalization tab

---

## FUTURE ENHANCEMENTS (Post-MVP)

### V1.1 - Enhanced Access Control
- Individual user accounts
- Email-based access requests
- Usage analytics per user
- Time-limited access codes

### V1.2 - Data Expansion
- More subreddit sources
- Twitter/X API integration
- TikTok trends analysis
- Instagram insights

### V1.3 - Advanced Features
- Export reports to PDF
- Share custom insights
- Email alerts for trends
- API for third-party access

### V1.4 - Monetization
- Premium tier with advanced features
- B2B partnerships dashboard
- White-label versions
- Affiliate integration

---

## RISK MITIGATION

### Technical Risks
- **API Rate Limits:** Cache aggressively, use free tiers wisely
- **Data Quality:** Implement validation, filter spam
- **Performance:** Optimize queries, use CDN for assets
- **Security:** Never expose API keys, validate all inputs

### Business Risks
- **User Adoption:** Start with core network, gather feedback
- **Data Accuracy:** Clearly label predictions as estimates
- **Legal Issues:** Include disclaimers, follow platform ToS
- **Competition:** Focus on unique value prop (gender-comparative insights)

---

## SUPPORT & RESOURCES

### Documentation
- README.md: Setup instructions
- API_DOCS.md: Data pipeline documentation
- DESIGN_SYSTEM.md: Component library
- DEPLOYMENT.md: Deployment guide

### Reference Materials
- Original dev brief: `/Users/jeremywilliams/Downloads/dev_brief.md`
- Polymarket design: https://polymarket.com
- Streamlit docs: https://docs.streamlit.io
- PRAW docs: https://praw.readthedocs.io

### Key Contacts
- **Client:** Jeremy Williams / Vyudu Inc
- **Developer:** Memex.Tech
- **Support:** [Support channel TBD]

---

## QUICK START COMMANDS

```bash
# Initial setup
cd /Users/jeremywilliams/Workspace/polymarket_gated_dashboard
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Configure secrets
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit secrets.toml with your API keys

# Run locally
./start.sh
# or
streamlit run src/app.py

# Deploy
git push origin main
# Then deploy via Streamlit Cloud UI
```

---

## NOTES

- Design system heavily inspired by Polymarket's clean, data-driven aesthetic
- Access gate is intentionally simple for MVP (can enhance later)
- Gender color scheme (Blue/Red) maintained from original brief despite Polymarket's green/red for market metrics
- All free-tier APIs, no costs for MVP deployment
- SQLite sufficient for MVP, can migrate to PostgreSQL/Supabase later if needed

---

**Ready to build. Ship fast, iterate based on real usage data.**
