from utils.finnhub_info import load_client, validate_ticker
import websocket

from src.utils import parse_config
token = parse_config.get('/Users/gosakrupa/PycharmProjects/PythonProject/config/config.yaml')["api-key"]

class FinnhubWebsocket:
    def __init__(self, ticker):
        self.ticker = ticker
        self.finnhub_client = load_client(token)
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={token}",
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()

    def on_message(self, ws, message):
        print(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, *ws):
        print("### closed ###")

    def on_open(self, ws):
        if validate_ticker(self.finnhub_client, self.ticker):
            send_dict = {"type": "subscribe", "symbol": f"{self.ticker}"}
            ws.send('{"type":"subscribe","symbol":f"{ticker}"}')