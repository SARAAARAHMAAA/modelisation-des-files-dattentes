import numpy as np

def simulate_mm1(lambda_rate, mu_rate, n_clients=1_000_000):
    arrival_times = np.cumsum(np.random.exponential(1 / lambda_rate, n_clients))
    service_times = np.random.exponential(1 / mu_rate, n_clients)

    enter_service = np.zeros(n_clients)
    leave_times = np.zeros(n_clients)

    for i in range(n_clients):
        if i == 0:
            enter_service[i] = arrival_times[i]
        else:
            enter_service[i] = max(arrival_times[i], leave_times[i - 1])
        leave_times[i] = enter_service[i] + service_times[i]

    response_times = leave_times - arrival_times
    waiting_times = enter_service - arrival_times
    rho = lambda_rate / mu_rate

    return np.mean(response_times), np.mean(waiting_times), rho
