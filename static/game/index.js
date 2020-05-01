import Game from "./game.js";

let canvas = document.getElementById("gameScreen");
let ctx = canvas.getContext("2d");

const game_width = 450;
const game_height = 450;

let game = new Game(game_width, game_height);

ctx.clearRect(0, 0, 450, 450);

game.draw(ctx);

// game.start()
