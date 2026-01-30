# Match case
country = "USA"

match country:
    case "India":
        print("IN")
    case "USA" | "United States":
        print("US")
    case "Germany":
        print("DE")
    case "Australia":
        print("AU")
    case _:
        print("Unknown Country")