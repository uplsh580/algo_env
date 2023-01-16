class NODE:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.parent = None
        self.children = []

class GRAPH:
    def __init__(self, values, edges):
        self.node_list =[]
        for id, v in enumerate(values):
            self.node_list.append(NODE(id, v))
        
        



def solution(values, edges, queries):
    answer = []
    return answer