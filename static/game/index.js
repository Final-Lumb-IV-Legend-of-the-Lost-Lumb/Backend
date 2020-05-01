import Game from "./game.js";

let canvas = document.getElementById("gameScreen");
let ctx = canvas.getContext("2d");

const game_width = 500;
const game_height = 500;

let game = new Game(game_width, game_height);

ctx.clearRect(0, 0, 500, 500);

game.draw(ctx);

// game.start()
