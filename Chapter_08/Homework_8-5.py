def describe_city(city, country='france'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('paris')
describe_city(city='mexico city', country='mexico')
describe_city(city='berlin', country='germany')