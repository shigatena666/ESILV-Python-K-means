def is_float(element):
    try:
        float(element)
        return True

    except ValueError:
        return False


def format_clusters(clusters):
    final_st = ""

    for key, value in clusters.items():
        final_st += f"C{key + 1}: {value}\n"

    return final_st
