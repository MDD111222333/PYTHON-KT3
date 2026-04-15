def filtered_books(books, search_term):
    filtered = filter(lambda b: search_term.lower() in b[1].lower(), books)
    
    def format_book(b):
        return [b[0], f"{b[1]}, {b[2]}", b[3], b[4]]
        
    return list(map(format_book, filtered))

