from models.TrieNode import TrieNode


class TrieService:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        """

        :param word: Word to insert in Trie
        :return: None
        """
        node = self.root
        for c in word.lower():
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.is_word = True

    def search_word(self, word):
        """

        :param word: Word to search in Trie
        :return: True if word exists else False
        """
        node = self.root
        for c in word.lower():
            if c not in node.children:
                return False
            node = node.children[c]

        if node.is_word:
            return True

