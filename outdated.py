def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()
            if "," in date:
                parts = date.split(" ")
                month_name = parts[0]
                day = int(parts[1].replace(",", ""))
                year = int(parts[2])
                if month_name in months:
                    month_num = months.index(month_name) + 1
                    print(f"{year:04d}-{month_num:02d}-{day:02d}")
                    break
            else:
                parts = date.split("/")
                if len(parts) == 3:
                    month = int(parts[0])
                    day = int(parts[1])
                    year = int(parts[2])
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
        except ValueError:
            continue

if __name__ == "__main__":
    main()




