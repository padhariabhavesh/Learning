"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
"""


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.prefixCount = 0
        self.wordEnd = False


class Solution:
    def insert(self, trie: TrieNode, word: str) -> None:
        currentLayer = trie
        for char in word:
            currentLayer.prefixCount += 1
            currentLayer = currentLayer.children[char]
        currentLayer.wordEnd = True

    def neighbors(self, cell: Tuple[int, int]) -> Generator:
        i, j = cell
        for r, s in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= i + r < self.m and 0 <= j + s < self.n:
                yield ((i + r, j + s), self.board[i + r][j + s])

    def backtrack(self, cell: Tuple[int, int], node: TrieNode) -> int:
        i, j = cell;
        removedWordsCount = 0

        if node.prefixCount > 0:
            for neighbor, char in self.neighbors(cell):
                if neighbor not in self.visited and char in node.children.keys():
                    self.visited.add(neighbor);
                    self.currentWord.append(char)
                    removedWordsCount += self.backtrack(neighbor, node.children[char])
                    self.visited.remove(neighbor);
                    self.currentWord.pop()
            node.prefixCount -= removedWordsCount

        if node.wordEnd:
            node.wordEnd = False;
            removedWordsCount += 1
            self.wordsOnBoard.append("".join(self.currentWord))

        return removedWordsCount

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board;
        self.m, self.n = len(board), len(board[0])

        wordTrie = TrieNode()
        for word in words:
            self.insert(wordTrie, word)

        self.wordsOnBoard = []
        for i, j in product(range(self.m), range(self.n)):
            if board[i][j] in wordTrie.children.keys():
                self.visited = set([(i, j)]);
                self.currentWord = [board[i][j]]
                self.backtrack((i, j), wordTrie.children[board[i][j]])

        return self.wordsOnBoard