from fastapi import FastAPI
import datetime as dt
from typing import Optional
from pydantic import BaseModel, Field
from typing import Union

app = FastAPI()

mock_database = {
    'Trade': [
        {
                'asset_class': "Bond",
                'counterparty': 'xyz',
                'instrument_id': 'TSLA',
                'instrument_name': 'abc',
                'trade_date_time': '2020-07-15 14:30:26.159446',
                'trade_details': {
                    'buySellIndicator': 'SELL',
                    'price': 400.0,
                    'quantity': 30,
                },
                'trade_id': 1,
                'trader': 'sakshi'
        },
        {
            'asset_class': "Equity",
            'counterparty': 'xyz',
            'instrument_id': 'AAPL',
            'instrument_name': 'abc',
            'trade_date_time': '2020-07-15 14:30:26.159446',
            'trade_details': {
                'buySellIndicator': 'BUY',
                'price': 400.0,
                'quantity': 30,
            },
            'trade_id': 2,
            'trader': 'bob smith'
        }
    ]
}

class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")
    price: float = Field(description="The price of the Trade.")
    quantity: int = Field(description="The amount of units traded.")


class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")
    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")
    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")
    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")
    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")
    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")
    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")
    trader: str = Field(description="The name of the Trader")

@app.get("/")
def list_trades(search: Union[str, None] = None):
   if 'Trade' in mock_database:
    trades = mock_database['Trade']
    return_list = []
    for trade in trades:
        if 'counterparty' in trade and trade['counterparty'] == search:
            return_list.append(trade)
            continue
        if 'instrument_id' in trade and trade['instrument_id'] == search:
            return_list.append(trade)
            continue
        if 'instrument_name' in trade and trade['instrument_name'] == search:
            return_list.append(trade)
            continue
        if 'trader' in trade and trade['trader'] == search:
            return_list.append(trade)
            continue
    if len(return_list)>0:
        return return_list
    else:
        return [trades]
   return {'Response': 'No Data'}


@app.get("/{trade_id}/")
def single_trade(trade_id: str):
    if 'Trade' in mock_database:
        trades = mock_database['Trade']
        for trade in trades:
            if trade_id == trade['trade_id']:
                return trade
    return {'Response': 'No Data'}

