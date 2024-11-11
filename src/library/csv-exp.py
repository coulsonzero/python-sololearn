import csv


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
        writer.writerows(data)

def read_csv():
    with open('example.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if __name__ == '__main__':
    write_csv()