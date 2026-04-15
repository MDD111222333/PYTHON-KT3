def get_books(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]
        
        def parse_line(line):
            parts = line.strip().split('|')
            return [parts[0], parts[1], parts[2], int(parts[3]), float(parts[4])]
            
        return list(map(parse_line, filter(lambda l: bool(l.strip()), lines)))

