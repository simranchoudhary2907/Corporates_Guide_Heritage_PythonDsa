color = input("Enter light color: ").lower()
speed = int(input("Enter speed: "))

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green" if speed > 60:
        print("Slow down even on green")
    case "green":
        print("Go")
    case _:
        print("Invalid Color")