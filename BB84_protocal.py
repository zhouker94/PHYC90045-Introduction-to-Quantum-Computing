import cirq

# The information that Alice want to send to Bob
a_seq = "1001"
print("Alice sents {}".format(a_seq))

# Alice basis (X, Z)
a_basis = "1110"
print("Alice basis {}".format(a_basis))
# Bob basis (X, Z)
b_basis = "0010"
print("Bob basis {}".format(b_basis))

length = 2
qubits = [cirq.GridQubit(i, j) for i in range(length) for j in range(length)]
print(qubits)

circuit = cirq.Circuit()

# set init bits
circuit.append(cirq.X(q) for i, q in enumerate(qubits) if int(a_seq[i]))
# set Alice basis
circuit.append(cirq.H(q) for i, q in enumerate(qubits) if int(a_basis[i]))
# set Bob basis
circuit.append(cirq.H(q) for i, q in enumerate(qubits) if int(b_basis[i]))
print("Circuit:")
print(circuit)

# Measurement
circuit.append(cirq.measure(*qubits, key='x'))

simulator = cirq.google.XmonSimulator()
results = simulator.run(circuit, repetitions=5, qubit_order=qubits)
print("Results:")
print(results.histogram(key='x'))
print("Bob receives (5 times):")
print(results)

