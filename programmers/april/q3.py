from sys import maxsize as INT_MAX
import bisect 

def get_min_pos(list):
    min_v = min(list)
    return list.index(min_v)

def min_dist_index(list):
    ret = []
    for i, e in enumerate(list):
        ret.append((e,i))
    return sorted(ret)

def min_dist_pos(list):
    min_v = INT_MAX
    for e in list:
        if e > 0:
            min_v = min(min_v, e)
    if min_v == INT_MAX:
        return -1
    return list.index(min_v)

class Graph:
    def __init__(self, a, edges):
        self.node_info = a
        self.node_num = len(a)
        self.edges_num = len(edges)
        self.vertics = []

        for i in range(self.node_num):
            self.vertics.append([])

        for e in edges:
            u = e[0]
            v = e[1]
            self.vertics[u].append((v,1))
            self.vertics[v].append((u,1))

    def min_pos(self):
        return get_min_pos(self.node_info)

    def check_node_info(self):
        for e in self.node_info:
            if e != 0:
                return True
        return False

    def get_vertex(self, id):
        return self.vertics[id]

def dijkstra(g, s):
    vnum = g.node_num
    dist = [INT_MAX for x in range(vnum)]
    dist[s] = 0
    que = [(dist[s], s)]
    while len(que) > 0 :
        u_dist, u = que.pop(0)
        for v, w in g.get_vertex(u) :
            if dist[v] > dist[u] + w :
                dist[v] = dist[u] + w
                bisect.insort(que, (dist[v], v))
    return dist

def solution(a, edges):
    if sum(a) != 0:
        return -1
    g = Graph(a, edges)
    ret = 0

    while min(g.node_info) != 0:
        cur_minpos = g.min_pos() # 기준
        if cur_minpos < 0:
            return 0

        cur_dist = dijkstra(g, cur_minpos) # 거리계산

        dist_rank = min_dist_index(cur_dist)

        # target_pos = min_dist_pos(cur_dist) # 기준에서 가장 가까운 노드 위치
        stop_flag = False
        for dist, target_pos in dist_rank:
            cur_val = g.node_info[cur_minpos] # 기준의 값
            tar_val = g.node_info[target_pos] # 기준에서 가장 가까운 노드 위치의 값
            if tar_val > 0:
                move_amount = 0
                if abs(cur_val) >= tar_val:
                    cur_val += tar_val
                    move_amount = tar_val
                    tar_val = 0

                else:
                    move_amount = abs(cur_val)
                    cur_val = 0
                    tar_val -= abs(cur_val)
                    stop_flag = True

                g.node_info[cur_minpos] = cur_val
                g.node_info[target_pos] = tar_val

                ret += move_amount * cur_dist[target_pos]
            if stop_flag == True:
                break
    return ret

a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))
