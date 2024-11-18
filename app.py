import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title and description
st.title("Fibonacci Numbers and Signal Waves")
st.write("""
This application generates Fibonacci numbers and visualizes them along with signal waveforms 
(Sine and Cosine waves).
""")

# Function to generate Fibonacci numbers
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[:n]

# Input for the number of Fibonacci numbers to generate
n = st.number_input("Enter the number of Fibonacci numbers to generate:", min_value=1, max_value=1000, value=10, step=1)

# Generate Fibonacci sequence
fib_sequence = generate_fibonacci(n)

# Display Fibonacci numbers
st.write(f"Here is the sequence of the first {n} Fibonacci numbers:")
st.write(fib_sequence)

# Plot Fibonacci numbers as a line chart
st.subheader("Fibonacci Numbers Line Graph")
st.line_chart(fib_sequence)

# Generate signal waves
x = np.linspace(0, 2 * np.pi, 100)
sine_wave = np.sin(x)
cosine_wave = np.cos(x)

# Plot Fibonacci numbers and signal waves together
st.subheader("Fibonacci Numbers with Signal Waves")

# Create a plot using Matplotlib
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(range(n), fib_sequence, label="Fibonacci Numbers", marker="o")
ax.plot(x, sine_wave * max(fib_sequence) / 2, label="Sine Wave", linestyle="--")
ax.plot(x, cosine_wave * max(fib_sequence) / 2, label="Cosine Wave", linestyle="--")

ax.set_title("Fibonacci Numbers and Signal Waves")
ax.set_xlabel("Index / Time")
ax.set_ylabel("Amplitude")
ax.legend()

# Display the plot
st.pyplot(fig)
