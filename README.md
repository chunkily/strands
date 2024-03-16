# Strands

A program to help solve a [strands](https://www.nytimes.com/games/strands)
puzzle.

## Requirements

Probably any modern Python 3 version. Tested to work with Python 3.11.

You will also need a word list in a JSON format. I used `words_dictionary` from
[dwyl/english-words](https://github.com/dwyl/english-words/blob/master/words_dictionary.json),
licensed under
[The Unlicense license](https://github.com/dwyl/english-words/blob/master/LICENSE.md).

The program caches the trie in a pickle file that takes up about 44MB of space
with the `words_dictionary` word list.

## Usage

Place the word list in the data directory, and then run the `main.py` script.
Follow the instructions to input the puzzle.

```sh
python main.py
```

### Rebuilding trie

Run the `trie.py` script to rebuild the trie from the word list.

```sh
python trie.py
```
