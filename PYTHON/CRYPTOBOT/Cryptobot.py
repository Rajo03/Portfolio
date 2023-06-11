import ccxt

# Konfiguracja API Binance
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
})

# Funkcja kupowania
def buy(symbol, amount):
    order = exchange.create_market_buy_order(symbol, amount)
    print('Kupiono:', order)

# Funkcja sprzedaży
def sell(symbol, amount):
    order = exchange.create_market_sell_order(symbol, amount)
    print('Sprzedano:', order)

# Główna pętla programu
def main():
    symbol = 'USDT/USD'
    target_price = 1.0
    amount = 10

    while True:
        # Pobierz bieżącą cenę
        ticker = exchange.fetch_ticker(symbol)
        current_price = ticker['close']

        # Sprawdź warunki handlowe
        if current_price < target_price:
            buy(symbol, amount)
        elif current_price > target_price:
            sell(symbol, amount)

        # Poczekaj określony czas przed kolejną iteracją
        time.sleep(60)

if __name__ == '__main__':
    main()