def get_books(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]
        
        def parse_line(line):
            parts = line.strip().split('|')
            return [parts[0], parts[1], parts[2], int(parts[3]), float(parts[4])]
            
        return list(map(parse_line, filter(lambda l: bool(l.strip()), lines)))


def filtered_books(books, search_term):
    filtered = filter(lambda b: search_term.lower() in b[1].lower(), books)
    
    def format_book(b):
        return [b[0], f"{b[1]}, {b[2]}", b[3], b[4]]
        
    return list(map(format_book, filtered))


def get_totals(books):
    return list(map(lambda b: (b[0], b[2] * b[3]), books))
