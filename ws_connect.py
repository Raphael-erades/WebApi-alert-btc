from websocket import create_connection
import json

test_key = '1243D3AE-8D5F-49A2-AF4C-07EDD3D4D15F'

class CoinAPIv1_subscribe(object):
  def __init__(self, apikey):
    self.type = "hello"
    self.apikey = apikey
    self.heartbeat = True
    self.subscribe_data_type = ["trade"]
    self.subscribe_filter_symbol_id= ["COINBASE_SPOT_BTC_USD"]  #add each 

ws = create_connection("wss://ws.coinapi.io/v1/")
sub = CoinAPIv1_subscribe(test_key)
ws.send(json.dumps(sub.__dict__))
while True:
    msg =  ws.recv()
    input_dict = json.loads(msg)
    if(len(input_dict)!=1):
        print(input_dict['price'])
ws.close()