def read_file(file_path):
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            row_data = [float(col) if '.' in col else int(col) for col in columns]

            data.append(row_data)

    return data

if __name__ == "__main__":
    file_inp = "input_file.txt"

    data = read_file(file_inp)

    temp1_data= []

    for row in data:
        # print(row)
        for col in row:
            # print(col)
            if col == 11:
                ll =[]
                for i in range(10):
                    ll.append(row[col+i])
                temp1_data.append(ll)
    
    print(temp1_data)

