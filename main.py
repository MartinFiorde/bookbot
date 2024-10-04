def main():
    path = 'books/frankenstein.txt'
    print(get_all_content(path))
    print(f"Words count: {count_words(path)}")


def get_all_content(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            #file.seek(0) # put pointer back to start of file. usefull if you need to reuse the same file in the "with open()" block
        return content
    
    except FileNotFoundError:
        print(f"El archivo en la dirección {path} no fue encontrado.")
        return ""
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return ""


def count_words(path):
    try:
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                count += len(line.split())
        return count
    
    except FileNotFoundError:
        print(f"El archivo en la dirección {path} no fue encontrado.")
        return 0
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return 0


main()
