def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0
    maxi = 100
    mini = 0
    guess = None

    while guess != val:
        num_guesses += 1
        guess = (maxi - mini) / 2 + mini

        if val > guess:
            mini = guess

        elif val < guess:
            maxi = guess

    return num_guesses