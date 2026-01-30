def retrieve_similar_decisions(purchase_amount, decisions, threshold=0.2):
    similar = []
    for d in decisions:
        diff_ratio = abs(d.purchase_amount - purchase_amount) / purchase_amount
        if diff_ratio <= threshold:
            similar.append(d)
    return similar
