class Trie(object):

    def __init__(self):
        self.words = {}

    def insert(self, word):
        if word == "":
            self.word[""] = None
            return
        chars = [char for char in word]
        self.words = self._insert_into_words(chars, self.words)

    def _insert_into_words(self, chars, word_dict):
        if not chars:
            word_dict[None] = None
            return word_dict
        char = chars[0]
        if char not in word_dict:
            word_dict[char] = self._insert_into_words(chars[1:], {})
        else:
            word_dict[char] = self._insert_into_words(chars[1:], word_dict[char])
        return word_dict
        
    def search(self, word):
        return self._search(word, must_end=True)

    def startsWith(self, prefix):
        return self._search(prefix, must_end=False)

    def _search(self, word, must_end=True):
        if not word:
            return "" in self.words

        first_char = word[0]
        if first_char not in self.words:
            return False

        cur = self.words[first_char]
        for char in word[1:]:
            if char in cur:
                cur = cur[char]
            else:
                return False
        
        return cur is None or None in cur if must_end else True

if __name__ == "__main__":
    trie = Trie();

    trie.insert("apple");
    print("True: ", trie.search("apple"))   # returns true
    print("False: ", trie.search("app"))     # returns false
    print("True: ", trie.startsWith("app")) # returns true
    trie.insert("app")
    print("True: ", trie.search("app"))     # returns true

    print("WORDS: ", trie.words)

    print()
    print("Inserting aaaa")
    trie.insert("aaaa")
    print("True: ", trie.startsWith("a"))
    print("True: ", trie.startsWith("aaa"))
    print("False: ", trie.search("aaa"))
    print("True: ", trie.startsWith("aaaa"))
    print("True: ", trie.search("aaaa"))

    print()
    print("Inserting aaa")
    trie.insert("aaa")
    print(trie.words)
    print("True: ", trie.startsWith("a"))
    print("True: ", trie.startsWith("aaa"))
    print("True: ", trie.search("aaa"))
    print("True: ", trie.startsWith("aaaa"))
    print("True: ", trie.search("aaaa"))
    

    print()
    print("Inserting aaaaa")
    trie.insert("aaaaa")
    print("True: ", trie.startsWith("a"))
    print("True: ", trie.startsWith("aaa"))
    print("True: ", trie.search("aaa"))
    print("True: ", trie.startsWith("aaaa"))
    print("True: ", trie.search("aaaa"))
    print("True:", trie.search("aaaaa"))
    print("True:", trie.startsWith("aaaaa"))
