
def get_budgets(lst):
	sum = 0
	for element in lst:
		value = element.get("budget")
		sum = sum+value
	return sum

def get_budgets(lst):
	return sum(i['budget'] for i in lst)




print(get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }]))
