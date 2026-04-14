import argparse
from bot.client import get_client
from bot.orders import place_futures_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Binance Futures Bot CLI")
    
    parser.add_argument('--symbol', required=True)
    parser.add_argument('--side', required=True)
    parser.add_argument('--type', required=True)
    parser.add_argument('--quantity', required=True, type=float)
    parser.add_argument('--price', type=float)

    args = parser.parse_args()

    try:
        # 1. Validate user inputs [cite: 20]
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)
        
        # 2. Print order request summary 
        print("\n--- ORDER REQUEST SUMMARY ---")
        print(f"Symbol:   {args.symbol.upper()}")
        print(f"Side:     {args.side.upper()}")
        print(f"Type:     {args.type.upper()}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price:    {args.price}")
        print("-----------------------------\n")

        # 3. Initialize client and place order
        client = get_client()
        result = place_futures_order(client, args.symbol, args.side, args.type, args.quantity, args.price)
        
        # 4. Handle response output 
        if "error" in result:
            print(f"❌ FAILURE: {result['error']}")
        else:
            print(f"✅ SUCCESS: Order successfully placed on Testnet.")
            print(f"Order ID:     {result.get('orderId')}")
            print(f"Status:       {result.get('status')}")
            print(f"Executed Qty: {result.get('executedQty')}")
            # Note: avgPrice is included if available in the Binance response
            print(f"Avg Price:    {result.get('avgPrice', 'N/A')}")

    except Exception as e:
        print(f"❌ Input Error: {e}")

if __name__ == "__main__":
    main()