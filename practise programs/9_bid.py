import art

print(art.logo)
print("Welcome to the secret auction program")

from replit import clear
#HINT: You can call clear() to clear the output in the console.



repeat ="yes"
customer_dict={}

while repeat =="yes":
  name_key =input("What is your name?: ")
  money_value =int(input("What's your bid?:"))

  customer_dict[name_key]= money_value

  repeat =input("Are there any other biddere?: 'yes' or 'no'").lower()
  clear()

maximum= 0
for key in customer_dict:
  amount=customer_dict[key]
  if amount > maximum:
    maximum = amount
    new_key=key

print(f"The winner is {new_key} with a bid of Rs{amount}")
