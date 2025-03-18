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
        with open(path, "r", encoding="utf-8") as file:
            for char in file.read():
                if str(char).isalpha():
                    if char.lower() in char_dic_counts:
                        char_dic_counts[char.lower()] += 1
                    else:
                        char_dic_counts[char.lower()] = 1
        sorted_dic = dict(
            sorted(char_dic_counts.items(), key=lambda item: ord(item[0]))
        )
        return sorted_dic

    except FileNotFoundError:
        print(f"El archivo en la dirección {path} no fue encontrado.")
        return {}
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {}

