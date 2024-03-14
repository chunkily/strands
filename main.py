from trie import Trie, TrieNode, get_english_trie


def read_board():
    board = [
        "frnnrd",
        "ogeuoa",
        "nhtyrl",
        "roueob",
        "sennou",
        "pyffsg",
        "roadot",
        "kycoye",
    ]

    return board


def dfs(board, trie: Trie, i, j, path: list, words: dict, m, n):
    # Check if the current cell is within the board and has not been visited yet
    if i < 0 or i >= n or j < 0 or j >= m or (i, j) in path:
        return

    # Check if the current cell is not removed
    char = board[i][j]
    if char == " ":
        return

    # Check if the current path is a prefix of any word
    word = "".join([board[x][y] for x, y in path]) + char
    if not trie.startsWith(word):
        return

    path.append((i, j))

    # If the current path is a word, add it to the result
    if trie.search(word) and word not in words:
        words[word] = path.copy()

    # Explore the neighboring cells in the board
    for dx, dy in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        dfs(board, trie, i + dx, j + dy, path, words, m, n)

    # Backtrack and unmark the current cell
    path.pop()


def display_answer(board, path, m, n):
    for i in range(n):
        for j in range(m):
            char = board[i][j]
            if (i, j) in path:
                print(char.upper(), end=" ")
            else:
                print(".", end=" ")
        print()


def output(board, words, m, n):
    print_words(words)

    while True:
        word = input(
            "\n\nEnter a word to display its path, a ? to redisplay all words,\n or press Enter to exit: "
        )
        if word == "":
            return
        elif word == "?":
            print_words(words)
        elif word in words:
            display_answer(board, words[word], m, n)
        else:
            print("Word not found in the board")


def print_words(words):
    print(f"{len(words)} words found in the board:")

    terminal_width = 80
    pos = 0
    for word in sorted(words.keys()):
        word_len = len(word)
        pos += word_len
        if pos > terminal_width:
            print()
            pos = word_len
        print(word, end=" ")


def main():
    trie = get_english_trie()

    board = read_board()
    n = len(board)
    m = len(board[0])
    words = dict()

    for i in range(n):
        for j in range(m):
            dfs(board, trie, i, j, list(), words, m, n)

    output(board, words, m, n)


if __name__ == "__main__":
    main()
