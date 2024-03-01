import csv


def load_csv(path):
    # wrapper around CSV library to return a generator for a given path
    with open(path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = []
        for row in reader:
            rows.append(row)

    return rows

def write_csv(path, rows: dict, existing=False):
    # wrapper around the CSV library for writing results. Use existing to append to files already written
    if existing:
        with open(path, 'a') as csv_file:
            for row in rows:
                writer.writerow(row)
    else:
        with open(path, 'w') as csv_file:
            writer.writeheader()
            for row in rows:
                writer.writerow(row)