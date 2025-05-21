from mm1.experiments_mm1 import run_experiments
from mm1.plots_mm1 import plot_results
 
if __name__ == "__main__":
    lambda_vals, tr, tw, rho = run_experiments()
    plot_results(lambda_vals, tr, tw, rho)
