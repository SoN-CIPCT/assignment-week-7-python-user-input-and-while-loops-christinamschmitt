# # Week 7 Python User input and while loops
# # Make a list of pizza orders and populate it.

pizza_orders = ['cheese', 'pepperoni', 'olive', 'pineapple', 'sausage']

# # Make an empty list called finished pizzas.
finished_pizzas = []

# # Loop through the list of orders, saying your pizza pie is finished.
# # After the pizza is made, move the pizza to finished pizzas
while pizza_orders:
    completed = pizza_orders.pop()
    finished_pizzas.append(completed)
    print(f"Your {completed} pizza pie is finished!")      

print("All of the pizzas have been made.")
for finished_pizza in finished_pizzas:
    print(f"The {finished_pizza} pizza was made.")