def main():
    country_capitals = {}
    print("Welcome! Type 'exit' to quit the program.")
    while True:
        country = input("Enter a country: ").strip()
        if country.lower() == "exit":
            print("Goodbye!")
            break
        country_key = country.title()
        if country_key in country_capitals:
            print(f"The capital of {country_key} is {country_capitals[country_key]}.")
        else:
            capital = input(f"I don't know the capital of {country_key}. Please enter it: ").strip()
            country_capitals[country_key] = capital.title()
            print(f"Got it! {country_key}'s capital is {capital.title()}.")
if __name__ == "__main__":
    main()
