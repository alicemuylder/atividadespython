import sys
import ccxt

def get_bitcoin_price(n):
    exchange = ccxt.binance()  
    symbol = "BTC/USDT"
    ticker = exchange.fetch_ticker(symbol)
    bitcoin_price = ticker["last"]
    cost_in_usd = n * bitcoin_price
    return cost_in_usd

def main():
    if len(sys.argv) != 2:
        print("Uso: python bitcoin_alt.py <quantidade de Bitcoins>")
        sys.exit(1)

    try:
        n = float(sys.argv[1])
    except ValueError:
        print("A quantidade de Bitcoins deve ser um número válido.")
        sys.exit(1)

    cost_in_usd = get_bitcoin_price(n)
    print(f"Custo de {n} Bitcoins: ${cost_in_usd:.4f}")

if __name__ == "__main__":
    main()