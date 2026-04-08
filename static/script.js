let score = 0;
let total = 0;
let streak = 0;
let currentAnswer = null;
let answered = false;

function updateScoreboard() {
    document.getElementById("score").textContent = score;
    document.getElementById("total").textContent = total;
    document.getElementById("pct").textContent = total === 0 ? "0%" : Math.round((score / total) * 100) + "%";
    document.getElementById("streak").textContent = streak;
}

function showOnly(id) {
    ["welcome", "loading", "error-card", "question-card", "result-card"].forEach(function (elId) {
        document.getElementById(elId).style.display = "none";
    });
    document.getElementById(id).style.display = "block";
}

async function fetchQuestion() {
    showOnly("loading");

    var topic = document.getElementById("topic").value;
    var difficulty = document.getElementById("difficulty").value;

    try {
        var res = await fetch("/api/question", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ topic: topic, difficulty: difficulty }),
        });

        var data = await res.json();

        if (data.error) {
            document.getElementById("error-msg").textContent = data.error;
            showOnly("error-card");
            return;
        }

        renderQuestion(data);
    } catch (err) {
        document.getElementById("error-msg").textContent = "Network error. Check if the server is running.";
        showOnly("error-card");
    }
}

function renderQuestion(data) {
    answered = false;
    currentAnswer = data.correct;

    document.getElementById("q-number").textContent = "Question " + (total + 1);
    document.getElementById("q-text").textContent = data.question;

    var optionsEl = document.getElementById("options");
    optionsEl.innerHTML = "";

    Object.keys(data.options).sort().forEach(function (key) {
        var btn = document.createElement("button");
        btn.className = "option-btn";
        btn.innerHTML =
            '<span class="option-letter">' + key + "</span>" +
            '<span class="option-text">' + escapeHtml(data.options[key]) + "</span>";
        btn.onclick = function () {
            selectAnswer(key, data);
        };
        optionsEl.appendChild(btn);
    });

    showOnly("question-card");
}

function selectAnswer(chosen, data) {
    if (answered) return;
    answered = true;
    total++;

    var isCorrect = chosen === data.correct;
    if (isCorrect) {
        score++;
        streak++;
    } else {
        streak = 0;
    }
    updateScoreboard();

    var btns = document.querySelectorAll(".option-btn");
    btns.forEach(function (btn) {
        var letter = btn.querySelector(".option-letter").textContent;
        btn.classList.add("disabled");
        if (letter === data.correct) {
            btn.classList.add("correct");
        } else if (letter === chosen && !isCorrect) {
            btn.classList.add("wrong");
        }
    });

    var banner = document.getElementById("result-banner");
    banner.textContent = isCorrect ? "Correct!" : "Incorrect";
    banner.className = "result-banner " + (isCorrect ? "correct-banner" : "wrong-banner");

    document.getElementById("correct-answer").textContent =
        "Correct answer: " + data.correct + " — " + data.options[data.correct];

    document.getElementById("explanation").textContent = data.explanation;

    document.getElementById("result-card").style.display = "block";
    document.getElementById("result-card").scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function escapeHtml(text) {
    var d = document.createElement("div");
    d.textContent = text;
    return d.innerHTML;
}

updateScoreboard();
