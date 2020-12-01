def make_sandwich(*items):
    print("\nMaking a sandwich with:")
    for item in items:
        print(f"  {item}")

make_sandwich("bacon", "lettuce", "tomato", "mayonnaise")
make_sandwich("ham", "swiss cheese")
make_sandwich("turkey", "ham", "cheddar cheese", "bacon","mayonnaise")