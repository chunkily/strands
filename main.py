import json
import pickle
from trie import Trie


def build_english_trie():
    try:
        pickle_in = open("data/trie.pkl", "rb")
        trie = pickle.load(pickle_in)
        print("Loaded trie from trie.pkl")
        return trie
    except FileNotFoundError:
        print("Building trie from words.json")

    trie = Trie()

    with open("data/words.json", "r") as f:
        words: dict = json.load(f)
        for word in words.keys():
            trie.insert(word)

    pickle.dump(trie, open("data/trie.pkl", "wb"))

    return trie


def read_board():
    board = [["h", "e", "l"], ["w", "o", "l"], ["o", "r", "d"]]

    for row in board:
        print(row)

    return board


def gen_permutations(board, trie, i, j, visited, word, words, n, m):
    # Depth first search
    for char in adjacent(board, i, j, n, m):
        if visited[i][j]:
            continue
        word += char
        print(word)
        if trie.search(word):
            words.add(word)
        if trie.startsWith(word):
            new_visited = visited.copy()
            new_visited[i][j] = True
            for x in range(max(0, i - 1), min(n, i + 2)):
                for y in range(max(0, j - 1), min(m, j + 2)):
                    gen_permutations(board, trie, x, y, new_visited, word, words, n, m)
        word = word[:-1]


def adjacent(board, i, j, n, m):
    for x in range(max(0, i - 1), min(n, i + 2)):
        for y in range(max(0, j - 1), min(m, j + 2)):
            if x != i or y != j:
                yield board[x][y]


def main():
    trie = build_english_trie()
    # print("hello", trie.search("hello"))
    # print("henlo", trie.search("henlo"))

    board = read_board()
    n = len(board)
    m = len(board[0])
    words = set()
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            gen_permutations(board, trie, i, j, visited, board[i][j], words, n, m)

    print(words)


if __name__ == "__main__":
    main()
