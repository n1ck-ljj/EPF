import stable_year

def main():
    print("Types of EPF calculators: ")
    print("1. Static year (no changes to your salary, contribution rates and no withdrawls done)\n2. Working on it.")
    trigger = int(input(("Please select the type of calculator you want.\n")))

    match trigger:
        case 1:
            stable_year.static_year()
        case 2:
            print("Not ready yet.")
            exit()
        case __: 
            print("Wrong number entered. Exiting...")
            exit()

if __name__ == "__main__":
    main()
