from typing import List


def exists_word(word: str, queue) -> List[dict]:
    result = []

    for i in range(len(queue)):
        file_data = queue.search(i)
        filename = file_data["nome_do_arquivo"]
        lines_with_word = []

        for line_num, line in enumerate(
            file_data["linhas_do_arquivo"], start=1
                ):
            if word.lower() in line.lower():  # Busca case insensitive
                lines_with_word.append({"linha": line_num})

        if lines_with_word:
            result.append({
                "palavra": word,
                "arquivo": filename,
                "ocorrencias": lines_with_word
            })

    return result


def search_by_word(word: str, queue) -> List[dict]:
    result = []

    for i in range(len(queue)):
        file_data = queue.search(i)
        filename = file_data["nome_do_arquivo"]
        occurrences = []

        for line_num, line in enumerate(
            file_data["linhas_do_arquivo"], start=1
                ):
            if word.lower() in line.lower():  # Busca case insensitive
                occurrences.append({
                    "linha": line_num,
                    "conteudo": line.strip()  # Conteúdo da linha encontrada
                })

        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": filename,
                "ocorrencias": occurrences
            })

    return result
