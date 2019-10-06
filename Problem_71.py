bounds = {"btm": 0, "top": 1}

def counting_fractions(n, d):
    known = []
    for k in range(d, 0, -1):
        if (n/k) not in known:
            known.append(n/k)
    for m in range(len(known)):
        if bounds["btm"] < known[m] < (3/7):
            bounds["btm"] = known[m]
        elif bounds["top"] > known[m] > (3/7):
            bounds["top"] = known[m]

    if n == d:
        return bounds
    else:
        print(bounds)
        return counting_fractions(n + 1, d)


def use_bounds_find_fraction(btm, top):
    return "incomplete"


# {'btm': 0.42842842842842843, 'top': 0.428714859437751}

# Unsure of the solution here, folks.
