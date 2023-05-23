states_and_capitals = {
    'UP': 'Lucknow',
    'Bihar': 'Patna',
    'Rajasthan': 'Udaipur',
    'Chhattisgarh': 'Raipur',
    'Jharkhand': 'Ranchi'
}

for state, capital in states_and_capitals.items():
    print(f"State: {state}\tCapital: {capital}")

# Correcting the capital of Rajasthan
states_and_capitals['Rajasthan'] = 'Jaipur'

print("\n")

for state, capital in states_and_capitals.items():
    print(f"State: {state}\tCapital: {capital}")
