import json
OUTPUT_FILE = "output.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, 'r', encoding='utf8') as f:
        data_str = ''
        for line in f:
            data_str += line

        data_list = list(filter(None, data_str.split('\n')))
        header_str = data_list[:1]
        for line in header_str:
            header_list = line.split(',')

        rows_str = data_list[1:]
        full_rows_list = []
        for line in rows_str:
            tmp_rows_list = line.split(',')
            full_rows_list += tmp_rows_list

        tmp_dict = {}
        new_list = []
        while full_rows_list:
            for i, value in enumerate(header_list):
                tmp_dict[value] = full_rows_list[i]
            new_list.append(tmp_dict.copy())
            tmp_dict.clear()
            full_rows_list = full_rows_list[i+1:]

        return new_list


print(json.dumps(csv_to_list_dict(OUTPUT_FILE), indent=4))