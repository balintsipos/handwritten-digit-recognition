const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const predictBtn = document.getElementById('predictBtn');

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
canvas.width = 300;
canvas.height = 300;

let isDrawing = false;
    let lastX = 0;
    let lastY = 0;

    function draw(e) {
        if (!isDrawing) return;
        context.beginPath();
        context.moveTo(lastX, lastY);
        context.lineTo(e.offsetX, e.offsetY);
        context.lineWidth = 8;
        context.stroke();
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
    imgData = canvas.toDataURL();
    console.log(imgData);
}

const clear = function() {
    context.clearRect(0, 0, canvas.width, canvas.height);
}

predictBtn.addEventListener('click', predict);
clearBtn.addEventListener('click', clear);

