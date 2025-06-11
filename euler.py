def read_the_matrix(filename):
    with open(filename, "r") as f:
        n = int(f.readline())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)
        return n, matrix

def rank(matrix, n):
    in_deg = [0] * n
    out_deg = [0] * n
    for u in range(n):
        for v in range(n):
            if matrix[u][v]:
                out_deg[u] += matrix[u][v]
                in_deg[v] += matrix[u][v]
    return in_deg, out_deg

def is_the_half_euler_graph(in_deg, out_deg, n):
    start = end = -1
    for i in range(n):
        if out_deg[i] - in_deg[i] == 1:
            if start == -1:
                start = i
            else:
                return False, -1
        elif in_deg[i] - out_deg[i] == 1:
            if end == -1:
                end = i
            else:
                return False, -1
        elif in_deg[i] != out_deg[i]:
            return False, -1
    if (start == -1 and end == -1):

        # Euler circuit (not semi)
        start = next((i for i in range(n) if out_deg[i] > 0), 0)
    return True, start

def find_the_road_to_euler(matrix, n, start):
    stack = [start]
    path = []
    adj = [matrix[i][:] for i in range(n)]  # Copy matrix
    while stack:
        u = stack[-1]
        found = False
        for v in range(n):
            if adj[u][v] > 0:
                stack.append(v)
                adj[u][v] -= 1  # Delete the edge (xoa canh da di)
                found = True
                break
        if not found:
            path.append(stack.pop())
    return path[::-1]  # Reverse the road (dao nguoc duong di)

def main():
    n, matrix = read_the_matrix("D:\\Euler_half_graph\\dothi.in")
    in_deg, out_deg = rank(matrix, n)

    is_semi, start = is_the_half_euler_graph(in_deg, out_deg, n)
    if not is_semi:
        print("G is not a half Euler graph")
        return

    road = find_the_road_to_euler(matrix, n, start)

    print("G is half Euler graph.")
    print("Road to Euler:")
    print(" -> ".join(map(str, road)))

if __name__ == "__main__":
    main()  