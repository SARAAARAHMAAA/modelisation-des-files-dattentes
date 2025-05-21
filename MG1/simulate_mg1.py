import numpy as np

def simulate_mg1(lambda_val, mu, J=1000000):
    arrival_times = np.cumsum(np.random.exponential(1 / lambda_val, size=J))
    
    # Service times : uniforme entre (0.5 / μ) et (1.5 / μ) par exemple
    service_times = np.random.uniform(0.5 / mu, 1.5 / mu, size=J)
    
    start_service_times = np.zeros(J)
    leave_times = np.zeros(J)

    start_service_times[0] = arrival_times[0]
    leave_times[0] = start_service_times[0] + service_times[0]

    for i in range(1, J):
        start_service_times[i] = max(arrival_times[i], leave_times[i-1])
        leave_times[i] = start_service_times[i] + service_times[i]

    response_times = leave_times - arrival_times
    waiting_times = start_service_times - arrival_times
    occupation_rate = np.mean(service_times) * lambda_val

    return np.mean(response_times), np.mean(waiting_times), occupation_rate
