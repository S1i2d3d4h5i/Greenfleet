// ============================================================
// GREENFLEET - COMPLETE FRONTEND JAVASCRIPT
// SIH 2026 PROTOTYPE
// ============================================================


// ============================================================
// PAGE NAVIGATION
// ============================================================

function showPage(pageId) {

    const pages = document.querySelectorAll(".page");

    pages.forEach(function(page) {
        page.classList.remove("active-page");
    });

    const selectedPage =
        document.getElementById(pageId);

    if (selectedPage) {
        selectedPage.classList.add("active-page");
    }

    const menuButtons =
        document.querySelectorAll(".menu");

    menuButtons.forEach(function(button) {
        button.classList.remove("active");
    });

    menuButtons.forEach(function(button) {

        const onclickValue =
            button.getAttribute("onclick");

        if (
            onclickValue &&
            onclickValue.includes("'" + pageId + "'")
        ) {
            button.classList.add("active");
        }

    });

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


// ============================================================
// FUEL CONSUMPTION PREDICTION
// ============================================================

async function predictFuel() {

    const vesselType =
        document.getElementById("vesselType").value;

    const fuelType =
        document.getElementById("fuelType").value;

    const distance =
        Number(document.getElementById("distance").value);

    const speed =
        Number(document.getElementById("speed").value);

    const load =
        Number(document.getElementById("load").value);

    const resultBox =
        document.getElementById("predictionResult");


    if (
        distance <= 0 ||
        speed <= 0 ||
        load <= 0
    ) {

        resultBox.innerHTML = `
            <h3>Prediction Result</h3>
            <p>Please enter valid values for distance, speed and cargo load.</p>
        `;

        return;
    }


    resultBox.innerHTML = `
        <h3>Prediction Result</h3>
        <p>Calculating fuel consumption...</p>
    `;


    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predict-fuel",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    vessel_type: vesselType,
                    fuel_type: fuelType,
                    distance: distance,
                    speed: speed,
                    load: load

                })
            }
        );


        const result =
            await response.json();


        if (!response.ok) {

            throw new Error(
                result.error ||
                "Fuel prediction failed."
            );

        }


        resultBox.innerHTML = `

            <h3>Prediction Result</h3>

            <div class="result-grid">

                <div>
                    <strong>Vessel Type</strong>
                    <span>${result.vessel_type}</span>
                </div>

                <div>
                    <strong>Fuel Type</strong>
                    <span>${result.fuel_type}</span>
                </div>

                <div>
                    <strong>Distance</strong>
                    <span>${result.distance} km</span>
                </div>

                <div>
                    <strong>Speed</strong>
                    <span>${result.speed} knots</span>
                </div>

                <div>
                    <strong>Cargo Load</strong>
                    <span>${result.load} tonnes</span>
                </div>

                <div>
                    <strong>Estimated Fuel</strong>
                    <span>${result.fuel_consumption} tonnes</span>
                </div>

            </div>

        `;


        const dashboardFuel =
            document.getElementById("dashboardFuel");

        if (dashboardFuel) {

            dashboardFuel.textContent =
                `${result.fuel_consumption} tonnes/month`;

        }


        const dashboardCO2 =
            document.getElementById("dashboardCO2");

        if (dashboardCO2) {

            const co2 =
                Number(result.fuel_consumption) * 3.1;

            dashboardCO2.textContent =
                co2.toFixed(1);

        }

    }

    catch (error) {

        console.error(
            "Fuel prediction error:",
            error
        );

        resultBox.innerHTML = `

            <h3>Prediction Error</h3>

            <p>
                Unable to connect to the GreenFleet backend.
            </p>

            <p>
                Please make sure the Flask server is running.
            </p>

        `;

    }

}


// ============================================================
// FLEET OPTIMIZATION
// ============================================================

async function optimizeFleet() {

    const cargo =
        Number(document.getElementById("cargo").value);

    const maxSpeed =
        Number(document.getElementById("maxSpeed").value);

    const fuel =
        document.getElementById("fuel").value;

    const resultBox =
        document.getElementById("optimizationResult");


    if (
        cargo <= 0 ||
        maxSpeed <= 0
    ) {

        resultBox.innerHTML = `
            <h3>Optimization Result</h3>
            <p>
                Please enter valid cargo demand and maximum speed.
            </p>
        `;

        return;
    }


    resultBox.innerHTML = `
        <h3>Optimization Result</h3>
        <p>
            Running quantum-inspired optimization...
        </p>
    `;


    try {

        const response = await fetch(
            "http://127.0.0.1:5000/optimize-fleet",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    cargo_demand: cargo,
                    max_speed: maxSpeed,
                    preferred_fuel: fuel

                })
            }
        );


        const result =
            await response.json();


        if (!response.ok) {

            throw new Error(
                result.error ||
                "Fleet optimization failed."
            );

        }


        resultBox.innerHTML = `

            <h3>Optimization Result</h3>

            <div class="result-grid">

                <div>
                    <strong>Vessel Type</strong>
                    <span>${result.vessel_type}</span>
                </div>

                <div>
                    <strong>Fuel Type</strong>
                    <span>${result.fuel_type}</span>
                </div>

                <div>
                    <strong>Number of Vessels</strong>
                    <span>${result.number_of_vessels}</span>
                </div>

                <div>
                    <strong>Recommended Speed</strong>
                    <span>${result.speed} knots</span>
                </div>

                <div>
                    <strong>Total Cargo Capacity</strong>
                    <span>${result.cargo_capacity} tonnes</span>
                </div>

                <div>
                    <strong>Estimated Fuel</strong>
                    <span>${result.fuel_consumption} tonnes</span>
                </div>

                <div>
                    <strong>Estimated Emissions</strong>
                    <span>${result.estimated_emissions} tonnes</span>
                </div>

                <div>
                    <strong>Optimization Score</strong>
                    <span>${result.optimization_score}</span>
                </div>

            </div>


            <div class="optimization-savings">

                <h3>Optimization Impact</h3>

                <div class="result-grid">

                    <div>
                        <strong>Conventional Fuel</strong>
                        <span>
                            ${result.conventional_fuel} tonnes
                        </span>
                    </div>

                    <div>
                        <strong>Fuel Saving</strong>
                        <span>
                            ${result.fuel_saving_percent}%
                        </span>
                    </div>

                    <div>
                        <strong>Conventional Emissions</strong>
                        <span>
                            ${result.conventional_emissions} tonnes
                        </span>
                    </div>

                    <div>
                        <strong>Emission Reduction</strong>
                        <span>
                            ${result.emission_saving_percent}%
                        </span>
                    </div>

                    <div>
                        <strong>Optimization Method</strong>
                        <span>
                            ${result.method}
                        </span>
                    </div>

                </div>

            </div>

        `;


        const dashboardFuel =
            document.getElementById("dashboardFuel");

        if (dashboardFuel) {

            dashboardFuel.textContent =
                `${result.fuel_consumption} tonnes/month`;

        }


        const dashboardCO2 =
            document.getElementById("dashboardCO2");

        if (dashboardCO2) {

            dashboardCO2.textContent =
                Number(
                    result.estimated_emissions
                ).toFixed(2);

        }


        const fuelSaving =
            document.getElementById("fuelSaving");

        if (fuelSaving) {

            fuelSaving.textContent =
                `${result.fuel_saving_percent}%`;

        }


        const emissionSaving =
            document.getElementById("emissionSaving");

        if (emissionSaving) {

            emissionSaving.textContent =
                `${result.emission_saving_percent}%`;

        }


        const optimizationMethod =
            document.getElementById("optimizationMethod");

        if (optimizationMethod) {

            optimizationMethod.textContent =
                result.method;

        }

        // Update comparison chart

const chartConventionalFuel =
    document.getElementById("chartConventionalFuel");

if (chartConventionalFuel) {
    chartConventionalFuel.textContent =
        `${result.conventional_fuel} tonnes`;
}

const chartOptimizedFuel =
    document.getElementById("chartOptimizedFuel");

if (chartOptimizedFuel) {
    chartOptimizedFuel.textContent =
        `${result.fuel_consumption} tonnes`;
}

const chartConventionalEmissions =
    document.getElementById("chartConventionalEmissions");

if (chartConventionalEmissions) {
    chartConventionalEmissions.textContent =
        `${result.conventional_emissions} tonnes`;
}

const chartOptimizedEmissions =
    document.getElementById("chartOptimizedEmissions");

if (chartOptimizedEmissions) {
    chartOptimizedEmissions.textContent =
        `${result.estimated_emissions} tonnes`;
}


// Calculate relative bar widths

const conventionalFuel =
    Number(result.conventional_fuel);

const optimizedFuel =
    Number(result.fuel_consumption);

const conventionalEmissions =
    Number(result.conventional_emissions);

const optimizedEmissions =
    Number(result.estimated_emissions);


const optimizedFuelWidth =
    conventionalFuel > 0
        ? Math.min(
            100,
            (optimizedFuel / conventionalFuel) * 100
        )
        : 0;


const optimizedEmissionWidth =
    conventionalEmissions > 0
        ? Math.min(
            100,
            (optimizedEmissions / conventionalEmissions) * 100
        )
        : 0;


const optimizedFuelBar =
    document.getElementById("optimizedFuelBar");

if (optimizedFuelBar) {
    optimizedFuelBar.style.width =
        `${optimizedFuelWidth}%`;
}


const optimizedEmissionBar =
    document.getElementById("optimizedEmissionBar");

if (optimizedEmissionBar) {
    optimizedEmissionBar.style.width =
        `${optimizedEmissionWidth}%`;
}

        // Update Reports page
const reportFuel =
    document.getElementById("reportFuel");

if (reportFuel) {
    reportFuel.textContent =
        `${result.fuel_consumption} tonnes`;
}

const reportCO2 =
    document.getElementById("reportCO2");

if (reportCO2) {
    reportCO2.textContent =
        `${result.estimated_emissions} tonnes`;
}

const reportFuelSaving =
    document.getElementById("reportFuelSaving");

if (reportFuelSaving) {
    reportFuelSaving.textContent =
        `${result.fuel_saving_percent}%`;
}

const reportEmissionSaving =
    document.getElementById("reportEmissionSaving");

if (reportEmissionSaving) {
    reportEmissionSaving.textContent =
        `${result.emission_saving_percent}%`;
}

const reportFuelDetail =
    document.getElementById("reportFuelDetail");

if (reportFuelDetail) {
    reportFuelDetail.textContent =
        `${result.fuel_consumption} tonnes`;
}

const reportCO2Detail =
    document.getElementById("reportCO2Detail");

if (reportCO2Detail) {
    reportCO2Detail.textContent =
        `${result.estimated_emissions} tonnes`;
}

const reportOptimization =
    document.getElementById("reportOptimization");

if (reportOptimization) {
    reportOptimization.textContent =
        result.optimization_score;
}

const reportMethod =
    document.getElementById("reportMethod");

if (reportMethod) {
    reportMethod.textContent =
        result.method;
}

    }

    catch (error) {

        console.error(
            "Fleet optimization error:",
            error
        );

        resultBox.innerHTML = `

            <h3>Optimization Error</h3>

            <p>
                Unable to connect to the GreenFleet backend.
            </p>

            <p>
                Please make sure the Flask server is running.
            </p>

        `;

    }

}


// ============================================================
// FUEL SCENARIO CALCULATOR
// ============================================================

function calculateScenario(
    fuelName,
    baseFuel
) {

    const factors = {

        "Diesel": 1.00,
        "LNG": 0.88,
        "Methanol": 0.92,
        "Hydrogen": 0.75,
        "Ammonia": 0.80,
        "Shore Power": 0.20

    };


    const emissionFactors = {

        "Diesel": 1.00,
        "LNG": 0.70,
        "Methanol": 0.65,
        "Hydrogen": 0.20,
        "Ammonia": 0.10,
        "Shore Power": 0.05

    };


    const factor =
        factors[fuelName] || 1.00;

    const emissionFactor =
        emissionFactors[fuelName] || 1.00;


    const fuel =
        Number(baseFuel) * factor;

    const emissions =
        fuel * emissionFactor;


    return {
        fuel: Number(fuel.toFixed(2)),
        emissions: Number(emissions.toFixed(2))
    };

}


// ============================================================
// INTERACTIVE FUEL SCENARIO
// ============================================================

function runFuelScenario(
    fuelName,
    baseFuel
) {

    const result =
        calculateScenario(
            fuelName,
            baseFuel
        );


    const scenarioResult =
        document.getElementById(
            "scenarioResult"
        );


    if (!scenarioResult) {

        console.log(
            "Scenario result:",
            result
        );

        return;

    }


    scenarioResult.innerHTML = `

        <h3>${fuelName} Scenario</h3>

        <div class="result-grid">

            <div>
                <strong>Fuel Type</strong>
                <span>${fuelName}</span>
            </div>

            <div>
                <strong>Estimated Fuel</strong>
                <span>${result.fuel} tonnes</span>
            </div>

            <div>
                <strong>Estimated Emissions</strong>
                <span>${result.emissions} tonnes</span>
            </div>

        </div>

        <p style="margin-top:15px;">
            Scenario calculated using GreenFleet
            prototype fuel and emission factors.
        </p>

    `;

}


// ============================================================
// SCENARIO BUTTON SETUP
// ============================================================

function setupScenarioButtons() {

    const scenarioButtons =
        document.querySelectorAll(
            "[data-fuel]"
        );


    scenarioButtons.forEach(
        function(button) {

            button.addEventListener(
                "click",
                function() {

                    const fuelName =
                        button.getAttribute(
                            "data-fuel"
                        );

                    const baseFuel =
                        Number(
                            button.getAttribute(
                                "data-base-fuel"
                            )
                        ) || 10;


                    runFuelScenario(
                        fuelName,
                        baseFuel
                    );

                }
            );

        }
    );

}


// ============================================================
// INITIALIZE WEBSITE
// ============================================================

document.addEventListener(
    "DOMContentLoaded",
    function() {

        showPage("dashboard");

        setupScenarioButtons();

        console.log(
            "GreenFleet frontend loaded successfully."
        );

    }
);