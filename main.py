from trie import Trie, TrieNode, get_english_trie


def read_board():
    board = []
    print("Enter the board. (use spaces to exclude cells)")
    for _ in range(8):
        row = input(f"Row {_ + 1}: ")
        row = row.ljust(6, " ")
        board.append(row)

    while True:
        print_board(board)
        confirm = input("Is this the board you want to use? (Y/n): ")
        if confirm.lower() == "n":
            row = int(input("Enter the row to change: ")) - 1
            col_letter = int(input("Enter the column to change: ")) - 1
            col = ord(col_letter) - ord("a")
            char = input("Enter the new character: ")
            board[row] = board[row][:col] + char + board[row][col + 1 :]
        else:
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


def print_board(board):
    print("  a b c d e f")
    for i in range(8):
        print(i + 1, end=" ")
        for j in range(6):
            print(board[i][j], end=" ")
        print()


def display_answer(board, path, m, n):
    print("  a b c d e f")
    for i in range(n):
        print(i + 1, end=" ")
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
            "\n\nEnter a word to display its path, a ? to redisplay all words,\n"
            "!(mn) to display answers that contain a specific cell or nothing to exit: "
        )
        if word == "":
            return
        elif word == "?":
            print_words(words)
            print_board(board)
        elif word.startswith("!"):
            filtered = filter_answers(words, word[1:])
            print_words(filtered)
        elif word in words:
            display_answer(board, words[word], m, n)
        else:
            print("Word not found in the board")


def filter_answers(words, coords):
    filtered = dict()
    if len(coords) != 2:
        return filtered

    c1 = coords[0].lower()
    c2 = coords[1]

    cell = (int(c2) - 1, ord(c1) - ord("a"))

    for word, path in words.items():
        if cell in path:
            filtered[word] = path
    return filtered


def print_words(words):
    print(f"{len(words)} words found:")

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
        print("Calculating... ", i / n * 100, "%")
        for j in range(m):
            dfs(board, trie, i, j, list(), words, m, n)

    output(board, words, m, n)


if __name__ == "__main__":
    main()
