// ============================================================
// CONFIGURATION
// ============================================================

const API_URL = "http://127.0.0.1:8000/predict";

console.log("✅ script.js loaded");
console.log("🔗 API:", API_URL);


// ============================================================
// HTML ELEMENTS
// ============================================================

const form = document.getElementById("studentForm");
const button = document.getElementById("predictBtn");

const resultSection = document.getElementById("result");
const scoreElement = document.getElementById("score");

const riskBadge = document.getElementById("riskBadge");
const riskMessage = document.getElementById("riskMessage");

const aiResponse = document.getElementById("aiResponse");
const errorElement = document.getElementById("error");

console.log("Form:", form);
console.log("Button:", button);
console.log("Result:", resultSection);


// ============================================================
// SAFETY CHECK
// ============================================================

if (!form) {
    console.error("❌ ERROR: studentForm not found");
}

if (!button) {
    console.error("❌ ERROR: predictBtn not found");
}


// ============================================================
// FORM SUBMIT
// ============================================================

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    console.log("--------------------------------");
    console.log("🚀 FORM SUBMITTED");
    console.log("--------------------------------");


    // ========================================================
    // VALIDATION
    // ========================================================

    if (!form.checkValidity()) {

        console.log("❌ Form validation failed");

        form.reportValidity();

        return;
    }

    console.log("✅ Form validation passed");


    // ========================================================
    // BUTTON LOADING
    // ========================================================

    button.disabled = true;

    button.textContent =
        "Analyzing...";


    hideError();


    // ========================================================
    // GET FORM VALUES
    // ========================================================

    const studentData = {

        age: Number(
            document.getElementById("age").value
        ),

        gender:
            document.getElementById("gender").value,

        country:
            document.getElementById("country").value,

        academic_level:
            document.getElementById("academic_level").value,

        most_used_platform:
            document.getElementById("platform").value,

        purpose_of_use:
            document.getElementById("purpose").value,

        avg_daily_usage_hours: Number(
            document.getElementById("usage").value
        ),

        daily_unlocks: Number(
            document.getElementById("unlocks").value
        ),

        study_hours: Number(
            document.getElementById("study_hours").value
        ),

        physical_activity_hours: Number(
            document.getElementById("activity").value
        ),

        sleep_hours_per_night: Number(
            document.getElementById("sleep").value
        ),

        stress_level:
            document.getElementById("stress").value

    };


    // ========================================================
    // SHOW DATA IN CONSOLE
    // ========================================================

    console.log("📦 Student data:");
    console.table(studentData);


    // ========================================================
    // API REQUEST
    // ========================================================

    try {

        console.log("--------------------------------");
        console.log("📡 SENDING REQUEST");
        console.log("URL:", API_URL);
        console.log("METHOD: POST");
        console.log("--------------------------------");


        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(studentData)

        });


        console.log(
            "📥 Response status:",
            response.status
        );


        // ====================================================
        // READ RESPONSE
        // ====================================================

        const data = await response.json();


        console.log("📥 API response:");
        console.log(data);


        // ====================================================
        // API ERROR
        // ====================================================

        if (!response.ok) {

            let message = "Prediction failed.";

            if (data.detail) {

                if (typeof data.detail === "string") {

                    message = data.detail;

                } else {

                    message =
                        JSON.stringify(data.detail);
                }
            }

            throw new Error(message);
        }


        // ====================================================
        // SCORE
        // ====================================================

        const score =
            Number(data.mental_health_score);


        if (Number.isNaN(score)) {

            throw new Error(
                "Invalid score received from backend."
            );
        }


        console.log(
            "🧠 Mental Health Score:",
            score
        );


        // ====================================================
        // DISPLAY SCORE
        // ====================================================

        animateScore(
            0,
            score,
            1000
        );


        // ====================================================
        // RISK
        // ====================================================

        const risk =
            String(data.risk_category || "")
                .toUpperCase();


        console.log(
            "⚠️ Risk Category:",
            risk
        );


        riskBadge.textContent = risk;


        // Remove old classes

        riskBadge.classList.remove(
            "low",
            "moderate",
            "high"
        );

        riskMessage.classList.remove(
            "low",
            "moderate",
            "high"
        );


        // ====================================================
        // LOW RISK
        // HIGH SCORE = GOOD
        // ====================================================

        if (risk === "LOW") {

            riskBadge.classList.add("low");

            riskMessage.classList.add("low");

            riskMessage.innerHTML = `
                🟢
                <strong>Low Risk — Good wellness range.</strong>
                <br>
                Your predicted score is in the higher range.
                Continue maintaining healthy habits and balance.
            `;
        }


        // ====================================================
        // MODERATE RISK
        // ====================================================

        else if (risk === "MODERATE") {

            riskBadge.classList.add("moderate");

            riskMessage.classList.add("moderate");

            riskMessage.innerHTML = `
                🟡
                <strong>Moderate Risk — Some attention may help.</strong>
                <br>
                Your predicted score is in the middle range.
                Consider improving sleep, physical activity,
                stress management, and healthy screen-time habits.
            `;
        }


        // ====================================================
        // HIGH RISK
        // LOW SCORE = MORE CONCERN
        // ====================================================

        else if (risk === "HIGH") {

            riskBadge.classList.add("high");

            riskMessage.classList.add("high");

            riskMessage.innerHTML = `
                🔴
                <strong>High Risk — Your wellness may need more attention.</strong>
                <br>
                Your predicted score is in the lower range.
                Consider reaching out to a trusted person or
                qualified mental-health professional if concerns persist.
            `;
        }


        // ====================================================
        // AI RESPONSE
        // ====================================================

        const responseText =
            data.ai_response ||
            "No AI guidance was returned.";


        console.log("🤖 AI response:");
        console.log(responseText);


        // ====================================================
        // MARKDOWN RESPONSE
        // ====================================================

        if (
            typeof marked !== "undefined" &&
            typeof DOMPurify !== "undefined"
        ) {

            const html =
                marked.parse(responseText);

            aiResponse.innerHTML =
                DOMPurify.sanitize(html);

        } else {

            aiResponse.textContent =
                responseText;
        }


        // ====================================================
        // SHOW RESULT
        // ====================================================

        resultSection.classList.remove(
            "hidden"
        );


        // ====================================================
        // SCROLL TO RESULT
        // ====================================================

        setTimeout(() => {

            resultSection.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        }, 150);


        console.log("--------------------------------");
        console.log("✅ PREDICTION SUCCESS");
        console.log("--------------------------------");

    }


    // ========================================================
    // CATCH ERROR
    // ========================================================

    catch (error) {

        console.error("--------------------------------");
        console.error("❌ API ERROR");
        console.error(error);
        console.error("--------------------------------");


        showError(
            "Backend request failed.\n\n" +
            "Make sure FastAPI is running at:\n" +
            "http://127.0.0.1:8000\n\n" +
            "Error: " +
            error.message
        );

    }


    // ========================================================
    // RESET BUTTON
    // ========================================================

    finally {

        button.disabled = false;

        button.textContent =
            "Analyze My Mental Health";
    }

});


// ============================================================
// SCORE ANIMATION
// ============================================================

function animateScore(
    start,
    end,
    duration
) {

    const startTime =
        performance.now();


    function update(currentTime) {

        const elapsed =
            currentTime - startTime;


        const progress =
            Math.min(
                elapsed / duration,
                1
            );


        // Smooth ease-out

        const eased =
            1 -
            Math.pow(
                1 - progress,
                3
            );


        const current =
            start +
            (end - start) *
            eased;


        scoreElement.textContent =
            current.toFixed(2);


        if (progress < 1) {

            requestAnimationFrame(
                update
            );
        }
    }


    requestAnimationFrame(
        update
    );
}


// ============================================================
// ERROR FUNCTIONS
// ============================================================

function showError(message) {

    errorElement.textContent =
        message;

    errorElement.classList.remove(
        "hidden"
    );
}


function hideError() {

    errorElement.textContent = "";

    errorElement.classList.add(
        "hidden"
    );
}