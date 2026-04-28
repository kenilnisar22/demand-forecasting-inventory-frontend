# Demand Forecasting & Inventory Management Frontend

A Streamlit-based web application for demand forecasting and inventory management. This frontend provides an intuitive interface for analyzing sales data, predicting future demand, and managing inventory levels.

## Features

- **Dashboard Overview** - Key metrics and visualizations at a glance
- **Demand Forecasting** - Predict future demand using historical data
- **Inventory Management** - Track and manage inventory levels
- **Data Visualization** - Interactive charts and graphs for analysis

## Tech Stack

- **Frontend**: Streamlit (Python)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Matplotlib
- **API Integration**: Requests for backend communication

## Project Structure

```
demand-forecasting-inventory-frontend/
├── README.md
├── requirements.txt
├── app/
│   ├── pages/          # Streamlit pages
│   └── components/     # Reusable UI components
├── assets/
│   └── screenshots/    # App screenshots
└── dashboard/          # Dashboard modules
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app/main.py
   ```

## Usage

Open your browser and navigate to `http://localhost:8501` after starting the application.

## License

MIT