def get_input():
    with open("day_8/input.txt", "r") as f:
        return list(map(int, f.read().split(" ")))


def find_node_length(node):
    num_child_nodes = node[0]
    num_metadata = node[1]
    if num_child_nodes == 0:
        return 2 + num_metadata
    else:
        size = 2
        # offset = 2
        for i in range(num_child_nodes):
            size += find_node_length(node[size:])
        return size + num_metadata
        # return 2 + num_metadata + sum(find_node_length(node[offset:]))


def get_tree(node):
    num_child_nodes = node[0]
    num_metadata = node[1]
    nodes = {"children": [], "metadata": node[-1*num_metadata:]}
    offset = 2
    for i in range(num_child_nodes):
        offset_initial = offset
        offset += find_node_length(node[offset:])
        nodes["children"].append(get_tree(node[offset_initial:offset + 0]))

    return nodes


def sum_metadata(node_tree):
    return sum(node_tree["metadata"]) + sum(sum_metadata(child) for child in node_tree["children"])


def node_value(node_tree):
    if not node_tree["children"]:
        return sum(node_tree["metadata"])
    else:
        # print([node_value(node_tree["children"][i])
        #       for i in node_tree["metadata"] if i < len(node_tree["children"])])
        return sum(node_value(node_tree["children"][i-1]) for i in node_tree["metadata"] if i <= len(node_tree["children"]))


def part_one(node):
    node_tree = get_tree(node)

    return sum_metadata(node_tree)


def part_two(node):
    node_tree = get_tree(node)

    return node_value(node_tree)


print(part_one(get_input()))
print(part_two(get_input()))
