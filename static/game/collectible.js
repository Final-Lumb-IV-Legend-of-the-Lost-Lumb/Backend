import { data } from "./data.js";

export default class Collectible {
  constructor(game, name, x, y) {
    this.image = document.getElementById("fish");

    this.width = 30;
    this.height = 30;

    this.name = name;
    this.map = data.map2;

    this.row = this.map.sardineOil[0][0];
    this.column = this.map.sardineOil[0][1];

    console.log("rc", this.row, this.column);

    //player current coordinates x & y
    // this.xPos = this.column;
    // this.yPos = this.row;
    this.xPos = 30 * this.column;
    this.yPos = 30 * this.row;
  }

  draw(ctx) {
    // sardine 1
    ctx.drawImage(this.image, this.xPos, this.yPos, this.height, this.width);
    // sardine 2
    ctx.drawImage(
      this.image,
      30 * this.map.sardineOil[1][1],
      30 * this.map.sardineOil[1][0],
      this.height,
      this.width
    );
    // sardine 3
    ctx.drawImage(
      this.image,
      30 * this.map.sardineOil[2][1],
      30 * this.map.sardineOil[2][0],
      this.height,
      this.width
    );
    // tiger
    ctx.drawImage(
      document.getElementById("tiger"),
      30 * this.map.cage[1],
      30 * this.map.cage[0],
      this.height,
      this.width
    );

    //tiger cage
    ctx.beginPath();
    ctx.moveTo(this.map.cage[1] * 30, this.map.cage[0] * 30);
    ctx.lineTo(this.map.cage[1] * 30, (this.map.cage[0] + 1) * 30);
    ctx.lineTo((this.map.cage[1] + 1) * 30, (this.map.cage[0] + 1) * 30);
    ctx.lineTo((this.map.cage[1] + 1) * 30, (this.map.cage[0] + 0) * 30);
    ctx.lineTo(this.map.cage[1] * 30, this.map.cage[0] * 30);
    ctx.strokeStyle = "black";
    ctx.stroke();

    // joe
    ctx.drawImage(
      document.getElementById("joe"),
      30 * this.map.theMan[1],
      30 * this.map.theMan[0],
      this.height,
      this.width
    );

    // door
    ctx.fillStyle = "lightgray";
    ctx.fillRect(this.map.theDoor[1] * 30, this.map.theDoor[0] * 30, 30, 30);
    ctx.fillStyle = "red";
    ctx.fillRect(this.map.theDoor[1] * 30, this.map.theDoor[0] * 30, 30, 30);
  }
}
