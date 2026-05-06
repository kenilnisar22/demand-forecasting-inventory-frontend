"""
Spend Overview Page
Displays spending analysis, cost trends, and budget tracking across inventory and operations.
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import sys
from pathlib import Path

# Add parent directory to path for component imports
sys.path.append(str(Path(__file__).parent.parent))
from components.kpis import kpi_card


# Page configuration
st.set_page_config(
    page_title="Spend Overview",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
    }
    .chart-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    """Main function for Spend Overview page."""
    
    # Page header
    st.title("💰 Spend Overview")
    st.markdown("---")
    
    # Date range filter
    col1, col2, col3 = st.columns(3)
    with col1:
        start_date = st.date_input(
            "Start Date",
            value=datetime.now() - timedelta(days=30),
            key="spend_start_date",
        )
    with col2:
        end_date = st.date_input(
            "End Date",
            value=datetime.now(),
            key="spend_end_date",
        )
    with col3:
        filter_category = st.selectbox(
            "Category",
            ["All", "Inventory", "Operations", "Logistics", "Other"],
            key="spend_category",
        )
    
    st.markdown("---")
    
    # === KEY METRICS SECTION ===
    st.subheader("📊 Key Spending Metrics")
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    
    with kpi_col1:
        with st.container():
            st.markdown(
                '<div class="metric-container">'
                '<p style="margin: 0; font-size: 14px; opacity: 0.9;">Total Spend</p>'
                '<p style="margin: 10px 0 0 0; font-size: 32px; font-weight: bold;">$150,420</p>'
                '<p style="margin: 5px 0 0 0; font-size: 12px; opacity: 0.8;">↑ 12.5% vs last month</p>'
                '</div>',
                unsafe_allow_html=True,
            )
    
    with kpi_col2:
        with st.container():
            st.markdown(
                '<div class="metric-container" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">'
                '<p style="margin: 0; font-size: 14px; opacity: 0.9;">Avg Daily Spend</p>'
                '<p style="margin: 10px 0 0 0; font-size: 32px; font-weight: bold;">$4,854</p>'
                '<p style="margin: 5px 0 0 0; font-size: 12px; opacity: 0.8;">↓ 3.2% vs last period</p>'
                '</div>',
                unsafe_allow_html=True,
            )
    
    with kpi_col3:
        with st.container():
            st.markdown(
                '<div class="metric-container" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">'
                '<p style="margin: 0; font-size: 14px; opacity: 0.9;">Budget Utilization</p>'
                '<p style="margin: 10px 0 0 0; font-size: 32px; font-weight: bold;">78.5%</p>'
                '<p style="margin: 5px 0 0 0; font-size: 12px; opacity: 0.8;">$21% remaining</p>'
                '</div>',
                unsafe_allow_html=True,
            )
    
    with kpi_col4:
        with st.container():
            st.markdown(
                '<div class="metric-container" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">'
                '<p style="margin: 0; font-size: 14px; opacity: 0.9;">Top Category</p>'
                '<p style="margin: 10px 0 0 0; font-size: 32px; font-weight: bold;">Inventory</p>'
                '<p style="margin: 5px 0 0 0; font-size: 12px; opacity: 0.8;">52% of total spend</p>'
                '</div>',
                unsafe_allow_html=True,
            )
    
    st.markdown("---")
    
    # === SPENDING TRENDS SECTION ===
    st.subheader("📈 Spending Trends")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.markdown(
            '<div class="chart-container">'
            '<h4>Daily Spend Trend</h4>'
            '</div>',
            unsafe_allow_html=True,
        )
        # Placeholder for daily spend trend chart
        st.info("📊 Chart Placeholder: Daily Spend Trend Over Selected Period")
        st.markdown(
            "*This will display a line chart showing daily spending trends with options to drill down by category.*"
        )
    
    with chart_col2:
        st.markdown(
            '<div class="chart-container">'
            '<h4>Spend by Category</h4>'
            '</div>',
            unsafe_allow_html=True,
        )
        # Placeholder for spend by category chart
        st.info("📊 Chart Placeholder: Spend Distribution by Category")
        st.markdown(
            "*This will display a pie/donut chart showing percentage breakdown of spending by category.*"
        )
    
    st.markdown("---")
    
    # === DETAILED ANALYSIS SECTION ===
    st.subheader("📋 Detailed Spend Analysis")
    
    analysis_col1, analysis_col2 = st.columns(2)
    
    with analysis_col1:
        st.markdown(
            '<div class="chart-container">'
            '<h4>Top Spending Items</h4>'
            '</div>',
            unsafe_allow_html=True,
        )
        # Placeholder for top spending items
        st.info("📊 Chart Placeholder: Top 10 Spending Items")
        st.markdown(
            "*This will display a horizontal bar chart showing the top spending items/suppliers.*"
        )
    
    with analysis_col2:
        st.markdown(
            '<div class="chart-container">'
            '<h4>Spend Variance Analysis</h4>'
            '</div>',
            unsafe_allow_html=True,
        )
        # Placeholder for spend variance
        st.info("📊 Chart Placeholder: Budget vs Actual Spend")
        st.markdown(
            "*This will display a comparison chart showing budget vs actual spending with variance indicators.*"
        )
    
    st.markdown("---")
    
    # === CATEGORY BREAKDOWN SECTION ===
    st.subheader("💳 Category Breakdown")
    
    category_col1, category_col2, category_col3 = st.columns(3)
    
    with category_col1:
        st.markdown(
            '<div class="chart-container">'
            '<h4>Inventory Spending</h4>'
            '</div>',
            unsafe_allow_html=True,
        )
        st.metric("Total", "$78,218", "+5.2%")
        st.markdown("📊 Placeholder: Inventory spend breakdown")
    
    with category_col2:
        st.markdown(
            '<div class="chart-container">'
            '<h4>Operations Spending</h4>'
            '</div>',
            unsafe_allow_html=True,
        )
        st.metric("Total", "$45,320", "-2.1%")
        st.markdown("📊 Placeholder: Operations spend breakdown")
    
    with category_col3:
        st.markdown(
            '<div class="chart-container">'
            '<h4>Logistics Spending</h4>'
            '</div>',
            unsafe_allow_html=True,
        )
        st.metric("Total", "$26,882", "+8.3%")
        st.markdown("📊 Placeholder: Logistics spend breakdown")
    
    st.markdown("---")
    
    # === DATA TABLE SECTION ===
    st.subheader("📑 Transaction Details")
    
    with st.expander("View Detailed Transactions", expanded=False):
        # Placeholder for transaction table
        st.info("📊 Placeholder: Detailed transaction list table")
        st.markdown(
            """
            *This will display a filterable and sortable table containing:*
            - Transaction Date
            - Category
            - Item/Supplier
            - Amount
            - Department
            - Status
            """
        )
    
    st.markdown("---")
    
    # === INSIGHTS & RECOMMENDATIONS SECTION ===
    st.subheader("💡 Insights & Recommendations")
    
    insight_col1, insight_col2 = st.columns(2)
    
    with insight_col1:
        st.markdown("**📌 Key Insights**")
        st.info(
            """
            - Spending increased by 12.5% compared to last month
            - Inventory category accounts for 52% of total spend
            - Top 3 suppliers represent 38% of total spending
            - Logistics costs show upward trend (↑8.3%)
            """
        )
    
    with insight_col2:
        st.markdown("**💭 Recommendations**")
        st.warning(
            """
            - Review top suppliers for cost optimization opportunities
            - Consider consolidating inventory purchases
            - Analyze logistics cost drivers for potential savings
            - Monitor budget utilization to stay within 80% threshold
            """
        )


if __name__ == "__main__":
    main()
