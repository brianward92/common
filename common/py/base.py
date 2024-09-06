from collections.abc import Iterable


def invert_dict(d, one_to_one=False):
    res = dict()
    if one_to_one:
        for k, v in d.items():
            if v in res:
                raise ValueError(f"Duplicated key {v} (value in input).")
            res[v] = k
    else:
        for k, v in d.items():
            res[v] = res.get(v, []) + [k]
    return res


def to_list(values):
    if isinstance(values, (str, bytes)):
        return [values]
    elif values is None:
        return []
    elif isinstance(values, Iterable):
        return list(values)
    else:
        return [values]
