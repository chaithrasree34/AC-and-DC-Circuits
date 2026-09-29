# AC-and-DC-Circuits
import math

# ==========================================
# AC AND DC CIRCUIT CALCULATOR
# ==========================================

def dc_circuit():
    print("\n========== DC CIRCUIT ==========")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")

    choice = int(input("Enter choice: "))

    if choice == 1:
        current = float(input("Enter current (A): "))
        resistance = float(input("Enter resistance (Ω): "))

        voltage = current * resistance

        print(f"\nVoltage = {voltage:.2f} V")

    elif choice == 2:
        voltage = float(input("Enter voltage (V): "))
        resistance = float(input("Enter resistance (Ω): "))

        current = voltage / resistance

        print(f"\nCurrent = {current:.2f} A")

    elif choice == 3:
        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (A): "))

        resistance = voltage / current

        print(f"\nResistance = {resistance:.2f} Ω")

    elif choice == 4:
        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (A): "))

        power = voltage * current

        print(f"\nDC Power = {power:.2f} W")

    else:
        print("Invalid choice.")


def series_resistance():
    print("\n========== SERIES RESISTANCE ==========")

    n = int(input("Enter number of resistors: "))

    total = 0

    for i in range(1, n + 1):
        r = float(input(f"Enter R{i} (Ω): "))
        total += r

    print(f"\nTotal Series Resistance = {total:.2f} Ω")


def parallel_resistance():
    print("\n========== PARALLEL RESISTANCE ==========")

    n = int(input("Enter number of resistors: "))

    reciprocal = 0

    for i in range(1, n + 1):
        r = float(input(f"Enter R{i} (Ω): "))

        if r <= 0:
            print("Resistance must be greater than zero.")
            return

        reciprocal += 1 / r

    total = 1 / reciprocal

    print(f"\nTotal Parallel Resistance = {total:.2f} Ω")


def ac_circuit():
    print("\n========== AC CIRCUIT ==========")
    print("1. RLC Series Impedance")
    print("2. AC Current")
    print("3. AC Real Power")
    print("4. AC Apparent Power")
    print("5. AC Reactive Power")

    choice = int(input("Enter choice: "))

    if choice == 1:

        resistance = float(input("Enter resistance R (Ω): "))
        inductance = float(input("Enter inductance L (H): "))
        capacitance = float(input("Enter capacitance C (F): "))
        frequency = float(input("Enter frequency (Hz): "))

        xl = 2 * math.pi * frequency * inductance
        xc = 1 / (2 * math.pi * frequency * capacitance)

        impedance = math.sqrt(
            resistance ** 2 + (xl - xc) ** 2
        )

        print(f"\nInductive Reactance  = {xl:.2f} Ω")
        print(f"Capacitive Reactance = {xc:.2f} Ω")
        print(f"Total Impedance      = {impedance:.2f} Ω")

    elif choice == 2:

        voltage = float(input("Enter AC voltage (V): "))
        impedance = float(input("Enter impedance (Ω): "))

        current = voltage / impedance

        print(f"\nAC Current = {current:.2f} A")

    elif choice == 3:

        voltage = float(input("Enter RMS voltage (V): "))
        current = float(input("Enter RMS current (A): "))
        power_factor = float(input("Enter power factor: "))

        power = voltage * current * power_factor

        print(f"\nReal Power = {power:.2f} W")

    elif choice == 4:

        voltage = float(input("Enter RMS voltage (V): "))
        current = float(input("Enter RMS current (A): "))

        apparent_power = voltage * current

        print(f"\nApparent Power = {apparent_power:.2f} VA")

    elif choice == 5:

        voltage = float(input("Enter RMS voltage (V): "))
        current = float(input("Enter RMS current (A): "))
        power_factor = float(input("Enter power factor: "))

        apparent_power = voltage * current

        reactive_power = apparent_power * math.sqrt(
            1 - power_factor ** 2
        )

        print(f"\nReactive Power = {reactive_power:.2f} VAR")

    else:
        print("Invalid choice.")


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n")
    print("=" * 45)
    print("       AC & DC CIRCUIT CALCULATOR")
    print("=" * 45)

    print("1. DC Circuit")
    print("2. Series Resistance")
    print("3. Parallel Resistance")
    print("4. AC Circuit")
    print("5. Exit")

    main_choice = int(input("\nEnter your choice: "))

    if main_choice == 1:
        dc_circuit()

    elif main_choice == 2:
        series_resistance()

    elif main_choice == 3:
        parallel_resistance()

    elif main_choice == 4:
        ac_circuit()

    elif main_choice == 5:
        print("\nProgram terminated.")
        break

    else:
        print("\nInvalid choice. Please try again.")
