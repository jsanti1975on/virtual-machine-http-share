let frames = [];
let speechLines = [];
let frameIndex = 0;
let speechIndex = 0;
let typingSpeed = 50;
let lineDelay = 2000;

async function loadAssets() {
  try {
    const framesRes = await fetch("assets/tux-frames.txt");
    const framesText = await framesRes.text();
    frames = framesText.split("---").map(f => f.trim());
    console.log("Frames loaded:", frames);

    const speechRes = await fetch("assets/tux-speech.txt");
    const speechText = await speechRes.text();
    speechLines = speechText.split("\n").filter(line => line.trim().length > 0);
    console.log("Speech lines loaded:", speechLines);

    startAnimation();
  } catch (err) {
    document.getElementById("ascii").textContent = "⚠️ Error loading Tux assets!";
    console.error(err);
  }
}

function animateTux() {
  if (frames.length === 0) return;
  document.getElementById("ascii").textContent = frames[frameIndex];
  frameIndex = (frameIndex + 1) % frames.length;
}

function typeLine(line, callback) {
  const speechEl = document.getElementById("speech");
  speechEl.innerHTML = "";

  let i = 0;
  function typeChar() {
    if (i < line.length) {
      speechEl.innerHTML = line.substring(0, i + 1) + '<span class="cursor">█</span>';
      i++;
      setTimeout(typeChar, typingSpeed);
    } else {
      speechEl.innerHTML = line + '<span class="cursor">█</span>';
      if (callback) setTimeout(callback, lineDelay);
    }
  }
  typeChar();
}

function showSpeechLine() {
  if (speechIndex >= speechLines.length) return;

  let line = speechLines[speechIndex];
  const speechEl = document.getElementById("speech");

  if (speechIndex === speechLines.length - 1) {
    speechEl.style.color = "red";
    speechEl.style.fontWeight = "bold";
  }

  typeLine(line, () => {
    speechIndex++;
    if (speechIndex < speechLines.length) {
      showSpeechLine();
    }
  });
}

function startAnimation() {
  setInterval(animateTux, 800);
  showSpeechLine();
}

loadAssets();