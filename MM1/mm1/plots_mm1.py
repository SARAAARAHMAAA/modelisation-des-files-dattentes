import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def plot_results(lambda_vals, response, waiting, rhos):
    plt.figure(figsize=(14, 5))

    plt.subplot(1, 3, 1)
    plt.plot(lambda_vals, response, marker='o')
    plt.title("Temps de réponse moyen")
    plt.xlabel("λ")
    plt.ylabel("Temps de réponse")

    plt.subplot(1, 3, 2)
    plt.plot(lambda_vals, waiting, marker='o', color='orange')
    plt.title("Temps d'attente moyen")
    plt.xlabel("λ")
    plt.ylabel("Temps d'attente")

    plt.subplot(1, 3, 3)
    plt.plot(lambda_vals, rhos, marker='o', color='green')
    plt.title("Taux d’occupation (ρ)")
    plt.xlabel("λ")
    plt.ylabel("ρ")

    plt.tight_layout()
    plt.show()
