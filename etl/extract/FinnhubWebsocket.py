import json
import ssl
import websocket
import os

from utils.finnhub_info import load_client, validate_ticker

class FinnhubWebsocket:
    def __init__(self):
        self.token = os.environ["api_key"]
        self.ticker = os.environ["ticker"]
        self.finnhub_client = load_client(self.token)

        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={self.token}",
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


    def on_message(self, ws, message):
        message = json.loads(message)
        print(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, *ws):
        print("### closed ###")

    def on_open(self, ws):
        if validate_ticker(self.finnhub_client, self.ticker):
            self.ws.send(f'{{"type": "subscribe", "symbol": "{self.ticker}"}}')
            print(f'Subscription for {self.ticker} succeeded')
        else:
            print(f'Subscription for {self.ticker} failed - ticker not found')

if __name__ == '__main__':
    FinnhubWebsocket()