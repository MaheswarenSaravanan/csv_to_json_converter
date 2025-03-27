import csv
from core.table import Table

path = "test_data"
delimiter = ","
header = True
ignore = True

def main():
    temp = []
    final = []
    tb = Table()
    with open(f"{path}/test.csv") as f:
        if header:
            data = csv.DictReader(f)
        else:
            a = csv.reader(f)
            columns_cnt = len(next(a))
            data = csv.DictReader(f, list(range(columns_cnt)))
        
        for row in data:
            tb.add_row(row, infer_column=False)

        # for row in data:
        #     empty = True
        #     t = {}
        #     for key, value in row.items():
        #         try:
        #             v = value.strip()
        #         except AttributeError as ae:
        #             if ignore:
        #                 empty = True
        #                 break
        #             else:
        #                 raise AttributeError("Invalid row found, correct or set ignore = True")
        #         t[key] = value.strip()
        #         if v != "":
        #             empty = False
        #     if not empty:
        #         final.append(t)

    # for i in final:
    #     tb.add_row(i, infer_column=True)

    tb.test()


if __name__ == "__main__":
    main()
    # tb = Table()
    # column_details = [
    #     {
    #         "name": "id"
    #     },
    #     {
    #         "name": "name"
    #     },
    #     {
    #         "name": "address"
    #     }
    # ]

    # data = [{'id': '14', 'name': 'Alice Johnson', 'age': '32', 'email': 'alice.johnson@example.com', 'salary': '90000', 'department': 'Legal', 'joining_date': '2018-07-10', 'remarks': 'Special \\case\\" with a comma"'}]

    # # tb.set_columns(column_details)
    # tb.add_row(data[0], infer_column=True)
    # tb.test()