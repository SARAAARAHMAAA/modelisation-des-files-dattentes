import matplotlib.pyplot as plt

def plot_results(lambda_values, response_times, waiting_times, occupation_rates):
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.plot(lambda_values, response_times, marker='o', color='blue')
    plt.title('Temps de réponse moyen (M/G/1)')
    plt.xlabel('Taux d\'arrivée λ')
    plt.ylabel('Temps de réponse')

    plt.subplot(1, 3, 2)
    plt.plot(lambda_values, waiting_times, marker='o', color='green')
    plt.title('Temps d\'attente moyen (M/G/1)')
    plt.xlabel('Taux d\'arrivée λ')
    plt.ylabel('Temps d\'attente')

    plt.subplot(1, 3, 3)
    plt.plot(lambda_values, occupation_rates, marker='o', color='red')
    plt.title('Taux d\'occupation du serveur (M/G/1)')
    plt.xlabel('Taux d\'arrivée λ')
    plt.ylabel('ρ = λ/μ')

    plt.tight_layout()
    plt.show()
