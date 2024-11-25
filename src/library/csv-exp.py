import csv
import pandas

def write_csv():
    # 数据
    data = [
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles']
    ]

    # 写入 CSV 文件
    with open('example.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'City'])
        writer.writerow(['John', '21', 'Shang Hai'])
        writer.writerows(data)

def read_csv():
    with open('example.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def pandas_csv():
    data = pandas.read_csv("example.csv")
    print(data)

if __name__ == '__main__':
    # pandas_csv()
    # write_csv()
    read_csv()