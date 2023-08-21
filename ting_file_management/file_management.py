import sys


def txt_importer(path_file):
    try:
        with open(path_file, 'r') as file:
            if path_file.endswith(".txt"):
                lines = file.read().split("\n")
                return lines
            else:
                print("Formato inválido", file=sys.stderr)
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    return []
