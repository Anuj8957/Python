from http.client import responses

from dhanhq import dhanhq

dhan = dhanhq("","")

# response = dhan.get_fund_limits()

# response = dhan.place_order(security_id='1333',   #hdfcbank
#     exchange_segment=dhan.NSE,
#     transaction_type=dhan.BUY,
#     quantity=10,
#     order_type=dhan.MARKET,
#     product_type=dhan.INTRA,
#     price=0)
#
response = dhan.get_trade_history("2024-08-01", "2024-08-30")

print(response)