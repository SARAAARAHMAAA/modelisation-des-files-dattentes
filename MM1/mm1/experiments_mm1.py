from mm1.simulate_mm1 import simulate_mm1
import numpy as np

def run_experiments(mu=1.0, repeats=50):
    lambda_values = [round(x, 1) for x in list(np.arange(0.1, 1.0, 0.1))]
    response_times, waiting_times, rhos = [], [], []

    for lmbda in lambda_values:
        all_tr, all_tw, all_rho = [], [], []

        for _ in range(repeats):
            tr, tw, rho = simulate_mm1(lmbda, mu)
            all_tr.append(tr)
            all_tw.append(tw)
            all_rho.append(rho)

        response_times.append(np.mean(all_tr))
        waiting_times.append(np.mean(all_tw))
        rhos.append(np.mean(all_rho))

        print(f"λ = {lmbda:.1f} | T ≈ {np.mean(all_tr):.4f} | W ≈ {np.mean(all_tw):.4f} | ρ ≈ {np.mean(all_rho):.2f}")

    return lambda_values, response_times, waiting_times, rhos
