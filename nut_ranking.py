# Merge-Sort-Based Pairwise Ranking for a “Middle Ground”

def user_prefers(a, b):
    """
    Prompt the user to indicate if they prefer 'a' over 'b'.
    Returns True if 'a' is preferred, False otherwise.
    """
    while True:
        answer = input(f"Do you prefer {a} over {b}? (y/n): ").strip().lower()
        if answer in ('y', 'n'):
            return answer == 'y'
        print("Please enter 'y' or 'n'.")

def merge_rank(left, right):
    """
    Merge two sorted lists of items by comparing their heads.
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if user_prefers(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append any leftovers
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def rank_items_merge(items):
    """
    Rank a list of items using a merge-sort style approach.
    This uses about O(n log n) comparisons—more than pure binary insertion
    but far fewer than comparing every pair.
    """
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = rank_items_merge(items[:mid])
    right = rank_items_merge(items[mid:])
    return merge_rank(left, right)

if __name__ == "__main__":
    nuts = [
        "almonds",
        "Brazil nuts",
        "cashew nuts",
        "hazelnuts",
        "macadamias",
        "pecans",
        "pine nuts",
        "pistachios",
        "walnuts",
        "peanuts"
    ]
    print("Let's rank your nuts with a merge-sort–based method!")
    final_ranking = rank_items_merge(nuts)
    print("\nYour final ranking:")
    for idx, nut in enumerate(final_ranking, start=1):
        print(f"{idx}. {nut}")
