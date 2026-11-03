const form = document.querySelector("#prediction-form");
const submitButton = form.querySelector("button[type='submit']");
const submitText = document.querySelector("#submit-text");
const emptyState = document.querySelector("#empty-state");
const resultState = document.querySelector("#result-state");
const serviceStatus = document.querySelector("#service-status");

async function checkService() {
  try {
    const response = await fetch("/api/health", { headers: { Accept: "application/json" } });
    if (!response.ok) throw new Error("Service unavailable");
    const data = await response.json();
    serviceStatus.textContent = data.dataset_available ? "Connected · Ready" : "Dataset unavailable";
  } catch {
    serviceStatus.textContent = "Connection unavailable";
  }
}

function showError(message) {
  emptyState.classList.remove("hidden");
  resultState.classList.add("hidden");
  emptyState.querySelector("strong").textContent = "Could not run prediction";
  emptyState.querySelector("p").textContent = message;
}

function showResult(data) {
  emptyState.classList.add("hidden");
  resultState.classList.remove("hidden");

  const score = Number(data.model_score || 0);
  document.querySelector("#score-value").textContent = `${score.toFixed(1)}%`;
  document.querySelector("#result-orb").style.background =
    `conic-gradient(var(--mint) ${score * 3.6}deg, rgba(124,228,189,.13) 0deg)`;
  document.querySelector("#prediction-label").textContent = data.label;
  document.querySelector("#prediction-copy").textContent =
    data.prediction === 1
      ? "The model assigned this profile to the positive class in the source dataset."
      : "The model assigned this profile to the negative class in the source dataset.";
  document.querySelector("#target-value").textContent = String(data.prediction);
  document.querySelector("#positive-value").textContent = `${Number(data.positive_class_score).toFixed(1)}%`;
  document.querySelector("#records-value").textContent = String(data.training_rows);
  document.querySelector("#notice-value").textContent = data.notice;
  document.querySelector("#result-time").textContent = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  resultState.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  submitButton.disabled = true;
  submitText.textContent = "Running model…";

  const formData = new FormData(form);
  const payload = Object.fromEntries(formData.entries());
  for (const [key, value] of Object.entries(payload)) {
    payload[key] = key === "oldpeak" ? Number(value) : Number.parseInt(value, 10);
  }

  try {
    const response = await fetch("/api/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || "The prediction request failed.");
    showResult(data);
  } catch (error) {
    showError(error.message || "Please check the entered values and try again.");
  } finally {
    submitButton.disabled = false;
    submitText.textContent = "Run model prediction";
  }
});

document.querySelector("#reset-button").addEventListener("click", () => {
  resultState.classList.add("hidden");
  emptyState.classList.remove("hidden");
  emptyState.querySelector("strong").textContent = "Awaiting input";
  emptyState.querySelector("p").textContent = "Complete the data profile and run the model to see its predicted dataset class.";
  form.scrollIntoView({ behavior: "smooth", block: "start" });
});

checkService();
