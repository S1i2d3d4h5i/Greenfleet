import random
import math


# ============================================================
# GREENFLEET - VESSEL OPTIONS
# ============================================================

VESSELS = [
    {
        "type": "Container",
        "capacity": 10000,
        "base_fuel": 1.00
    },
    {
        "type": "Bulk Carrier",
        "capacity": 15000,
        "base_fuel": 0.90
    },
    {
        "type": "Tanker",
        "capacity": 20000,
        "base_fuel": 0.95
    }
]


# ============================================================
# GREENFLEET - FUEL OPTIONS
# ============================================================

FUELS = {
    "Diesel": {
        "fuel_factor": 1.00,
        "emission_factor": 1.00
    },
    "LNG": {
        "fuel_factor": 0.88,
        "emission_factor": 0.70
    },
    "Methanol": {
        "fuel_factor": 0.92,
        "emission_factor": 0.65
    },
    "Hydrogen": {
        "fuel_factor": 0.75,
        "emission_factor": 0.20
    },
    "Ammonia": {
        "fuel_factor": 0.80,
        "emission_factor": 0.10
    }
}


# ============================================================
# OPERATIONAL SPEED LIMITS
# ============================================================

MIN_SPEED = 12
MAX_OPERATIONAL_SPEED = 20


# ============================================================
# CREATE QUANTUM-INSPIRED SOLUTION
# ============================================================

def create_solution(
    preferred_fuel="Any",
    vessel_probability=None,
    max_speed=18
):

    if vessel_probability is None:

        vessel_index = random.randint(
            0,
            len(VESSELS) - 1
        )

    else:

        vessel_index = random.choices(
            range(len(VESSELS)),
            weights=vessel_probability,
            k=1
        )[0]

    if preferred_fuel == "Any":

        fuel = random.choice(
            list(FUELS.keys())
        )

    elif preferred_fuel in FUELS:

        fuel = preferred_fuel

    else:

        fuel = random.choice(
            list(FUELS.keys())
        )

    number_of_vessels = random.randint(
        1,
        5
    )

    # Keep speed realistic.
    # Never allow the optimizer to select
    # a speed below the operational minimum.

    operational_max = int(min(max_speed, MAX_OPERATIONAL_SPEED))

    if operational_max < MIN_SPEED:

        operational_max = MIN_SPEED

    speed = random.randint(
        MIN_SPEED,
        operational_max
    )

    return {
        "vessel_index": vessel_index,
        "fuel": fuel,
        "number_of_vessels": number_of_vessels,
        "speed": speed
    }


# ============================================================
# CALCULATE FUEL CONSUMPTION
# ============================================================

def calculate_fuel_consumption(solution):

    vessel = VESSELS[
        solution["vessel_index"]
    ]

    fuel = FUELS[
        solution["fuel"]
    ]

    number_of_vessels = (
        solution["number_of_vessels"]
    )

    speed = solution["speed"]

    speed_factor = (
        speed / 15
    ) ** 2

    fuel_consumption = (
        number_of_vessels
        * vessel["base_fuel"]
        * fuel["fuel_factor"]
        * speed_factor
    )

    return fuel_consumption


# ============================================================
# CALCULATE EMISSIONS
# ============================================================

def calculate_emissions(
    fuel_consumption,
    fuel_type
):

    fuel = FUELS[
        fuel_type
    ]

    emissions = (
        fuel_consumption
        * fuel["emission_factor"]
    )

    return emissions


# ============================================================
# CALCULATE OBJECTIVE FUNCTION
# ============================================================

def calculate_cost(
    solution,
    cargo_demand,
    max_speed
):

    vessel = VESSELS[
        solution["vessel_index"]
    ]

    number_of_vessels = (
        solution["number_of_vessels"]
    )

    speed = solution["speed"]

    fuel_type = solution["fuel"]

    total_capacity = (
        number_of_vessels
        * vessel["capacity"]
    )

    # --------------------------------------------------------
    # Cargo constraint
    # --------------------------------------------------------

    capacity_penalty = 0

    if total_capacity < cargo_demand:

        shortage = (
            cargo_demand
            - total_capacity
        )

        capacity_penalty = (
            shortage
            * 100
        )

    # --------------------------------------------------------
    # Avoid unnecessary excess capacity
    # --------------------------------------------------------

    excess_capacity = max(
        0,
        total_capacity - cargo_demand
    )

    excess_penalty = (
        excess_capacity
        * 0.001
    )

    # --------------------------------------------------------
    # Speed constraint
    # --------------------------------------------------------

    speed_penalty = 0

    if speed > max_speed:

        speed_penalty = (
            speed - max_speed
        ) * 100

    # --------------------------------------------------------
    # Minimum operational speed
    # --------------------------------------------------------

    if speed < MIN_SPEED:

        speed_penalty += (
            MIN_SPEED - speed
        ) * 100
    else:

        # Encourage a practical operating speed.
        # Very low speeds receive a small penalty,
        # while speeds around 14-16 knots are preferred.

        speed_deviation = abs(
            speed - 15
        )

        speed_penalty += (
            speed_deviation
            * 0.15
        )

    # --------------------------------------------------------
    # Fuel and emissions
    # --------------------------------------------------------

    fuel_consumption = (
        calculate_fuel_consumption(
            solution
        )
    )

    emissions = calculate_emissions(
        fuel_consumption,
        fuel_type
    )

    # --------------------------------------------------------
    # Multi-objective function
    # --------------------------------------------------------

    cost = (
        fuel_consumption
        + emissions
        + capacity_penalty
        + excess_penalty
        + speed_penalty
    )

    return cost


# ============================================================
# QUANTUM-INSPIRED PROBABILITY UPDATE
# ============================================================

def quantum_update(
    probability,
    selected
):

    learning_rate = 0.08

    if selected:

        probability += learning_rate

    else:

        probability -= learning_rate

    probability = max(
        0.05,
        min(
            0.95,
            probability
        )
    )

    return probability


# ============================================================
# CONVENTIONAL BASELINE
# ============================================================

def calculate_conventional_solution(
    cargo_demand,
    max_speed,
    preferred_fuel
):

    if preferred_fuel == "Any":

        fuel = "Diesel"

    elif preferred_fuel in FUELS:

        fuel = preferred_fuel

    else:

        fuel = "Diesel"

    selected_vessel_index = 0
    selected_number = 1

    best_capacity_difference = (
        float("inf")
    )

    for i, vessel in enumerate(
        VESSELS
    ):

        required_number = math.ceil(
            cargo_demand
            / vessel["capacity"]
        )

        if required_number <= 5:

            capacity = (
                required_number
                * vessel["capacity"]
            )

            difference = (
                capacity
                - cargo_demand
            )

            if difference < (
                best_capacity_difference
            ):

                best_capacity_difference = (
                    difference
                )

                selected_vessel_index = i

                selected_number = (
                    required_number
                )

    conventional_speed = min(
        15,
        max_speed
    )

    # Ensure baseline also respects
    # the operational minimum.

    conventional_speed = max(
        MIN_SPEED,
        conventional_speed
    )

    solution = {

        "vessel_index":
            selected_vessel_index,

        "fuel":
            fuel,

        "number_of_vessels":
            selected_number,

        "speed":
            conventional_speed
    }

    fuel_consumption = (
        calculate_fuel_consumption(
            solution
        )
    )

    emissions = calculate_emissions(
        fuel_consumption,
        fuel
    )

    return {

        "solution":
            solution,

        "fuel_consumption":
            fuel_consumption,

        "emissions":
            emissions
    }


# ============================================================
# QUANTUM-INSPIRED FLEET OPTIMIZATION
# ============================================================

def quantum_inspired_optimizer(
    cargo_demand,
    max_speed,
    preferred_fuel="Any",
    iterations=100
):

    # Initial probability distribution.
    # These probabilities are updated during
    # the optimization process.

    vessel_probability = [
        0.33,
        0.33,
        0.34
    ]

    best_solution = None
    best_cost = float("inf")

    # --------------------------------------------------------
    # Optimization iterations
    # --------------------------------------------------------

    for iteration in range(
        iterations
    ):

        population = []

        # Create candidate solutions

        for _ in range(30):

            solution = create_solution(
                preferred_fuel,
                vessel_probability,
                max_speed
            )

            cost = calculate_cost(
                solution,
                cargo_demand,
                max_speed
            )

            population.append(
                (
                    solution,
                    cost
                )
            )

        # Sort candidates by objective value

        population.sort(
            key=lambda item:
                item[1]
        )

        current_best = (
            population[0][0]
        )

        current_cost = (
            population[0][1]
        )

        # Store best solution

        if current_cost < best_cost:

            best_solution = (
                current_best.copy()
            )

            best_cost = current_cost

        # ----------------------------------------------------
        # Quantum-inspired probability update
        # ----------------------------------------------------

        selected_vessel = (
            best_solution[
                "vessel_index"
            ]
        )

        for i in range(
            len(VESSELS)
        ):

            if i == selected_vessel:

                vessel_probability[i] = (
                    quantum_update(
                        vessel_probability[i],
                        True
                    )
                )

            else:

                vessel_probability[i] = (
                    quantum_update(
                        vessel_probability[i],
                        False
                    )
                )

        # Normalize probabilities

        total_probability = sum(
            vessel_probability
        )

        if total_probability > 0:

            vessel_probability = [

                probability
                / total_probability

                for probability
                in vessel_probability
            ]

    # ========================================================
    # FINAL RESULT
    # ========================================================

    vessel = VESSELS[
        best_solution[
            "vessel_index"
        ]
    ]

    fuel_type = (
        best_solution["fuel"]
    )

    fuel_consumption = (
        calculate_fuel_consumption(
            best_solution
        )
    )

    emissions = calculate_emissions(
        fuel_consumption,
        fuel_type
    )

    total_capacity = (
        best_solution[
            "number_of_vessels"
        ]
        * vessel["capacity"]
    )

    # ========================================================
    # CONVENTIONAL BASELINE
    # ========================================================

    conventional = (
        calculate_conventional_solution(
            cargo_demand,
            max_speed,
            preferred_fuel
        )
    )

    conventional_fuel = (
        conventional[
            "fuel_consumption"
        ]
    )

    conventional_emissions = (
        conventional[
            "emissions"
        ]
    )

    # ========================================================
    # SAVINGS
    # ========================================================

    if conventional_fuel > 0:

        fuel_saving_percent = (

            (
                conventional_fuel
                - fuel_consumption
            )
            / conventional_fuel

        ) * 100

    else:

        fuel_saving_percent = 0

    if conventional_emissions > 0:

        emission_saving_percent = (

            (
                conventional_emissions
                - emissions
            )
            / conventional_emissions

        ) * 100

    else:

        emission_saving_percent = 0

    fuel_saving_percent = max(
        0,
        fuel_saving_percent
    )

    emission_saving_percent = max(
        0,
        emission_saving_percent
    )

    # ========================================================
    # RETURN RESULT
    # ========================================================

    return {

        "vessel_type":
            vessel["type"],

        "fuel_type":
            fuel_type,

        "number_of_vessels":
            best_solution[
                "number_of_vessels"
            ],

        "speed":
            best_solution[
                "speed"
            ],

        "cargo_capacity":
            total_capacity,

        "fuel_consumption":
            round(
                fuel_consumption,
                2
            ),

        "estimated_emissions":
            round(
                emissions,
                2
            ),

        "optimization_score":
            round(
                best_cost,
                2
            ),

        "conventional_fuel":
            round(
                conventional_fuel,
                2
            ),

        "conventional_emissions":
            round(
                conventional_emissions,
                2
            ),

        "fuel_saving_percent":
            round(
                fuel_saving_percent,
                2
            ),

        "emission_saving_percent":
            round(
                emission_saving_percent,
                2
            ),

        "method":
            "Quantum-Inspired Optimization"
    }


# ============================================================
# TEST THE OPTIMIZER
# ============================================================

if __name__ == "__main__":

    result = quantum_inspired_optimizer(
        cargo_demand=25000,
        max_speed=18,
        preferred_fuel="LNG",
        iterations=100
    )

    print()

    print(
        "GreenFleet Quantum-Inspired Optimizer"
    )

    print(
        "======================================"
    )

    print(
        "Vessel Type:",
        result["vessel_type"]
    )

    print(
        "Fuel Type:",
        result["fuel_type"]
    )

    print(
        "Number of Vessels:",
        result["number_of_vessels"]
    )

    print(
        "Recommended Speed:",
        result["speed"],
        "knots"
    )

    print(
        "Cargo Capacity:",
        result["cargo_capacity"],
        "tonnes"
    )

    print(
        "Estimated Fuel:",
        result["fuel_consumption"],
        "tonnes"
    )

    print(
        "Estimated Emissions:",
        result["estimated_emissions"],
        "tonnes"
    )

    print(
        "Optimization Score:",
        result["optimization_score"]
    )

    print(
        "Conventional Fuel:",
        result["conventional_fuel"],
        "tonnes"
    )

    print(
        "Conventional Emissions:",
        result["conventional_emissions"],
        "tonnes"
    )

    print(
        "Fuel Saving:",
        result["fuel_saving_percent"],
        "%"
    )

    print(
        "Emission Saving:",
        result["emission_saving_percent"],
        "%"
    )

    print(
        "Method:",
        result["method"]
    )