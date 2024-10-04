def main():
    path = 'books/frankenstein.txt'

    print(get_head_and_tail(get_all_content(path)))

    print(f"Words count: {count_words(path)}")

    print(count_characters(path))


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


def get_head_and_tail(text):
    lines = text.splitlines(keepends=True)
    head = lines[:10]
    tail = lines[-10:]
    result = ""
    line_index = 0
    print("total lines: " + str(len(lines)))
    for line in head:
        result += f"{line_index}.{line}"
        line_index += 1

    line_index = len(lines) - 10
    for line in tail:
        result += f"{line_index}.{line}"
        line_index += 1

    return result


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


def count_characters(path):
    try:
        char_dic_counts = {}
        with open(path, 'r', encoding='utf-8') as file:
            for char in file.read():
                if 'a' <= char <= 'z':
                    if char.lower() in char_dic_counts:
                        char_dic_counts[char.lower()] += 1
                    else:
                        char_dic_counts[char.lower()] = 1
        sorted_dic = dict(sorted(char_dic_counts.items(), key=lambda item: ord(item[0])))
        return sorted_dic
    
    except FileNotFoundError:
        print(f"El archivo en la dirección {path} no fue encontrado.")
        return {}
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {}


if __name__ == '__main__':
    main()
