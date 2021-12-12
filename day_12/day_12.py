



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

def process_node(nodes,curNode="start",prevNodes=[],p2=False,little=None):
    paths = []
    prevNodes.append(curNode)
    for n in nodes[curNode]:
        if n == "end":
            paths.append(["end"])
        elif n == "start":
            pass
        elif isCaps(n):
            paths = paths + process_node(nodes,n,prevNodes.copy(),p2,little)
        else:
            if n in prevNodes:
                if p2 and little == None:
                    paths = paths + process_node(nodes,n,prevNodes.copy(),p2,n)
            else:
                paths = paths + process_node(nodes,n,prevNodes.copy(),p2,little)
    temp = []
    for p in paths:
        temp.append([curNode]+p)
    return temp



file = open("input.txt","r")
nodes = load_nodes(file)
# print(nodes)
paths = process_node(nodes)
# print(paths)
print(len(paths))

paths = process_node(nodes,p2=True)
# print(paths)
print(len(paths))

