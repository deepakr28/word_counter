import argparse
from service.TrieService import TrieService
from tabulate import tabulate

TABLE_HEADERS = ["Predefined Word", "Match Count"]
SPECTIAL_CHARS = '.,?#'

class WordCounter:
    def __init__(self, content_file, pre_defined_file):
        self.result_dict = dict()
        self.trie_service = TrieService()
        self.content_file = content_file
        self.pre_defined_word_file = pre_defined_file

    def process_pre_defined_file(self):
        try:
            with open(self.pre_defined_word_file, "r") as f1:
                for word in f1:
                    word = word.strip()
                    word = self.remove_special_chars(word)
                    if len(word) > 0:
                        self.trie_service.insert_word(word)
                        self.result_dict[word] = 0
        except Exception as e:
            print(f"Unable to read content file: {self.pre_defined_word_file}")
            raise e

    def remove_special_chars(self, word):
        return word.rstrip(SPECTIAL_CHARS)

    def read_content_file(self):
        with open(self.content_file, "r") as f2:
            for line in f2:
                for word in line.strip().split():
                    word = self.remove_special_chars(word)
                    try:
                        if self.trie_service.search_word(word):
                            word_count = self.result_dict.get(word, 0) + 1
                            self.result_dict[word] = word_count
                    except Exception as e:
                        print(f"Error while searching for pre-defined word {word}")
                        print(e.__traceback__)

    def print_result_dict(self):
        if not self.result_dict:
            return
        table_values = [[word, count] for word, count in self.result_dict.items()]
        print(
            tabulate(
                table_values,
                headers=TABLE_HEADERS,
                tablefmt="heavy_grid",
                maxcolwidths=[None, 30],
            )
        )


def validate_args(args):
    try:
        open(args.input_content_file)
    except Exception as e:
        print(f"unable to open {args.input_content_file}")
        raise e

    try:
        open(args.pre_defined_word_file)
    except Exception as e:
        print(f"unable to open {args.pre_defined_word_file}")
        raise e


def parse_arguments():
    parser = argparse.ArgumentParser(prog="File word counter", description="something")

    options = parser.add_argument_group("Pre defined word files")
    options.add_argument(
        "-c",
        "--content_file",
        metavar="File 1 with the content of lines to search words in.",
        dest="input_content_file",
        required=True,
    )
    options.add_argument(
        "-p",
        "--pre-defined-word",
        metavar="File 2 with the pre_defined of words to search in content file.",
        dest="pre_defined_word_file",
        required=True,
    )

    validate_args(parser.parse_args())
    return parser.parse_args()


def main():
    try:
        args = parse_arguments()
        word_counter = WordCounter(
            pre_defined_file=args.pre_defined_word_file,
            content_file=args.input_content_file,
        )
        word_counter.process_pre_defined_file()
        word_counter.read_content_file()

        word_counter.print_result_dict()

    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
