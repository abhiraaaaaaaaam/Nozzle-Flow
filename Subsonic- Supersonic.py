import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 3.0  
dx = 0.05  # Step Size
n = int(L / dx) + 1  # Grid Points
gamma = 1.4  
CFL = 0.5  
nt = 700  
x = np.linspace(0, L, n)

def conservative_form(n, x, dx, gamma, CFL, nt):
    dens = np.zeros(n)
    temp = np.zeros(n)
    pres = np.zeros(n)
    A = np.zeros(n)
    vel = np.zeros(n)
    mass_flow = np.zeros(n)
    diff_U1 = np.zeros(n)
    diff_U2 = np.zeros(n)
    diff_U3 = np.zeros(n)
    J = np.zeros(n)

    # Initial profile setup
    for i in range(n):
        if x[i] <= 0.5:
            dens[i] = 1  
            temp[i] = 1  
        elif 0.5 < x[i] <= 1.5:
            dens[i] = 1 - 0.366 * (x[i] - 0.5)
            temp[i] = 1 - 0.167 * (x[i] - 0.5)
        elif 1.5 < x[i] <= 3:
            dens[i] = 0.634 - 0.3879 * (x[i] - 1.5)
            temp[i] = 0.833 - 0.3507 * (x[i] - 1.5)
        
        pres[i] = dens[i] * temp[i] 
        A[i] = 1 + 2.2 * (x[i] - 1.5)**2  
        vel[i] = 0.59 / (dens[i] * A[i])  

    U1 = dens * A
    U2 = dens * A * vel
    U3 = dens * A * ((temp / (gamma - 1)) + (gamma / 2) * vel**2)

    # Initializing the total flow time
    total_sim_time = 0  

    # Solving the equations (Conservative Form) using MacCormack's Method
    for z in range(nt):
        U1_old = U1.copy()
        U2_old = U2.copy()
        U3_old = U3.copy()

        # Calculating the time step using the CFL Formula
        dt = min((CFL * dx) / (np.sqrt(temp) + vel))

        # Flux vector calculation 
        F1 = U2
        F2 = (U2**2 / U1) + ((gamma - 1) / gamma) * (U3 - (gamma / 2) * (U2**2 / U1))
        F3 = (gamma * U2 * U3 / U1) - (gamma * (gamma - 1) / 2) * (U2**3 / U1**2)

        # Predictor step

        for j in range(1, n - 1):
            J[j] = (1 / gamma) * dens[j] * temp[j] * (A[j + 1] - A[j]) / dx
            diff_U1[j] = -(F1[j + 1] - F1[j]) / dx
            diff_U2[j] = -(F2[j + 1] - F2[j]) / dx + J[j]
            diff_U3[j] = -(F3[j + 1] - F3[j]) / dx

        U1 = U1 + diff_U1 * dt
        U2 = U2 + diff_U2 * dt
        U3 = U3 + diff_U3 * dt

        # Corrector step
        F1 = U2
        F2 = (U2**2 / U1) + ((gamma - 1) / gamma) * (U3 - (gamma / 2) * (U2**2 / U1))
        F3 = (gamma * U2 * U3 / U1) - (gamma * (gamma - 1) / 2) * (U2**3 / U1**2)

        dens = U1 / A
        vel = U2 / U1
        temp = (gamma - 1) * (U3 / U1 - (gamma / 2) * vel**2)
        pres = dens * temp

        diff_U1_n1 = np.zeros(n)
        diff_U2_n1 = np.zeros(n)
        diff_U3_n1 = np.zeros(n)

        for k in range(1, n - 1):
            J[k] = (1 / gamma) * dens[k] * temp[k] * (A[k] - A[k - 1]) / dx
            diff_U1_n1[k] = -(F1[k] - F1[k - 1]) / dx
            diff_U2_n1[k] = -(F2[k] - F2[k - 1]) / dx + J[k]
            diff_U3_n1[k] = -(F3[k] - F3[k - 1]) / dx

        dU1_dt = 0.5 * (diff_U1 + diff_U1_n1)
        dU2_dt = 0.5 * (diff_U2 + diff_U2_n1)
        dU3_dt = 0.5 * (diff_U3 + diff_U3_n1)

        for m in range(1, n - 1):
            U1[m] = U1_old[m] + dU1_dt[m] * dt
            U2[m] = U2_old[m] + dU2_dt[m] * dt
            U3[m] = U3_old[m] + dU3_dt[m] * dt

        # Boundary conditions
        U1[0] = dens[0] * A[0]
        U2[0] = 2 * U2[1] - U2[2]
        U3[0] = U1[0] * ((temp[0] / (gamma - 1)) + (gamma / 2) * vel[0]**2)
        U1[-1] = 2 * U1[-2] - U1[-3]
        U2[-1] = 2 * U2[-2] - U2[-3]
        U3[-1] = 2 * U3[-2] - U3[-3]

        dens = U1 / A
        vel = U2 / U1
        temp = (gamma - 1) * (U3 / U1 - (gamma / 2) * vel**2)
        pressure = dens * temp
        Mach_no = vel / np.sqrt(temp)

        total_sim_time += dt

    plt.plot(x, pressure, label=f'Timestep {z}')
    
    # Plot the final results
    plt.title("Pressure")
    plt.xlabel("Nozzle length")
    plt.ylabel("pressure")
    plt.grid(True)
    plt.show()

    plt.plot(x, Mach_no, label=f'Timestep {z}')
    
    # Plot the final results
    plt.title("Mach Number")
    plt.xlabel("Nozzle length")
    plt.ylabel("Mach Number")
    plt.grid(True)
    plt.show()

    plt.plot(x, dens, label=f'Timestep {z}')
    
    # Plot the final results
    plt.title("Density")
    plt.xlabel("Nozzle length")
    plt.ylabel("Density")
    plt.grid(True)
    plt.show()

    plt.plot(x, temp, label=f'Timestep {z}')
    
    # Plot the final results
    plt.title("Temperature")
    plt.xlabel("Nozzle length")
    plt.ylabel("Temperature")
    plt.grid(True)
    plt.show()
    
    return vel, pressure, temp, Mach_no, dens

vel, pressure, temp, Mach_no, dens = conservative_form(n, x, dx, gamma, CFL, nt)