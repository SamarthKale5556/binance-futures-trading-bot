VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT", "STOP_MARKET"]


def validate_side(side):
    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type):
    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")

    return order_type


def validate_quantity(quantity):
    quantity = float(quantity)

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity


def validate_price(price, order_type):
    if order_type.upper() == "LIMIT":

        if price is None:
            raise ValueError("Price is required for LIMIT orders")

        price = float(price)

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        return price

    return price


def validate_symbol(symbol):
    symbol = symbol.upper()

    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT")

    return symbol