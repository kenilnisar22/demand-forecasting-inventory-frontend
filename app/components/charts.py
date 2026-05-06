"""
Reusable chart components for demand forecasting and inventory management dashboard.
Provides interactive visualizations using Plotly and Matplotlib.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go  # type: ignore
import plotly.express as px  # type: ignore
from typing import List, Optional, Dict, Any
import numpy as np


def line_chart_with_forecast(
    df: pd.DataFrame,
    actual_column: str,
    forecast_column: Optional[str] = None,
    date_column: str = "date",
    title: str = "Demand Forecast",
    y_label: str = "Quantity",
    x_label: str = "Date",
    height: int = 400,
) -> "go.Figure":
    """
    Create an interactive line chart with optional forecast overlay.
    
    Args:
        df: DataFrame containing the data
        actual_column: Column name for actual values
        forecast_column: Column name for forecast values (optional)
        date_column: Column name for dates
        title: Chart title
        y_label: Y-axis label
        x_label: X-axis label
        height: Chart height in pixels
    
    Returns:
        Plotly Figure object
    """
    fig = go.Figure()
    
    # Add actual data line
    fig.add_trace(
        go.Scatter(
            x=df[date_column],
            y=df[actual_column],
            mode="lines+markers",
            name="Actual",
            line=dict(color="#1f77b4", width=2),
            marker=dict(size=5),
            hovertemplate="<b>Date:</b> %{x}<br><b>Actual:</b> %{y:.0f}<extra></extra>",
        )
    )
    
    # Add forecast line if provided
    if forecast_column and forecast_column in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df[date_column],
                y=df[forecast_column],
                mode="lines",
                name="Forecast",
                line=dict(color="#ff7f0e", width=2, dash="dash"),
                hovertemplate="<b>Date:</b> %{x}<br><b>Forecast:</b> %{y:.0f}<extra></extra>",
            )
        )
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color="#1f1f1f")),
        xaxis_title=x_label,
        yaxis_title=y_label,
        hovermode="x unified",
        height=height,
        template="plotly_white",
        margin=dict(l=40, r=40, t=40, b=40),
    )
    
    return fig


def bar_chart(
    df: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str = "Bar Chart",
    y_label: str = "Value",
    x_label: str = "Category",
    height: int = 400,
    color: str = "#1f77b4",
) -> go.Figure:
    """
    Create a reusable bar chart.
    
    Args:
        df: DataFrame containing the data
        x_column: Column name for x-axis
        y_column: Column name for y-axis values
        title: Chart title
        y_label: Y-axis label
        x_label: X-axis label
        height: Chart height in pixels
        color: Bar color
    
    Returns:
        Plotly Figure object
    """
    fig = go.Figure(
        data=[
            go.Bar(
                x=df[x_column],
                y=df[y_column],
                marker_color=color,
                hovertemplate=f"<b>{{x}}</b><br>{y_label}: {{y:.0f}}<extra></extra>",
            )
        ]
    )
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color="#1f1f1f")),
        xaxis_title=x_label,
        yaxis_title=y_label,
        height=height,
        template="plotly_white",
        margin=dict(l=40, r=40, t=40, b=40),
    )
    
    return fig


def multi_series_line_chart(
    df: pd.DataFrame,
    x_column: str,
    y_columns: List[str],
    title: str = "Multi-Series Chart",
    y_label: str = "Value",
    x_label: str = "Date",
    height: int = 400,
    colors: Optional[List[str]] = None,
) -> go.Figure:
    """
    Create a line chart with multiple series.
    
    Args:
        df: DataFrame containing the data
        x_column: Column name for x-axis
        y_columns: List of column names for y-axis values
        title: Chart title
        y_label: Y-axis label
        x_label: X-axis label
        height: Chart height in pixels
        colors: List of colors for each series (optional)
    
    Returns:
        Plotly Figure object
    """
    if colors is None:
        colors = px.colors.qualitative.Plotly
    
    fig = go.Figure()
    
    for idx, col in enumerate(y_columns):
        color = colors[idx % len(colors)]  # type: ignore
        fig.add_trace(
            go.Scatter(
                x=df[x_column],
                y=df[col],
                mode="lines+markers",
                name=col,
                line=dict(color=color, width=2),
                marker=dict(size=5),
                hovertemplate=f"<b>{{x}}</b><br>{col}: {{y:.2f}}<extra></extra>",
            )
        )
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color="#1f1f1f")),
        xaxis_title=x_label,
        yaxis_title=y_label,
        hovermode="x unified",
        height=height,
        template="plotly_white",
        margin=dict(l=40, r=40, t=40, b=40),
    )
    
    return fig


def distribution_chart(
    data: List[float],
    title: str = "Distribution",
    x_label: str = "Value",
    y_label: str = "Frequency",
    nbins: int = 30,
    height: int = 400,
) -> go.Figure:
    """
    Create a histogram for data distribution.
    
    Args:
        data: List of numeric values
        title: Chart title
        x_label: X-axis label
        y_label: Y-axis label
        nbins: Number of bins for histogram
        height: Chart height in pixels
    
    Returns:
        Plotly Figure object
    """
    fig = go.Figure(
        data=[
            go.Histogram(
                x=data,
                nbinsx=nbins,
                marker_color="#1f77b4",
                hovertemplate="<b>Range:</b> %{x}<br><b>Frequency:</b> %{y}<extra></extra>",
            )
        ]
    )
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color="#1f1f1f")),
        xaxis_title=x_label,
        yaxis_title=y_label,
        height=height,
        template="plotly_white",
        margin=dict(l=40, r=40, t=40, b=40),
    )
    
    return fig


def heatmap_chart(
    df: pd.DataFrame,
    title: str = "Heatmap",
    color_scale: str = "Viridis",
    height: int = 500,
) -> go.Figure:
    """
    Create an interactive heatmap.
    
    Args:
        df: DataFrame containing the data
        title: Chart title
        color_scale: Plotly color scale name
        height: Chart height in pixels
    
    Returns:
        Plotly Figure object
    """
    fig = go.Figure(
        data=go.Heatmap(
            z=df.values,
            x=df.columns,
            y=df.index,
            colorscale=color_scale,
            hovertemplate="<b>%{y}</b><br>%{x}: %{z:.2f}<extra></extra>",
        )
    )
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color="#1f1f1f")),
        height=height,
        template="plotly_white",
        margin=dict(l=40, r=40, t=40, b=40),
    )
    
    return fig


def scatter_plot(
    df: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str = "Scatter Plot",
    x_label: str = "X",
    y_label: str = "Y",
    size_column: Optional[str] = None,
    color_column: Optional[str] = None,
    height: int = 400,
) -> go.Figure:
    """
    Create an interactive scatter plot with optional sizing and coloring.
    
    Args:
        df: DataFrame containing the data
        x_column: Column name for x-axis
        y_column: Column name for y-axis
        title: Chart title
        x_label: X-axis label
        y_label: Y-axis label
        size_column: Column name for marker size (optional)
        color_column: Column name for marker color (optional)
        height: Chart height in pixels
    
    Returns:
        Plotly Figure object
    """
    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        size=size_column,
        color=color_column,
        title=title,
        labels={x_column: x_label, y_column: y_label},
        height=height,
        template="plotly_white",
    )
    
    fig.update_layout(
        title=dict(font=dict(size=16, color="#1f1f1f")),
        hovermode="closest",
        margin=dict(l=40, r=40, t=40, b=40),
    )
    
    return fig


def box_plot(
    df: pd.DataFrame,
    x_column: Optional[str] = None,
    y_column: Optional[str] = None,
    title: str = "Box Plot",
    y_label: str = "Value",
    height: int = 400,
) -> go.Figure:
    """
    Create a box plot for distribution analysis.
    
    Args:
        df: DataFrame containing the data
        x_column: Column name for x-axis categories (optional)
        y_column: Column name for y-axis values
        title: Chart title
        y_label: Y-axis label
        height: Chart height in pixels
    
    Returns:
        Plotly Figure object
    """
    fig = px.box(
        df,
        x=x_column,
        y=y_column,
        title=title,
        labels={y_column: y_label},
        height=height,
        template="plotly_white",
    )
    
    fig.update_layout(
        title=dict(font=dict(size=16, color="#1f1f1f")),
        margin=dict(l=40, r=40, t=40, b=40),
    )
    
    return fig


def funnel_chart(
    stages: List[str],
    values: List[float],
    title: str = "Funnel Chart",
    height: int = 400,
) -> go.Figure:
    """
    Create a funnel chart for pipeline or conversion visualization.
    
    Args:
        stages: List of stage names
        values: List of corresponding values
        title: Chart title
        height: Chart height in pixels
    
    Returns:
        Plotly Figure object
    """
    fig = go.Figure(
        go.Funnel(
            y=stages,
            x=values,
            marker_color="#1f77b4",
            hovertemplate="<b>%{y}</b><br>Value: %{x:.0f}<extra></extra>",
        )
    )
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color="#1f1f1f")),
        height=height,
        template="plotly_white",
        margin=dict(l=40, r=40, t=40, b=40),
    )
    
    return fig


def confidence_interval_chart(
    df: pd.DataFrame,
    x_column: str,
    y_column: str,
    upper_bound_column: str,
    lower_bound_column: str,
    title: str = "Forecast with Confidence Interval",
    y_label: str = "Value",
    x_label: str = "Date",
    height: int = 400,
) -> go.Figure:
    """
    Create a chart with confidence interval bands.
    
    Args:
        df: DataFrame containing the data
        x_column: Column name for x-axis
        y_column: Column name for central values
        upper_bound_column: Column name for upper confidence bound
        lower_bound_column: Column name for lower confidence bound
        title: Chart title
        y_label: Y-axis label
        x_label: X-axis label
        height: Chart height in pixels
    
    Returns:
        Plotly Figure object
    """
    fig = go.Figure()
    
    # Add confidence interval as filled area
    fig.add_trace(
        go.Scatter(
            x=df[x_column],
            y=df[upper_bound_column],
            fill=None,
            mode="lines",
            line_color="rgba(0,100,80,0)",
            showlegend=False,
        )
    )
    
    fig.add_trace(
        go.Scatter(
            x=df[x_column],
            y=df[lower_bound_column],
            fill="tonexty",
            mode="lines",
            line_color="rgba(0,100,80,0)",
            name="95% Confidence Interval",
            fillcolor="rgba(0,100,80,0.2)",
        )
    )
    
    # Add central line
    fig.add_trace(
        go.Scatter(
            x=df[x_column],
            y=df[y_column],
            mode="lines",
            name="Forecast",
            line=dict(color="#ff7f0e", width=2),
            hovertemplate="<b>Date:</b> %{x}<br><b>Forecast:</b> %{y:.0f}<extra></extra>",
        )
    )
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color="#1f1f1f")),
        xaxis_title=x_label,
        yaxis_title=y_label,
        hovermode="x unified",
        height=height,
        template="plotly_white",
        margin=dict(l=40, r=40, t=40, b=40),
    )
    
    return fig
