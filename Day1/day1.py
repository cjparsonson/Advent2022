# Day 1 Advent of Code

# Declare an empty list
data_list = []
# Open the file
with open('./inputData.txt', 'r') as file:
    raw_data = file.read()
    # Split file into blocks, a double newline is the separator
    data_blocks = raw_data.split('\n\n')
    # Loop through the blocks splitting into groups of integers
    for block in data_blocks:
        split_block = block.split('\n')
        int_block = [int(item) for item in split_block]
        data_list.append(int_block)

# Create a list of summed lists and sort
totals_list = [sum(list_block) for list_block in data_list]
sorted_totals = sorted(totals_list, reverse=True)
print(f"The highest value is: {sorted_totals[0]}")

# Get total of top three highest
top_three = sorted_totals[:3]
print(f"The sum of the top three highest values is: {sum(top_three)}")
