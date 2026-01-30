# Match case
country = "France"

match country:
    case "India":
        print("IN")
    case "USA":
        print("US")
    case "Germany":
        print("DE")
    case "Australia":
        print("AU")
    case _:
        print("Unknown Country")