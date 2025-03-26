import csv

path = "test_data"
delimiter = ","
header = True
ignore = True

def main():
    temp = []
    final = []
    with open(f"{path}/test.csv") as f:
        if header:
            data = csv.DictReader(f)
        else:
            a = csv.reader(f)
            columns_cnt = len(next(a))
            data = csv.DictReader(f, list(range(columns_cnt)))

        for row in data:
            empty = True
            t = {}
            for key, value in row.items():
                try:
                    v = value.strip()
                except AttributeError as ae:
                    if ignore:
                        empty = True
                        break
                    else:
                        raise AttributeError("Invalid row found, correct or set ignore = True")
                t[key] = value.strip()
                if v != "":
                    empty = False
            if not empty:
                final.append(t)

    for i in final:
        print(i)



if __name__ == "__main__":
    main()