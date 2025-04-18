function generatePlan() {
  const destination = document.getElementById("destination").value.trim();
  const duration = document.getElementById("duration").value.trim();
  const budget = document.getElementById("budget").value.trim();
  const checkboxes = document.querySelectorAll(".checkboxes input[type='checkbox']");
  const travelStyles = Array.from(checkboxes)
                            .filter(cb => cb.checked)
                            .map(cb => cb.value);

  const resultDiv = document.getElementById("result");

  // Show inline error instead of alert
  if (!destination || !duration || !budget) {
    resultDiv.innerHTML = `<p class="error" style="color: red;">❌ Please fill in all the required fields!</p>`;
    return;
  }

  resultDiv.innerHTML = "<p>⏳ Generating your travel plan...</p>";

  fetch("/api/generate-plan", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      destination,
      duration,
      budget,
      travelStyles
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.plan) {
      resultDiv.innerHTML = marked.parse(data.plan);
    } else {
      resultDiv.innerHTML = `<p class="error" style="color: red;">❌ Error: ${data.error}</p>`;
    }
  })
  .catch(error => {
    resultDiv.innerHTML = `<p class="error" style="color: red;">❌ Request failed: ${error}</p>`;
  });
}

// 🔒 Enable/Disable button based on input
function setupInputValidation() {
  const destinationInput = document.getElementById("destination");
  const durationInput = document.getElementById("duration");
  const budgetInput = document.getElementById("budget");
  const generateBtn = document.getElementById("generateBtn");

  function checkInputs() {
    const destination = destinationInput.value.trim();
    const duration = durationInput.value.trim();
    const budget = budgetInput.value.trim();

    generateBtn.disabled = !(destination && duration && budget);
  }

  destinationInput.addEventListener("input", checkInputs);
  durationInput.addEventListener("input", checkInputs);
  budgetInput.addEventListener("input", checkInputs);

  // Initial check
  checkInputs();
}

// 🔁 Call on page load
window.addEventListener("DOMContentLoaded", setupInputValidation);
