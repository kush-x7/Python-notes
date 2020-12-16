
def my_function():   ->definning my function
    print("Hello")
    print("Bye")
    sum=2+3
    return sum

my_function()         ->calling my function

--------------------------------------------------


def greet_with(name, location):              ->definning a function which takes input while calling
    print(f'Hello {name}')
    print(f'WHat is it like in {location}?')


greet_with("Jack Bauer", "Nowhere")           ->sendinfg proper input while calling
greet_with("Nowhere", "Jack Bauer")
print()

greet_with(name="Angela", location="London")  ->assigning new variable name with some value
greet_with(location="London", name="Angela")
