Calculate Discount
This module provides a function to calculate the final price after applying a discount to an original price.

Installation
No installation is required, as this is a pure Python module.

Usage
To use the calculate_discount function, simply call it with the original price and the discount percentage as arguments:


import calculate_discount

final_price = calculate_discount.calculate_discount(100, 20)
print(final_price)
The calculate_discount function takes two arguments:

price: The original price of an item.
discount_percent: The discount percentage as a float between 0 and 100.
If the discount percentage is 20% or higher, the function applies the discount and returns the final price. Otherwise, the function returns the original price.

The calculate_discount function returns the final price as a float.

Example
Here's an example usage of the calculate_discount function:


import calculate_discount

final_price = calculate_discount.calculate_discount(100, 20)
print(final_price)
This will print 80.0, which is the final price after applying a 20% discount to an original price of 100.

Testing
To run the tests for this module, execute the following command in the terminal:


python -m unittest discover
This will run all the tests in the test_calculate_discount.py file.



License
This module is licensed under the MIT License.
