from binance.exceptions import BinanceAPIException
from bot.client import client
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):

    try:

        logger.info(
            f"Placing order: {symbol} | {side} | {order_type} | Qty: {quantity} | Price: {price}"
        )

        # MARKET ORDER
        if order_type == "MARKET":

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        # LIMIT ORDER
        elif order_type == "LIMIT":

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        # STOP MARKET ORDER
        elif order_type == "STOP_MARKET":

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                stopPrice=price
            )

        else:
            raise ValueError("Unsupported order type")

        logger.info(f"Order response: {response}")

        return {
            "success": True,
            "orderId": response.get("orderId", "Pending"),
            "status": response.get("status", "Created"),
            "executedQty": response.get("executedQty", "0"),
            "avgPrice": response.get("avgPrice", "N/A")
        }

    except BinanceAPIException as e:

        logger.error(f"Binance API Error: {e}")

        return {
            "success": False,
            "error": str(e)
        }

    except Exception as e:

        logger.error(f"Unexpected Error: {e}")

        return {
            "success": False,
            "error": str(e)
        }