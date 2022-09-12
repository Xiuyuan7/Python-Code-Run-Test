from datetime import datetime


class Solution:
    def __init__(self):
        self.broker_trades = {}
        self.electronic_trades = {}

    """
    @param: raw_tade:['trade_id', 'trade_date', 'time_of_trade', 'portfolio', 'exchange', 'product',
    'product_type', 'expiry_dt', 'qty', 'strike_price', 'side']
    """
    def process_raw_trade(self, raw_trade):
        trade_id = raw_trade[0]
        trade_date = raw_trade[1]
        time_of_trade = raw_trade[2]
        portfolio = raw_trade[3]
        exchange = raw_trade[4]
        product = raw_trade[5]
        product_type = raw_trade[6]
        expiry_dt = raw_trade[7]
        qty = int(raw_trade[8])
        strike_price = raw_trade[9]

        if exchange == 'CBOE':
            side = 'BUY' if qty > 0 else 'SELL'
        else:
            side = raw_trade[10]

        time_stamp = self.get_timestamp(trade_date, time_of_trade)

        attributes = (product, product_type, side, expiry_dt, strike_price)

        if portfolio == 'Broker':
            if attributes not in self.broker_trades:
                self.broker_trades[attributes] = {}
            if time_stamp not in self.broker_trades[attributes]:
                self.broker_trades[attributes][time_stamp] = set()
            self.broker_trades[attributes][time_stamp].add(trade_id)
        else:
            if attributes not in self.electronic_trades:
                self.electronic_trades[attributes] = {}
            if time_stamp not in self.electronic_trades[attributes]:
                self.electronic_trades[attributes][time_stamp] = set()
            self.electronic_trades[attributes][time_stamp].add(trade_id)

    """
    @params: trade_date:str, time_of_trade:str
    @return: int
    """
    def get_timestamp(self, trade_date, time_of_trade):
        te = trade_date + ' ' + time_of_trade
        ft = '%Y-%m-%d %H:%M:%S'
        dt = datetime.strptime(te, ft)
        return int(dt.timestamp())

    """
    @return: List[Tuple(str, str)]
    """
    def run(self):
        result = []

        for attributes in self.electronic_trades:
            if attributes not in self.broker_trades:
                continue
            for electronic_time in self.electronic_trades[attributes]:
                for broker_time in range(electronic_time, electronic_time + 61):
                    if broker_time not in self.broker_trades[attributes]:
                        continue
                    self.get_front_running_trades(attributes, electronic_time, broker_time, result)

        result.sort()

        return [(broker_id, electronic_id) for _, broker_id, electronic_id in result]

    """
    @params: attributes:Tuple(str, str, str, str, str), electronic_time:int, broker_time:int, 
    result:List[Tuple(int, str, str)]
    """
    def get_front_running_trades(self, attributes, electronic_time, broker_time, result):
        for broker_id in self.broker_trades[attributes][broker_time]:
            for electronic_id in self.electronic_trades[attributes][electronic_time]:
                result.append((electronic_time, broker_id, electronic_id))
