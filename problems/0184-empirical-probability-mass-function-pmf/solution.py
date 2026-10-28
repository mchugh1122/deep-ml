from collections import Counter

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    if not samples:
        return []
    
    total_count = len(samples)
    counts = Counter(samples)
    
    return [(val, counts[val] / total_count) for val in sorted(counts.keys())]