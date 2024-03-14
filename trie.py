import json
import pickle


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for letter in word:
            index = ord(letter) - ord("a")
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.isLeaf = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for letter in word:
            index = ord(letter) - ord("a")
            if not current.children[index]:
                return False
            current = current.children[index]
        return current.isLeaf and current

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for letter in prefix:
            index = ord(letter) - ord("a")
            if not current.children[index]:
                return False
            current = current.children[index]
        return True


def get_english_trie():
    try:
        with open("data/trie.pkl", "rb") as pickle_in:
            trie = pickle.load(pickle_in)
            return trie
    except FileNotFoundError:
        print("Cached trie not found.")

    return build_trie()


def build_trie():
    print("Building trie...")
    trie = Trie()

    with open("data/words.json", "r") as f:
        words: dict = json.load(f)
        for word in words.keys():
            try:
                # Only insert if word is only composed of letters
                # and at least 4 characters long
                if word.isalpha() and len(word) >= 4:
                    trie.insert(word)
            except:
                print(f"Error inserting {word}")
                raise

    pickle.dump(trie, open("data/trie.pkl", "wb"))

    return trie


if __name__ == "__main__":
    build_trie()
