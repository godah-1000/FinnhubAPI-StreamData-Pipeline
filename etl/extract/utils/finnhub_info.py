import finnhub

def validate_ticker(finnhub_client, ticker):
    symbol_lookup = finnhub_client.symbol_lookup(ticker)
    if symbol_lookup['count'] > 0:
        for items in symbol_lookup['result']:
            if items['symbol'] == ticker:
                return True
    return False

def load_client(token):
    return finnhub.Client(api_key=token)
