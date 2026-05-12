import requests


def text_analyzer():
    print("\nTEXT ANALYZER")

    sentence = input("Enter a sentence: ").strip()

    if sentence == "":
        print("Input cannot be empty!")
        return

    total_characters = len(sentence)

    words = sentence.split()
    total_words = len(words)

    cleaned = sentence.replace(" ", "").lower()

    if cleaned == cleaned[::-1]:
        palindrome = "Yes, it is a palindrome."
    else:
        palindrome = "No, it is not a palindrome."

    print("\nRESULTS")
    print("Total Characters:", total_characters)
    print("Total Words:", total_words)
    print("Palindrome Check:", palindrome)


def sorting_tool():
    print("\nSORTING TOOL")

    numbers_input = input("Enter numbers separated by commas: ").strip()

    if numbers_input == "":
        print("Input cannot be empty!")
        return

    try:
        numbers = [float(num) for num in numbers_input.split(",")]

    except ValueError:
        print("Invalid number format!")
        return

    ascending = sorted(numbers)

    descending = sorted(numbers, reverse=True)

    print("\nSORTING RESULTS")
    print("Ascending Order :", ascending)
    print("Descending Order:", descending)

    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:

        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    print("\nALGORITHM RESULTS")
    print("Largest Number :", largest)
    print("Smallest Number:", smallest)


def live_data_viewer():
    print("\nLIVE DATA VIEWER")

    city = input("Enter city name: ").strip()

    if city == "":
        print("City name cannot be empty!")
        return

    try:
        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        data = response.json()

        current_temp = data["current_condition"][0]["temp_C"]

        print(f"\nCurrent temperature in {city}: {current_temp}°C")

    except:
        print("Could not fetch live data. Please try again.")


def main():

    print("Welcome to Smart Text Analyzer & Live Data App")

    while True:

        print("\nMENU")
        print("1. Text Analyzer")
        print("2. Sorting Tool")
        print("3. Live Data Viewer")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            text_analyzer()

        elif choice == "2":
            sorting_tool()

        elif choice == "3":
            live_data_viewer()

        elif choice == "4":
            print("\nThank you for using the app!")
            break

        else:
            print("Invalid choice! Please select 1-4.")


main()
