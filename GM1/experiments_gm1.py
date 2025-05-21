import numpy as np
from GM1.simulate_gm1 import simulate_gm1 # type: ignore

def run_experiments(n_experiences=10, mu=1.0):
    lambda_values = np.linspace(0.1, 0.9, 9)
    response_means = []
    waiting_means = []
    rhos = []

    for lmbda in lambda_values:
        tr_list = []
        tw_list = []

        for _ in range(n_experiences):
            tr, tw, rho = simulate_gm1(lmbda, mu)
            tr_list.append(tr)
            tw_list.append(tw)

        response_means.append(np.mean(tr_list))
        waiting_means.append(np.mean(tw_list))
        rhos.append(rho)  # rho est constant pour une paire (lambda, mu)

    return lambda_values, response_means, waiting_means, rhos
