from order import Order
from calculate_shipping import CalculateShipping
from shippings import Default, Express

calculate_shipping = CalculateShipping()

order = Order(500)

calculate_shipping.execute_calculation(order, Default())
calculate_shipping.execute_calculation(order, Express())
