import pybithumb
import time

con_key = "81dd5f25e5daa70b2fff603901d2c09c"
sec_key = "82333efegeg9eg3e77c573weg34af17a"

bithumb = pybithumb.Bithumb(con_key, sec_key)

order = bithumb.buy_limit_order("BTC", 3000000, 0.001 )
print(order)

time.sleep(10)
cancel = bithumb.cancel_order(order)
print(cancel)
