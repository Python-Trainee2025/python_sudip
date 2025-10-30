import csv

def read_csv_file(filename):
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")


read_csv_file("data.csv")