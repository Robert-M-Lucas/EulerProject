tri_str = open("triangle.txt", "r").read()

tri = []
for line in tri_str.split("\n"):
    line_list = []
    for num in line.split(" "):
        line_list.append(int(num))
    tri.append(line_list)
height = len(tri)

tri_vals = []

"""
def traverse(layer, index, path_val):
    path_val += tri[layer][index]
    if not (tri_vals[layer][index] is None) or path_val <= tri_vals[layer][index]:
        return
    tri_vals[layer][index] = path_val

    for i in range(2):
        traverse(layer + 1, index + i)
"""

tri_vals.append(tri[0])
for i in range(1, len(tri)):
    # print("---------------")
    # print(tri_vals[i - 1])
    # print(tri[i])
    # print("*")
    new_line = []
    for j in range(len(tri[i])):
        best = -1

        if j < len(tri[i]) - 1:
            best = tri[i][j] + tri_vals[i - 1][j]

        if j > 0 and best < tri[i][j] + tri_vals[i - 1][j - 1]:
            best = tri[i][j] + tri_vals[i - 1][j - 1]

        new_line.append(best)
    tri_vals.append(new_line)
    # print(tri_vals[i])

print(max(tri_vals[-1]))
