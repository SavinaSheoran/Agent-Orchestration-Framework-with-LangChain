# tools.py  

from langchain_core.tools import tool, Tool
import requests
import random
import os

@tool("calculator", description="Performs arithmetic calculations. Use this for any math problems.")
def calculator(expression: str) -> str:
    """Evaluate mathematical expressions."""
    return str(eval(expression))




@tool("stock_price", description="Get current day price information for a stock. Example: 'RELIANCE.BSE'")
def stock_price(stock_symbol: str) -> str:
    """Fetch current day price information of a stock."""
    try:
        stock_api_key = os.getenv('stock_api_key')
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={stock_api_key}'
        r = requests.get(url)
        data = r.json()
        data = data['Global Quote']
        return f"""Stock Symbol: {data.get('01. symbol', 'N/A')} 
        | Open: {data.get('02. open', 'N/A')} | High: {data.get('03. high', 'N/A')} | Low: {data.get('04. low', 'N/A')} 
        | Close: {data.get('05. price', 'N/A')} | Volume: {data.get('06. volume', 'N/A')} 
        | Latest Trading Day: {data.get('07. latest trading day', 'N/A')}"""

    except Exception:
        return f"Error: Could not fetch stock price information for '{stock_symbol}'."

tools = [calculator, stock_price]