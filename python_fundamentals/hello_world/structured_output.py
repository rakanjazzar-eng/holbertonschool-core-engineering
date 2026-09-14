#!/usr/bin/env python3
"""Print structured output using derived values."""

pi_value = 3.14159
pi_rounded = round(pi_value, 2)

computation_valid = (2 + 2 == 4)

print("Language: Python")
print("Version: 3")
print(f"Pi approx: {pi_rounded:.2f}")
print(f"Computation valid: {computation_valid}")
