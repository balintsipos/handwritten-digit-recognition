const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const predictBtn = document.getElementById('predictBtn');
const predictedValueLabel = document.getElementById('prediction-result')

const radius = 5;
let start = 0;
let end = Math.PI * 2;
let dragging = false;

context.lineWidth = radius * 2;

function offset(el) {
    box = el.getBoundingClientRect();
    docElem = document.documentElement;
    return {
        top: box.top + window.pageYOffset - docElem.clientTop,
        left: box.left + window.pageXOffset - docElem.clientLeft
    };
}

const canvasOffset = offset(canvas);
canvas.width = 500;
canvas.height = 500;

context.fillStyle = "white";
context.fillRect(0, 0, canvas.width, canvas.height);

let isDrawing = false;
    let lastX = 0;
    let lastY = 0;

function draw(e) {
    if (!isDrawing) {
        return;
    }
    context.lineJoin = "round";
    context.lineCap = "round";
    context.beginPath();
    context.moveTo(lastX, lastY);
    context.lineTo(e.offsetX, e.offsetY);
    context.lineWidth = 8;
    context.stroke();

    let alpha = 1.0;
    let delta = 0.01;
    for (let i = 0; i < 5; i++) {
        context.strokeStyle = `rgba(128, 128, 128, ${alpha})`;
        context.lineWidth = 2 + (i + 1) * 2;
        context.beginPath();
        context.moveTo(lastX, lastY);
        context.lineTo(e.offsetX, e.offsetY);
        context.stroke();
        alpha -= delta;
    }
    [lastX, lastY] = [e.offsetX, e.offsetY];
    }

canvas.addEventListener('mousedown', (e) => {
    isDrawing = true;
    [lastX, lastY] = [e.offsetX, e.offsetY];
});

canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', () => isDrawing = false);
canvas.addEventListener('mouseout', () => isDrawing = false);

const predict = function() {
    let imgData = canvas.toDataURL('image/jpg');

    let message = {
        image: imgData
    };
    fetch(`${window.origin}/predict`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(message),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
    .then(function (response) {
        if (response.status !== 200) {
            console.log(`Response status was not 200: ${response.status}`);
            return;
        }

        response.json().then(function (data) {
            console.log(data);
            const local = JSON.stringify(data);
            const result = JSON.parse(local);
            predictedValueLabel.textContent = result.predictedValue;
        })

    })
}

const clear = function() {
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "white";
    context.fillRect(0, 0, canvas.width, canvas.height);
}

predictBtn.addEventListener('click', predict);
clearBtn.addEventListener('click', clear);