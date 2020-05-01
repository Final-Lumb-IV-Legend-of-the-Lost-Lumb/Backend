import Player from "./player.js";
import MapBuilder from "./map.js";
import { data } from "./data.js";
import Controller from "./controller.js";
import Collectible from "./collectible.js";

export default class Game {
  constructor(gameWidth, gameHeight) {
    this.gameWidth = gameWidth;
    this.gameHeight = gameHeight;
    this.player = new Player(this);
    this.collectible = new Collectible(this);
    this.map = data.map2;

    new Controller(this.player, this);
  }

  draw(ctx) {
    MapBuilder(ctx, this.map);
    this.player.draw(ctx);
    this.collectible.draw(ctx);
  }
}
