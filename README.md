# Numerical Methods, Optimization, and Dynamics

This repository contains implementations of various numerical methods, root-finding algorithms, kinematics optimizations, and dynamical systems simulations. This project was completed as part of a numerical methods course (UMC 202). 

A comprehensive discussion of the mathematical theory, derivations, and convergence analysis can be found in the **[Full_Technical_Report.pdf](./Full_Technical_Report.pdf)**.

## Project Structure

### 1. Root Finding & Convergence (`1_Root_Finding_Convergence`)
Implemented root-finding algorithms to find complex roots of polynomials. 
- **Method Used**: Muller's Method.
- **Objective**: Demonstrate quadratic convergence for complex roots without requiring derivative calculations.

### 2. Fractals and Chaos (`2_Fractals_and_Chaos`)
Visualized and analyzed dynamical systems that exhibit chaotic behavior and fractal geometry.
- **Methods Used**: Mandelbrot set generation, Logistic Map bifurcation diagrams, Lyapunov exponent calculation, and Newton fractals.
- **Objective**: Explore the sensitivity to initial conditions and the transition to chaos in non-linear dynamics.

### 3. Robotic Arm Kinematics (`3_Robotic_Arm_Kinematics`)
Solved the Inverse Kinematics problem for a robotic arm to trace specific paths.
- **Methods Used**: Gradient Descent and Gradient Descent with Momentum.
- **Objective**: Optimize joint angles to minimize the error between the end-effector and the target trajectory.

### 4. Fourier Shape Reconstruction (`4_Fourier_Shape_Reconstruction`)
Reconstructed complex 2D shapes (like the letter "S") using parametric equations and Fourier series.
- **Methods Used**: Trapezoidal rule for numerical integration to compute Fourier coefficients.
- **Objective**: Show how truncated Fourier series can approximate closed curves in a 2D plane.

### 5. Harmonic Oscillator Simulation (`5_Harmonic_Oscillator_RK4`)
Numerically solved second-order ordinary differential equations governing harmonic oscillators.
- **Methods Used**: Euler Method and Runge-Kutta 4th Order (RK4).
- **Objective**: Compare the stability, accuracy, and energy conservation of different numerical integration schemes over time.

## Running the Code

The project relies on standard Python libraries such as `numpy`, `matplotlib`, and `jupyter`. 

Most modules are provided as Jupyter Notebooks (`.ipynb`) for interactive exploration, while some algorithms are written in standard Python scripts (`.py`).

```bash
# Clone the repository
git clone <your-repo-url>
cd numerical-optimization-and-dynamics

# Install dependencies if necessary
pip install numpy matplotlib jupyter

# Run a script
python 1_Root_Finding_Convergence/muller_root.py
```
