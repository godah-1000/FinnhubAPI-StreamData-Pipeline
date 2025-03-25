import websocket
from src.utils import parse_config
from utils.finnhub_info import load_client, validate_ticker
import ssl

class FinnhubWebsocket:
    def __init__(self):
        config = parse_config.get('/Users/gosakrupa/PycharmProjects/PythonProject/config/config.yaml')

        self.token = config["api-key"]
        self.ticker = config["ticker"]
        self.finnhub_client = load_client(self.token)

        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={self.token}",
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


    def on_message(self, ws, message):
        print(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, *ws):
        print("### closed ###")

    def on_open(self, ws):
        if validate_ticker(self.finnhub_client, self.ticker):
            self.ws.send(f'{{"type": "subscribe", "symbol": "{self.ticker}"}}')

if __name__ == '__main__':
    FinnhubWebsocket()