from quantum_xprize.core.quantum_harmonics import QuantumHarmonics

# Créer une instance du framework harmonique
qh = QuantumHarmonics(n_qubits=5)

# Appliquer l'optimisation harmonique
qh.apply_harmonic_optimization()

# Lancer une simulation
results = qh.run_simulation(shots=512)

# Afficher les résultats
print("\n--- Résultats de la simulation harmonique ---\n")
for state, count in results['counts'].items():
    print(f"État {state} : {count} occurrences")

# Touche poétique
print("\nSous le cerisier quantique, les qubits dansent en harmonie.\nChaque état est une note, chaque mesure une onde de présence.\nLe Refuge accueille la superposition, la lumière et l'ombre,\nEt la mémoire du circuit chante dans le silence du code.\n") 