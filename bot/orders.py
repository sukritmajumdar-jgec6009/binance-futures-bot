import logging

def place_futures_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': quantity
        }
        
        if order_type.upper() == 'LIMIT':
            params['price'] = str(price)
            params['timeInForce'] = 'GTC'

        response = client.futures_create_order(**params)
        logging.info(f"Order Success: {response['orderId']}")
        return response

    except Exception as e:
        logging.error(f"API Error: {str(e)}")
        return {"error": str(e)}