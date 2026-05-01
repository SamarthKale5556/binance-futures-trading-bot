import typer
from rich.console import Console
from rich.table import Table

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_symbol
)

from bot.orders import place_order

app = typer.Typer()
console = Console()

# Startup Banner
console.print("[bold cyan]Binance Futures Trading Bot[/bold cyan]")
console.print("[yellow]Primetrade.ai Assignment Project[/yellow]\n")


@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):

    try:

        # Validate Inputs
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        # Request Summary Table
        request_table = Table(title="Order Request Summary")

        request_table.add_column("Field", style="cyan", justify="center")
        request_table.add_column("Value", style="green", justify="center")

        request_table.add_row("Symbol", symbol)
        request_table.add_row("Side", side)
        request_table.add_row("Order Type", order_type)
        request_table.add_row("Quantity", str(quantity))
        request_table.add_row("Price", str(price) if price else "N/A")

        console.print(request_table)

        # Place Order
        result = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        # Success Response
        if result["success"]:

            response_table = Table(title="Order Response")

            response_table.add_column("Field", style="cyan", justify="center")
            response_table.add_column("Value", style="green", justify="center")

            response_table.add_row("Order ID", str(result["orderId"]))
            response_table.add_row("Status", str(result["status"]))
            response_table.add_row("Executed Quantity", str(result["executedQty"]))
            response_table.add_row("Average Price", str(result["avgPrice"]))

            console.print(response_table)

            console.print(
                "\n[bold green]SUCCESS: Order placed successfully![/bold green]"
            )

        else:
            console.print(
                f"\n[bold red]API ERROR:[/bold red] {result['error']}"
            )

    except Exception as e:
        console.print(
            f"\n[bold red]VALIDATION ERROR:[/bold red] {e}"
        )


if __name__ == "__main__":
    app()