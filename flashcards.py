def generate(concepts):
    cards = []
    for term in concepts:
        cards.append({
            "term": term,
            "definition": f"This is a placeholder definition for {term}."
        })
    return cards
