class Graph:
    def __init__(self, edges):
        self.graph_dict = {}
        self.edges = edges
        for src, dest in self.edges:
            if src in self.graph_dict:
                self.graph_dict[src].append(dest)
            else:
                self.graph_dict[src] = [dest]
    
    def get_paths(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []
        
        paths = []
        for i in self.graph_dict[start]:
            if i not in path:
                new_paths = self.get_paths(i,end,path)
                for j in new_paths:
                    paths.append(j)
        return paths
            

    def get_shortest_path(self, start, end, path=[]):
        
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = float("inf")
        sp = []
        for i in self.graph_dict[start]:
            if i not in path:
                new_paths = self.get_paths(i, end, path)
                for i in new_paths:
                    if len(i) < shortest_path:
                        shortest_path = len(i)
                        sp = i
        return sp
                

routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

directions = Graph(routes)
print(directions.get_paths("Mumbai", "Toronto"))
print(directions.get_shortest_path("Mumbai", "Toronto"))