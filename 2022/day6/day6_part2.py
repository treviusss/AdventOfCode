with open("day6_input", "r") as f:
    datastream = f.read()
    for index in range(len(datastream) - 14):
        chunk = set(datastream[index : index + 14])
        if len(chunk) == 14:
            print(index + 14, datastream[index : index + 14])
            break
