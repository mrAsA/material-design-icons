def append(list1, list2):
    list1.extend(list2)
    return list1


def concat(lists):
    flat_list = [val for item in lists for val in (item if type(item) is list else item)]
    return flat_list


def filter(function, list):
    filtered_list = [item for item in list if function(item)]
    return filtered_list


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)

    return acc


def foldr(function, list, initial):
    acc = initial
    for item in reversed(list):
        acc = function(acc, item)

    return acc


def reverse(list):
    list.reverse()
    return list
