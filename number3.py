def get_totals(books):
    return list(map(lambda b: (b[0], b[2] * b[3]), books))
