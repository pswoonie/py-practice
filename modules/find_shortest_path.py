# This file is find_shortest_path.py

def show_path(*args):
    dist: dict = args[0]['dist']
    nodes: dict = args[0]['nodes']
    start: str = args[1]['start']
    dest: str = args[1]['end']

    dest_stack: list = [dest,]

    curr: str = dest
    _from: str = nodes[curr]

    while True:
        if _from == None: break
        curr = _from
        _from = nodes[curr]
        dest_stack.append(curr)

    dest_stack.reverse()
    path_ui: str = '->'.join(dest_stack)
    print(f'--Total Distance From {start} to {dest}: {dist[dest]}, path: {path_ui}')



if __name__ == "__main__":
    show_path()