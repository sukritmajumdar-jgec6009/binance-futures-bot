def validate_inputs(symbol, side, order_type, quantity, price):
    if side.upper() not in ['BUY', 'SELL']:
        raise ValueError("Side must be BUY or SELL")
    if order_type.upper() not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be MARKET or LIMIT")
    if order_type.upper() == 'LIMIT' and not price:
        raise ValueError("Price is required for LIMIT orders")
    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than zero")