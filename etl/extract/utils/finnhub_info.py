import finnhub
from src.utils import parse_config

api_key = parse_config.get('/Users/gosakrupa/PycharmProjects/PythonProject/config/config.yaml')["api-key"]
finnhub_client = finnhub.Client(api_key=api_key)

print(finnhub_client.symbol_lookup('BINANCE1:BTCUSDT'))