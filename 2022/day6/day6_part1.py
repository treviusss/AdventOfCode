with open("day6_input", "r") as f:
    datastream = f.read()
    for index in range(len(datastream) - 4):
        chunk = set(datastream[index : index + 4])
        if len(chunk) == 4:
            print(index + 4, datastream[index : index + 4])
            break
