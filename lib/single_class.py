"""
when an order is created with an address
the address is reflected in the address attribute
order = Order("123 Fake Street")
assert order.address == "123 Fake address"

"""

"""
when we added two valid item to the order
and we format the order note
it returns a string with the addres and the items

order = Order("123 Fake Street")
order.add_item("Chair")
order.add_item("Moisturiser")
assert order.format_note() == "Order for 123 Fake Street: Chair, Moisturiser"

"""