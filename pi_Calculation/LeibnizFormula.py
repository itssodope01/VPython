def leibniz_pi(num_terms):
    pi_terms = 0.0
    n = 3.0

    for i in range(num_terms):
        if (i + 1) % 2 != 0:
            pi_terms -= (1/n)
        else:
            pi_terms += (1/n)

        n += 2

    pi_estimate = 4 * (1 + pi_terms)
    return pi_estimate

num_terms = 1000000
pi_value = leibniz_pi(num_terms)
print(pi_value)
