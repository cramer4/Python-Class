jimmy = {
    "first_name": "jimmy",
    "last_name": "johnson",
    "age": 14,
    "city": "austin"
}


print(f"My friend's name is {jimmy.get('first_name').title()}.")
print(f"His last name is {jimmy.get('last_name').title()}.")
print(f"He is {jimmy.get('age')} years old.")
print(f"The city he lives in is {jimmy.get('city').title()}.")