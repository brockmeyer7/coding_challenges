def noPrefix(words):

    class TrieNode:
        def __init__(self) -> None:
            self.children = {}
            self.is_end = False

    class Trie:
        def __init__(self) -> None:
            self.root = TrieNode()

        def insert(self, key):
            node = self.root
            print('INSERT', end=' ')
            for c in key:
                if c in node.children:
                    node = node.children[c]
                else:
                    node.children[c] = TrieNode()
                    node = node.children[c]
                print(c, end='')
            print('\n')
            node.is_end = True

        def search(self, key) -> bool:
            node = self.root

            for c in key:
                if c in node.children:
                    node = node.children[c]
                else:
                    return False

                if node.is_end:
                    return True

            if node.children != {}:
                return True

            return False

    t = Trie()

    for w in words:
        if t.search(w):
            print('BAD SET')
            print(w)
            return
        t.insert(w)
    print('GOOD SET')


if __name__ == '__main__':
    words = ['aab', 'defgab', 'abcde', 'cedaaa', 'bbbbbbbbbb', 'jabjjjad']

    noPrefix(words)
