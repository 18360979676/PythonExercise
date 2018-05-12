#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yezhu2'


from bitmex_websocket import BitMEXWebsocket
ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD", api_key=None, api_secret=None)
ws.get_instrument()
ws.get_ticker()
ws.funds()
ws.market_depth()
ws.open_orders()
ws.recent_trades()
