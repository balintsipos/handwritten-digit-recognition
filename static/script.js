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

const putPoint = function(e) {
    if (dragging) {
        context.lineTo(e.pageX - canvasOffset.left, e.pageY - canvasOffset.top);
        context.stroke();
        context.beginPath();
        context.arc(e.offsetX, e.offsetY, radius, start, end);
        context.fill();
        context.beginPath();
        context.moveTo(e.pageX - canvasOffset.left, e.pageY - canvasOffset.top);
    }
}

const engage = function(e) {
    dragging = true;
    putPoint(e);
}

const disengage = function() {
    dragging = false;
    context.beginPath();    
}

const predict = function() {
    imgData = canvas.toDataURL();
    console.log(imgData);
}

const clear = function() {
    context.clearRect(0, 0, canvas.width, canvas.height);
}

canvas.addEventListener('mousedown', engage);
canvas.addEventListener('mousemove', putPoint);
canvas.addEventListener('mouseup', disengage);
predictBtn.addEventListener('click', predict);
clearBtn.addEventListener('click', clear);

