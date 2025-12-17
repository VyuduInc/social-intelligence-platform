#!/bin/bash

# Social Intelligence Platform - Startup Script
# Phase 1: Gated Dashboard with 3 Curated Tabs

echo "🚀 Starting Social Intelligence Platform..."
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "⚠️  Virtual environment not found. Creating one..."
    uv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies if needed
if ! python -c "import streamlit" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    uv pip install -r requirements.txt
    echo "✅ Dependencies installed"
fi

# Check if secrets file exists
if [ ! -f ".streamlit/secrets.toml" ]; then
    echo ""
    echo "⚠️  WARNING: .streamlit/secrets.toml not found!"
    echo "Creating default secrets file..."
    echo 'ACCESS_CODE = "vyudu2024"' > .streamlit/secrets.toml
    echo "✅ Default access code set to: vyudu2024"
    echo ""
fi

# Start the app
echo ""
echo "🎯 Launching dashboard..."
echo "📍 Access URL: http://localhost:8501"
echo "🔑 Access Code: vyudu2024"
echo ""
echo "Press Ctrl+C to stop the server"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

streamlit run src/app.py
