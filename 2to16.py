user_input = [[1,1,1,0,0,1], [1,0,0,0,0,1], [1,1,1,1,1,1], [0,0,0,0,0,0]]
output = []

for row in user_input:
    row_output = []
    for i, element in enumerate(row):
        if i == 0:
            previous_element = element
            element_count = 0
        else:
            previous_element = row[i-1]

        if previous_element == element:
            element_count += 1

        elif previous_element != element or i == (len(row)-1):
            row_output.append(f"{element_count} {previous_element}")
            element_count = 1

        if i == (len(row)-1):
            row_output.append(f"{element_count} {element}")

    output.append(row_output)

print(output)

print(int(True))