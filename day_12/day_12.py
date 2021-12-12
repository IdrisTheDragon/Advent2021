



def load_nodes(file):
    nodes = dict()

    for l in file:
        s = l[:-1].split("-")

        if s[0] in nodes:
            nodes[s[0]].append(s[1])
        else:
            nodes[s[0]] = [s[1]]
        if s[1] in nodes:
            nodes[s[1]].append(s[0])
        else:
            nodes[s[1]] = [s[0]]
    return nodes

def isCaps(text):
    return text != text.lower()    

def process_node(nodes,curNode,prevNodes):
    paths = []
    prevNodes.append(curNode)
    for n in nodes[curNode]:
        if n == "end":
            paths.append(["end"])
        elif n == "start":
            pass
        elif isCaps(n):
            paths = paths + process_node(nodes,n,prevNodes.copy())
        else:
            if n in prevNodes:
                pass
            else:
                paths = paths + process_node(nodes,n,prevNodes.copy())
    temp = []
    for p in paths:
        temp.append([curNode]+p)
    return temp


def process_node_2(nodes,curNode,prevNodes,little):
    paths = []
    prevNodes.append(curNode)
    for n in nodes[curNode]:
        if n == "end":
            paths.append(["end"])
        elif n == "start":
            pass
        elif isCaps(n):
            paths = paths + process_node_2(nodes,n,prevNodes.copy(),little)
        else:
            if n in prevNodes:
                if little == None:
                    paths = paths + process_node_2(nodes,n,prevNodes.copy(),n)
            else:
                paths = paths + process_node_2(nodes,n,prevNodes.copy(),little)
    temp = []
    for p in paths:
        temp.append([curNode]+p)
    return temp



file = open("input.txt","r")
nodes = load_nodes(file)
#print(nodes)
paths = process_node_2(nodes,"start",[],None)
print(paths)
print(len(paths))

