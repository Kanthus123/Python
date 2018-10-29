#Strategy pattern allows you to switch the algorithm or strategy based upon the situation.

#Consider the example of sorting, we implemented bubble sort but the data started to grow and bubble sort started getting very slow.
#In order to tackle this we implemented Quick sort. But now although the quick sort algorithm was doing better for large datasets,
#it was very slow for smaller datasets. In order to handle this we implemented a strategy where for small datasets,
#bubble sort will be used and for larger, quick sort.


from order import Order
from calculate_shipping import CalculateShipping
from shippings import Default, Express

calculate_shipping = CalculateShipping()

order = Order(500)

calculate_shipping.execute_calculation(order, Default())
calculate_shipping.execute_calculation(order, Express())
