import { data } from "./data.js";

export default class Collectible {
  constructor(game, name, x, y) {
    this.image = document.getElementById("fish");

    this.width = 50;
    this.height = 50;

    this.name = name;
    this.map = data.map2;

    this.row = this.map.sardineOil[0][0];
    this.column = this.map.sardineOil[0][1];

    console.log("rc", this.row, this.column);

    //player current coordinates x & y
    // this.xPos = this.column;
    // this.yPos = this.row;
    this.xPos = 50 * this.column;
    this.yPos = 50 * this.row;
  }

  draw(ctx) {
    // sardine 1
    ctx.drawImage(this.image, this.xPos, this.yPos, this.height, this.width);
    // sardine 2
    ctx.drawImage(
      this.image,
      50 * this.map.sardineOil[1][1],
      50 * this.map.sardineOil[1][0],
      this.height,
      this.width
    );
    // sardine 3
    ctx.drawImage(
      this.image,
      50 * this.map.sardineOil[2][1],
      50 * this.map.sardineOil[2][0],
      this.height,
      this.width
    );
    // tiger
    ctx.drawImage(
      document.getElementById("tiger"),
      50 * this.map.finishLine[1],
      50 * this.map.finishLine[0],
      this.height,
      this.width
    );
    // joe
    ctx.drawImage(
      document.getElementById("joe"),
      50 * this.map.theMan[1],
      50 * this.map.theMan[0],
      this.height,
      this.width
    );
  }
}
