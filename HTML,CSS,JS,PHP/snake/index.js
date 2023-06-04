const gameBoard = document.querySelector("#gameBoard");
const ctx = gameBoard.getContext("2d");
const scoreText = document.querySelector("scoreText");
const resetBtn = document.querySelector("#resetBtn");
const gamewidth = gameBoard.width;
const gameHeight = gameBoard.height;
const boardBackground = "white";
const snakeColor = "lightgreen";
const snakeborder = "black";
const foodcolor = "red";
const unitsize = 25;
let running = false;
let Xvelocity = unitsize;
let Yvelocity = 0;
let foodX;
let foodY;
let score = 0;
let snake = [
    {x:unitsize * 4, y:0},
    {x:unitsize * 3, y:0},
    {x:unitsize * 2, y:0},
    {x:0, y:0}
];

window.addEventListener("keydown", changeDirection);
resetBtn.addEventListener("click", resetGame);

gameStart();

function gameStart(){
    running = true;
    scoreText.textContent = score;
    createFood();
    drawFood();
    nextTick();
};
function nextTick(){
    if(running){
        setTimeout(()=>{
            clearBoard();
            drawFood();
            movesnake();
            drawsnake();
            checkGameOver();
            nextTick();
        }, 75); 
    }
    else{
        displayGameOver();
    }
};
function clearBoard(){
    ctx.fillStyle = boardBackground;
    ctx.fillRect(0, 0, gamewidth , gameHeight);
};
function createFood(){
    function randomFood(min, max){
        const randNum = Math.round((Math.random() * (max - min) + min) / unitsize) * unitsize;
        return randNum;
        
    }
    foodX = randomFood(0, gamewidth - unitsize);
    foodY = randomFood(0, gamewidth - unitsize);
    console.log(foodX);
};
function drawFood(){
    ctx.fillStyle = foodcolor;
    ctx.fillRect(foodX, foodY, unitsize, unitsize);
};
function movesnake(){
    const head = {x: snake[0].x +Xvelocity,
                  y: snake[0].y +Yvelocity};
                  
    snake.unshift(head);
    if(snake[]){

    }
    else{
        snake.pop();
    }
};
function drawsnake(){
    ctx.fillStyle = snakeColor;
    ctx.strokeStyle = snakeborder;
    snake.forEach(snakePart => {
        ctx.fillRect(snakePart.x, snakePart.y, unitsize, unitsize);
        ctx.strokeRect(snakePart.x, snakePart.y, unitsize, unitsize);
    })

};
function changeDirection(){};
function displayGameOver(){};
function checkGameOver(){};
function resetGame(){};