def main():
    path = 'books/frankenstein.txt'
    print(get_all_content(path))


def get_all_content(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            #file.seek(0) # put pointer back to start of file. usefull if you need to reuse the same file in the "with open()" block
        return content


main()
