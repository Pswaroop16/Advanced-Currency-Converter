
#!/usr/bin/env python3

import requests
import sys

CURRENCIES_URL = "https://api.frankfurter.app/currencies"
CONVERT_URL = "https://api.frankfurter.app/latest"


def get_supported_currencies():
    """
    Fetch supported currency codes from API
    """
    try:
        response = requests.get(CURRENCIES_URL, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print("\nError fetching supported currencies.")
        print(e)
        return None


def show_currency_codes():
    """
    Display all available currencies
    """
    currencies = get_supported_currencies()

    if not currencies:
        return

    print("\n========== AVAILABLE CURRENCIES ==========\n")

    for code, name in sorted(currencies.items()):
        print(f"{code:<5} - {name}")

    print(f"\nTotal currencies available: {len(currencies)}")
    print("==========================================")


def convert_currency(amount, from_currency, to_currency):
    """
    Convert one currency to another
    """

    try:
        params = {
            "amount": amount,
            "from": from_currency,
            "to": to_currency
        }

        response = requests.get(
            CONVERT_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if "rates" not in data:
            print("\nConversion failed.")
            return

        converted_amount = data["rates"].get(to_currency)

        if converted_amount is None:
            print("\nCurrency conversion unavailable.")
            return

        print("\n========== CONVERSION RESULT ==========")
        print(f"{amount:.2f} {from_currency}")
        print("↓")
        print(f"{converted_amount:.2f} {to_currency}")
        print("=======================================")

    except requests.exceptions.ConnectionError:
        print("\nNo internet connection.")

    except requests.exceptions.Timeout:
        print("\nRequest timed out.")

    except requests.exceptions.RequestException as e:
        print("\nAPI Error:")
        print(e)

    except Exception as e:
        print("\nUnexpected Error:")
        print(e)


def main():

    print("\nFetching supported currencies...")
    currencies = get_supported_currencies()

    if not currencies:
        print("Unable to start application.")
        sys.exit(1)

    while True:

        print("\n====================================")
        print("      ADVANCED CURRENCY CONVERTER")
        print("====================================")
        print("1. Convert Currency")
        print("2. Show Available Currency Codes")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            try:

                amount = float(
                    input("\nEnter amount: ").strip()
                )

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                from_currency = input(
                    "From Currency Code: "
                ).upper().strip()

                to_currency = input(
                    "To Currency Code: "
                ).upper().strip()

                if from_currency not in currencies:
                    print(
                        f"Invalid source currency: {from_currency}"
                    )
                    continue

                if to_currency not in currencies:
                    print(
                        f"Invalid target currency: {to_currency}"
                    )
                    continue

                convert_currency(
                    amount,
                    from_currency,
                    to_currency
                )

            except ValueError:
                print("Please enter a valid numeric amount.")

        elif choice == "2":
            show_currency_codes()

        elif choice == "3":
            print("\nThank you for using Currency Converter.")
            sys.exit(0)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
