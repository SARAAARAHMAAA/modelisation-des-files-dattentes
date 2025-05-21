from GM1.experiments_gm1 import run_experiments  # type: ignore
from GM1.plots_gm1 import plot_results  # type: ignore

if __name__ == "__main__":
    lambda_vals, response_times, waiting_times, occupation_rates = run_experiments()

    # Affichage dans le terminal (comme pour MM1)
    print("\nRésultats G/M/1 :")
    for i in range(len(lambda_vals)):
        print(f"λ = {lambda_vals[i]:.1f} | Temps de réponse = {response_times[i]:.4f} | Temps d'attente = {waiting_times[i]:.4f} | ρ = {occupation_rates[i]:.4f}")

    # Affichage graphique
    plot_results(lambda_vals, response_times, waiting_times, occupation_rates)

