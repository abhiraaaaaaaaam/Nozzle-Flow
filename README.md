# **Subsonic Compressible Flow through a Converging-Diverging Nozzle**

This project simulates the subsonic compressible flow through a converging-diverging (CD) nozzle using MacCormack’s scheme, a widely used explicit finite difference method. The simulation aims to analyze the flow variables (density, pressure, temperature, and velocity) within the nozzle and study their behavior as the flow accelerates from subsonic to sonic conditions.

## **Project Overview**

This project models compressible flow through a CD nozzle, where:
- **MacCormack’s scheme** is used to solve the governing equations.
- **Boundary conditions** and **initial conditions** are carefully set to simulate subsonic flow.
- Flow properties (Mach number, pressure, density, etc.) are visualized to match the analytical results.
- **Area variation** in the nozzle is modeled to allow flow acceleration, as illustrated in the provided graph.

## **Goals**

1. Implement the MacCormack scheme to solve the governing equations for compressible flow.
2. Apply boundary and initial conditions that yield a subsonic-to-sonic transition in the nozzle.
3. Visualize the flow properties and compare them with analytical results to validate the simulation.

## **Files in this Repository**

- **`Subsonic Flow_V2.ipynb`**: Jupyter notebook containing the code implementation for the simulation.
- **`Project_3.pdf`**: Documentation outlining the requirements, equations, and expected graphs.
- **`image.png`**: Reference image of the expected Mach number and pressure profiles for validation.
- **`README.md`**: Project overview and instructions.

## **Installation and Setup**

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
