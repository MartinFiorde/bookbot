import sys
from stats import count_words, count_characters


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    # print(get_head_and_tail(get_all_content(path)))
    # print(f"Words count: {count_words(path)}")
    # print(count_characters(path))

    print(generate_report(path))


def get_all_content(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
            # file.seek(0) # put pointer back to start of file. usefull if you need to reuse the same file in the "with open()" block
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
    for line in head:
        result += f"{line_index}.{line}"
        line_index += 1

    line_index = len(lines) - 10
    for line in tail:
        result += f"{line_index}.{line}"
        line_index += 1

    return result


def generate_report(path):
    result = ""
    result += f"--- Begin report of {path} ---\n"

    result += f"{count_words(path)} words found in the document\n\n"

    dic_sorted_by_value = {
        k: v
        for k, v in sorted(
            count_characters(path).items(), key=lambda item: item[1], reverse=True
        )
    }
    for key in dic_sorted_by_value:
        result += f"The '{key}' character was found {dic_sorted_by_value[key]} times\n"

    result += f"--- End report ---"
    return result


if __name__ == "__main__":
    main()
