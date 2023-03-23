def merge_sort(str):
    if not str:
        return []
    if len(str) <= 1:
        return [str[0]]

    mid = len(str) // 2
    left = merge_sort(str[:mid])
    right = merge_sort(str[mid:len(str)])

    return merge(left, right)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left[0] > right[0]:
        return [right[0]] + merge(left, right[1:])
    else:
        return [left[0]] + merge(left[1:], right)


def is_anagram(first_string, second_string):
    first_sorted = "".join(merge_sort(first_string.lower()))
    second_sorted = "".join(merge_sort(second_string.lower()))

    if first_string == "" or second_string == "":
        return (first_sorted, second_sorted, False)

    return (first_sorted, second_sorted, first_sorted == second_sorted)

#  referencias usadas para resolver o requisito:
#  https://panda.ime.usp.br/panda/static/pythonds_pt/02-AnaliseDeAlgoritmos/ExemploDeDeteccaoDeAnagramas.html
#  https://www.youtube.com/watch?v=yWdB1o8ry8I&ab_channel=Programa%C3%A7%C3%A3oPython
#  https://www.youtube.com/watch?v=6-umTQjRvmM&ab_channel=PalancaCode
#  utilizei conteudo do couse da trybe e também chatGPT
