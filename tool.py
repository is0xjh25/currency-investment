import csv


def import_csv(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        row_index = 0
        for row in reader:
            if row:  # avoid blank lines
                row_index += 1
                columns = [row[0], row[1], row[2], row[3], row[4], row[5]]
                data.append(columns)
    return data


def currency_change(file_path):
    data = import_csv(file_path)
    # Only check offer(spot), bid(spot)
    for i in range(4, 6):
        print("old:" + data[-2][i] + "\n" + "new:" + data[-1][i] + "\n")
        if data[-2][i] != data[-1][i]:
            print("!!!")
            return True
    return False
