# **Quasi 1D Compressible Flow through a Converging-Diverging Nozzle**

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

- **`Subsonic Flow_V2.py`**: Python file containing the code implementation for the subsonic flow simulation.
- **`Subsonic- Supersonic.py`**: Python file containing the code implementation for the subsonic-supersonic flow simulation.
- **`README.md`**: Project overview and instructions.

## **Installation and Setup**

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/Nozzle-Flow.git
   cd Nozzle-Flow

2. **Install dependencies: Ensure that Python and Jupyter Notebook are installed. Use pip to install required libraries.**:
   ```bash
   pip install numpy matplotlib

## **Usage**
1. Open the file Subsonic Flow_V2.py or Subsonic- Supersonic.py file.
2. Run the file
3. The code will output plots for pressure, density, temperature, and Mach number along the nozzle length.

## **Explanation of Key Components**
1. **MacCormack Scheme**
The MacCormack scheme is a two-step predictor-corrector method used for solving hyperbolic partial differential equations:

**Predictor Step**: Forward differencing in space.
**Corrector Step**: Backward differencing in space.

2. **Nozzle Area Variation**
The nozzle area is specified as: 
𝐴(𝑥)=1+2.2(𝑥−1.5)2A(x)=1+2.2(x−1.5)2
This shape causes the flow to accelerate in the converging section and decelerate in the diverging section.

3. **Boundary Conditions**
The simulation implements specific boundary conditions for velocity, density, and pressure at the inlet and outlet. These are set up to match the isentropic solutions for subsonic flow through the nozzle.

4. **Initial Conditions**
The initial state assumes uniform conditions across the nozzle. The values are adjusted in the first few steps to start the acceleration process.
