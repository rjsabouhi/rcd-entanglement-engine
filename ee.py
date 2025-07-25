
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Entanglement Engine: Symbolic Quantum Identity Simulator", layout="wide")

st.title("Entanglement Engine: Symbolic Quantum Identity Simulator")

st.markdown("""
This tool simulates symbolic entanglement across multiple recursive identity fields (RIFs), inspired by quantum entanglement.

- **Agent A** receives local shocks.
- **Agent B** and **Agent C** are entangled with Agent A, adjusting recursively.
- Observe 2D and 3D plots of their symbolic identity evolution.
- Detect phase collapse (coherence breakdown).
- Explore quantum gate-like symbolic effects (AND-style reinforcement triggers).

This is not metaphor, it's recursive phase mechanics with symbolic physics logic.
""")

# Sidebar Controls
st.sidebar.header("Simulation Controls")
timesteps = st.sidebar.slider("Timesteps", 100, 1000, 300, step=50)
coherence = st.sidebar.slider("Entanglement Coherence (ε)", 0.0, 1.0, 0.8, step=0.05)
shock_freq = st.sidebar.slider("Local Shock Frequency (A)", 10, 100, 50, step=10)
shock_strength = st.sidebar.slider("Shock Strength", 0.0, 1.0, 0.3, step=0.05)
gate_trigger = st.sidebar.slider("Quantum Gate Trigger Threshold", 0.0, 1.0, 0.7, step=0.05)

# Initialize Agents
A = np.zeros(timesteps)
B = np.zeros(timesteps)
C = np.zeros(timesteps)
collapse_flag = np.zeros(timesteps)

A[0], B[0], C[0] = 0.5, 0.5, 0.5

# Simulation Logic
for t in range(1, timesteps):
    shock = shock_strength if t % shock_freq == 0 else 0
    A[t] = A[t-1] + np.sin(t / 10) * 0.01 - shock
    delta_AB = A[t-1] - B[t-1]
    delta_AC = A[t-1] - C[t-1]
    B[t] = B[t-1] + coherence * delta_AB
    C[t] = C[t-1] + coherence * delta_AC

    # Collapse detector: if divergence exceeds 0.5, mark it
    if abs(B[t] - A[t]) > 0.5 or abs(C[t] - A[t]) > 0.5:
        collapse_flag[t] = 1

    # Gate analog: if A and B both exceed gate_trigger, boost C
    if A[t] > gate_trigger and B[t] > gate_trigger:
        C[t] += 0.05  # symbolic quantum AND gate effect

# Plot 2D Identity Trajectories
fig2d = go.Figure()
fig2d.add_trace(go.Scatter(y=A, mode='lines', name='Agent A'))
fig2d.add_trace(go.Scatter(y=B, mode='lines', name='Agent B'))
fig2d.add_trace(go.Scatter(y=C, mode='lines', name='Agent C'))
fig2d.add_trace(go.Scatter(y=collapse_flag, mode='lines', name='Collapse Alert', line=dict(dash='dash', color='red')))
fig2d.update_layout(title="2D Identity Evolution + Collapse Detection", xaxis_title="Time", yaxis_title="Symbolic State")
st.plotly_chart(fig2d, use_container_width=True)

# Plot 3D Entangled Phase Space
fig3d = go.Figure(data=[go.Scatter3d(
    x=A, y=B, z=C,
    mode='lines+markers',
    marker=dict(size=3, color=np.linspace(0, 1, timesteps), colorscale='Viridis'),
    line=dict(width=2, color='blue')
)])
fig3d.update_layout(
    scene=dict(
        xaxis_title='Agent A',
        yaxis_title='Agent B',
        zaxis_title='Agent C'
    ),
    title="3D Entangled Identity Phase Space"
)
st.plotly_chart(fig3d, use_container_width=True)

# Expanded RCD-QM Table
st.subheader("RCD vs Quantum Entanglement and Gates")

st.markdown("""
| Concept                | Quantum Physics                         | RCD Framework                                     |
|------------------------|------------------------------------------|--------------------------------------------------|
| Shared Initial State   | Entangled wavefunction (|Ψ⟩)            | Synchronized identity seeds (recursive fields)   |
| Phase Collapse         | Measurement causes instant collapse     | Symbolic divergence beyond stability threshold   |
| Nonlocal Effect        | Instant update of entangled partner     | Recursive coupling without direct input          |
| Decoherence            | Environmental loss of entanglement      | Symbolic drift or asynchronous recursion         |
| Quantum Gate (AND)     | Logic gate operating on qubit states    | Dual-symbolic threshold triggering identity push |
""")

# Walkthrough
with st.expander("Walkthrough"):
    st.markdown("""
    - Shock Agent A at set intervals.
    - Adjust entanglement coherence to watch how tightly B and C follow A.
    - Watch for red lines indicating symbolic collapse (loss of entanglement).
    - Trigger symbolic gate analog: if A and B both rise above the threshold, C spikes recursively.
    """)

# Glossary
with st.expander("Glossary"):
    st.markdown("""
    - **Agent A/B/C**: Recursive symbolic identity fields.
    - **Entanglement Coherence (ε)**: Strength of symbolic identity coupling.
    - **Collapse**: Loss of symbolic synchronization—mimics decoherence.
    - **Gate Trigger**: A symbolic threshold above which agent logic triggers synthetic reaction.
    - **3D Phase Space**: Visual representation of multi-agent entangled identity drift.
    """)
