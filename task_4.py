from pprint import pprint

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"


def csv_to_list_dict(filename, delimeter=",", new_line="\n") -> list[dict]:
    with open(filename, "r") as file:
        header = file.readline() # read first row
        headers = header.replace(new_line, "").split(delimeter)
        
        for line in file:
            object_values = line.replace(new_line, "").split(delimeter)
            yield dict(zip(headers, object_values))


def dict_printer(line):
    pprint([record for record in line])


dict_printer(csv_to_list_dict(INPUT_FILE))
