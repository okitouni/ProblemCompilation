# count the number of matching islands in two img inputs
# partial matches do not count
def count_matches(img1, img2):
    n = len(img1)

    def get_children(i, j):
        children = []
        if i > 0:  # top neighbor
            children.append((i - 1, j))
        if i < n - 1:  # bottom neighbor
            children.append((i + 1, j))
        if j > 0:  # left neighbor
            children.append((i, j - 1))
        if j < n - 1:  # right neighbor
            children.append((i, j + 1))
        return children

    cache = dict()
    def touches_mismatch(i, j):
        answer = False
        visited.add((i,j))
        if img1[i][j] != img2[i][j]:
            answer = True
        else:
            if img1[i][j] == "1":
                for child in get_children(i, j):
                    if child not in visited:
                        if touches_mismatch(*child):
                            answer = True
                            break
        cache[(i,j)] = answer
        return answer

    count = 0
    for i in range(n):
        for j in range(n):
            visited = set()
            if img1[i][j] == "1" and (i,j) not in cache and not touches_mismatch(i, j): #amortized O(1)
                # remove ``(i,j) not in cache`` to count size of islands
                count += 1
    return count


img1 = ["0001", "0011", "0000", "1001"]
img2 = ["0001", "0011", "0000", "1001"]
print(*[r1 + " " + r2 for r1, r2 in zip(img1, img2)], sep="\n")
print("count", count_matches(img1, img2))
