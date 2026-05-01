"""
Reusable KPI (Key Performance Indicator) card components for dashboard display.
Provides styled metric cards with trend indicators and comparisons.
"""

import streamlit as st
from typing import Optional, Dict, Any
from datetime import datetime
import math


def kpi_card(
    title: str,
    value: float,
    metric_suffix: str = "",
    metric_prefix: str = "",
    delta: Optional[float] = None,
    delta_type: Optional[str] = None,
    icon: Optional[str] = None,
    color: str = "#1f77b4",
    comparison_text: Optional[str] = None,
) -> None:
    """
    Display a KPI card with value, delta, and optional trend indicator.
    
    Args:
        title: KPI title/label
        value: Numeric value to display
        metric_suffix: Suffix for the metric (e.g., "%", "units")
        metric_prefix: Prefix for the metric (e.g., "$")
        delta: Change value (optional, for trend)
        delta_type: Type of delta - "up" (positive/good), "down" (negative/good), 
                   "neutral" (no indicator), or None (auto-detect from delta sign)
        icon: Emoji or text icon to display (optional)
        color: Hex color code for the card border
        comparison_text: Text for comparison (e.g., "vs last month")
    
    Returns:
        None - renders card in Streamlit
    """
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Title
        st.markdown(f"<span style='font-size: 14px; color: #666;'>{title}</span>", unsafe_allow_html=True)
        
        # Main value
        value_str = f"{metric_prefix}{value:,.2f}{metric_suffix}" if isinstance(value, (int, float)) else str(value)
        st.markdown(
            f"<span style='font-size: 32px; font-weight: bold; color: {color};'>{value_str}</span>",
            unsafe_allow_html=True,
        )
        
        # Comparison text
        if comparison_text:
            st.markdown(f"<span style='font-size: 12px; color: #999;'>{comparison_text}</span>", unsafe_allow_html=True)
    
    with col2:
        if icon:
            st.markdown(f"<span style='font-size: 40px;'>{icon}</span>", unsafe_allow_html=True)
        elif delta is not None:
            # Display trend indicator
            if delta_type is None:
                # Auto-detect based on delta sign
                delta_type = "up" if delta >= 0 else "down"
            
            if delta_type == "up":
                indicator = "📈"
                delta_color = "#27ae60" if delta >= 0 else "#e74c3c"
            elif delta_type == "down":
                indicator = "📉"
                delta_color = "#e74c3c" if delta >= 0 else "#27ae60"
            else:
                indicator = "➡️"
                delta_color = "#95a5a6"
            
            st.markdown(f"<span style='font-size: 28px;'>{indicator}</span>", unsafe_allow_html=True)
            
            # Delta value
            delta_str = f"{metric_prefix}{abs(delta):,.2f}{metric_suffix}" if isinstance(delta, (int, float)) else str(abs(delta))
            sign = "+" if delta >= 0 else "-"
            st.markdown(
                f"<span style='font-size: 14px; color: {delta_color}; font-weight: bold;'>{sign}{delta_str}</span>",
                unsafe_allow_html=True,
            )


def metric_row(
    metrics: Dict[str, Dict[str, Any]],
    columns: int = 3,
) -> None:
    """
    Display multiple KPI cards in a row.
    
    Args:
        metrics: Dictionary of metric data with format:
                {
                    "metric_name": {
                        "value": 1000,
                        "title": "Sales",
                        "delta": 50,
                        "icon": "💰",
                        "color": "#1f77b4",
                        "suffix": "$",
                        "comparison": "vs last month"
                    }
                }
        columns: Number of columns to display
    
    Returns:
        None - renders cards in Streamlit
    """
    cols = st.columns(columns)
    
    for idx, (metric_key, metric_data) in enumerate(metrics.items()):
        with cols[idx % columns]:
            kpi_card(
                title=metric_data.get("title", metric_key),
                value=metric_data.get("value", 0),
                metric_suffix=metric_data.get("suffix", ""),
                metric_prefix=metric_data.get("prefix", ""),
                delta=metric_data.get("delta"),
                delta_type=metric_data.get("delta_type"),
                icon=metric_data.get("icon"),
                color=metric_data.get("color", "#1f77b4"),
                comparison_text=metric_data.get("comparison"),
            )


def status_badge(
    label: str,
    value: str,
    status: str = "neutral",
) -> None:
    """
    Display a status badge with color-coded indicator.
    
    Args:
        label: Label for the badge
        value: Value/status text to display
        status: "good", "warning", "critical", or "neutral"
    
    Returns:
        None - renders badge in Streamlit
    """
    status_colors = {
        "good": "#27ae60",
        "warning": "#f39c12",
        "critical": "#e74c3c",
        "neutral": "#95a5a6",
    }
    
    color = status_colors.get(status, status_colors["neutral"])
    
    st.markdown(
        f"""
        <div style='
            background-color: {color}20;
            border-left: 4px solid {color};
            padding: 12px;
            border-radius: 4px;
            margin-bottom: 10px;
        '>
            <span style='color: #666; font-size: 12px;'>{label}</span>
            <br>
            <span style='color: {color}; font-size: 16px; font-weight: bold;'>{value}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def progress_indicator(
    title: str,
    current: float,
    target: float,
    unit: str = "",
    color: str = "#1f77b4",
) -> None:
    """
    Display a progress indicator card.
    
    Args:
        title: Title of the metric
        current: Current value
        target: Target/goal value
        unit: Unit of measurement
        color: Hex color for the progress bar
    
    Returns:
        None - renders progress indicator in Streamlit
    """
    percentage = (current / target) * 100 if target > 0 else 0
    percentage = min(100, max(0, percentage))  # Clamp between 0-100
    
    st.markdown(
        f"""
        <div style='margin-bottom: 20px;'>
            <span style='font-size: 14px; color: #666;'>{title}</span>
            <br>
            <div style='
                background-color: #f0f0f0;
                height: 24px;
                border-radius: 4px;
                overflow: hidden;
                margin: 8px 0;
            '>
                <div style='
                    background: linear-gradient(90deg, {color}, {color}dd);
                    height: 100%;
                    width: {percentage}%;
                    transition: width 0.3s ease;
                    display: flex;
                    align-items: center;
                    justify-content: flex-end;
                    padding-right: 8px;
                '>
                    <span style='
                        color: white;
                        font-size: 12px;
                        font-weight: bold;
                        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
                    '>{percentage:.0f}%</span>
                </div>
            </div>
            <span style='font-size: 12px; color: #999;'>
                {current:.1f}{unit} / {target:.1f}{unit}
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def summary_stat_grid(
    stats: Dict[str, Dict[str, Any]],
    rows: int = 2,
    columns: int = 2,
) -> None:
    """
    Display summary statistics in a grid layout.
    
    Args:
        stats: Dictionary of statistics with format:
               {
                   "stat_key": {
                       "label": "Label",
                       "value": "Value",
                       "status": "good|warning|critical|neutral"
                   }
               }
        rows: Number of rows in grid
        columns: Number of columns in grid
    
    Returns:
        None - renders grid in Streamlit
    """
    for row_idx in range(rows):
        cols = st.columns(columns)
        for col_idx in range(columns):
            stat_idx = row_idx * columns + col_idx
            stat_keys = list(stats.keys())
            
            if stat_idx < len(stat_keys):
                with cols[col_idx]:
                    stat_key = stat_keys[stat_idx]
                    stat_data = stats[stat_key]
                    status_badge(
                        label=stat_data.get("label", stat_key),
                        value=stat_data.get("value", "N/A"),
                        status=stat_data.get("status", "neutral"),
                    )


def change_indicator(
    current: float,
    previous: float,
    metric_suffix: str = "",
    metric_prefix: str = "",
    show_percentage: bool = True,
) -> None:
    """
    Display a change indicator showing difference between current and previous values.
    
    Args:
        current: Current value
        previous: Previous value
        metric_suffix: Suffix for the metric
        metric_prefix: Prefix for the metric
        show_percentage: Whether to show percentage change
    
    Returns:
        None - renders indicator in Streamlit
    """
    if previous == 0:
        percentage_change = 0
        absolute_change = current
    else:
        absolute_change = current - previous
        percentage_change = (absolute_change / abs(previous)) * 100
    
    # Determine color based on change direction
    change_color = "#27ae60" if absolute_change >= 0 else "#e74c3c"
    change_icon = "📈" if absolute_change >= 0 else "📉"
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        change_str = f"{metric_prefix}{abs(absolute_change):,.2f}{metric_suffix}"
        st.markdown(
            f"<span style='font-size: 18px; color: {change_color}; font-weight: bold;'>"
            f"{'+'if absolute_change >= 0 else '-'}{change_str}</span>",
            unsafe_allow_html=True,
        )
        
        if show_percentage:
            pct_str = f"{abs(percentage_change):.1f}%"
            st.markdown(
                f"<span style='font-size: 14px; color: {change_color};'>"
                f"{pct_str} change</span>",
                unsafe_allow_html=True,
            )
    
    with col2:
        st.markdown(f"<span style='font-size: 24px;'>{change_icon}</span>", unsafe_allow_html=True)


def alert_card(
    message: str,
    alert_type: str = "info",
    title: Optional[str] = None,
) -> None:
    """
    Display an alert/notification card.
    
    Args:
        message: Alert message text
        alert_type: "info", "success", "warning", or "error"
        title: Optional alert title
    
    Returns:
        None - renders alert in Streamlit
    """
    alert_styles = {
        "info": {"bg": "#d1ecf1", "border": "#0c5460", "text": "#0c5460"},
        "success": {"bg": "#d4edda", "border": "#155724", "text": "#155724"},
        "warning": {"bg": "#fff3cd", "border": "#856404", "text": "#856404"},
        "error": {"bg": "#f8d7da", "border": "#721c24", "text": "#721c24"},
    }
    
    style = alert_styles.get(alert_type, alert_styles["info"])
    
    alert_html = f"""
    <div style='
        background-color: {style["bg"]};
        border-left: 4px solid {style["border"]};
        padding: 12px;
        border-radius: 4px;
        margin-bottom: 10px;
    '>
    """
    
    if title:
        alert_html += f"<span style='color: {style['text']}; font-weight: bold; font-size: 14px;'>{title}</span><br>"
    
    alert_html += f"<span style='color: {style['text']}; font-size: 13px;'>{message}</span></div>"
    
    st.markdown(alert_html, unsafe_allow_html=True)


def comparison_cards(
    items: Dict[str, Dict[str, Any]],
    columns: int = 3,
) -> None:
    """
    Display comparison cards for side-by-side metric comparison.
    
    Args:
        items: Dictionary with format:
               {
                   "item_key": {
                       "name": "Item Name",
                       "value": 100,
                       "unit": "units",
                       "rank": 1,
                       "highlight": True/False
                   }
               }
        columns: Number of columns to display
    
    Returns:
        None - renders comparison cards in Streamlit
    """
    cols = st.columns(columns)
    
    for idx, (item_key, item_data) in enumerate(items.items()):
        with cols[idx % columns]:
            highlight = item_data.get("highlight", False)
            border_color = "#f39c12" if highlight else "#e0e0e0"
            bg_color = "#fffbf0" if highlight else "#ffffff"
            
            st.markdown(
                f"""
                <div style='
                    background-color: {bg_color};
                    border: 2px solid {border_color};
                    padding: 16px;
                    border-radius: 8px;
                    text-align: center;
                '>
                    <span style='color: #666; font-size: 12px;'>{item_data.get("name", item_key)}</span>
                    <br>
                    <span style='color: #1f1f1f; font-size: 24px; font-weight: bold;'>
                        {item_data.get("value", 0)}{item_data.get("unit", "")}
                    </span>
                    {f"<br><span style='color: #f39c12; font-size: 12px; font-weight: bold;'>Rank #{item_data.get('rank', 'N/A')}</span>" if "rank" in item_data else ""}
                </div>
                """,
                unsafe_allow_html=True,
            )
