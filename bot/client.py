from binance.client import Client
from dotenv import load_dotenv
import os

from bot.logging_config import logger

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

try:
    # Create Binance client
    client = Client(API_KEY, API_SECRET)

    # Connect to Binance Futures Testnet
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    logger.info("Connected to Binance Futures Testnet successfully")

except Exception as e:
    logger.error(f"Error connecting to Binance Testnet: {e}")
    raise