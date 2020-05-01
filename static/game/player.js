import { data } from "./data.js";

let canvas = document.getElementById("gameScreen");
let ctx2 = canvas.getContext("2d");

export default class Player {
  constructor(game) {
    //player's sprite
    this.image = document.getElementById("carole");

    //player's size
    this.width = 50;
    this.height = 50;
    //player move
    this.direction = 0;
    this.map = data.map2;

    //player current row and column
    this.row = this.map.startingPoint[0];
    this.column = this.map.startingPoint[1];

    //player current coordinates x & y
    // this.xPos = this.column;
    // this.yPos = this.row;
    this.xPos = 50 * this.column;
    this.yPos = 50 * this.row;

    //player's in game inventory
    this.sardine = 0;
    this.gotJoe = false;
  }

  pickItem() {
    if (this.map.array[this.row][this.column] == 2) {
      this.sardine++;
      this.map.array[this.row][this.column] = 0;
      console.log(this.sardine);
    }
    this.unlockDoor();
  }

  unlockDoor() {
    if (this.sardine == 3) {
      ctx2.fillStyle = "lightgray";
      ctx2.fillRect(
        this.map.theDoor[1] * 50,
        this.map.theDoor[0] * 50,
        this.width,
        this.height
      );
      this.map.array[this.map.theDoor[0]][this.map.theDoor[1]] = 0;
      this.sardine = 0;
    }
  }

  get_joe() {
    if (this.map.array[this.row][this.column] == 5) {
      this.gotJoe = true;
      this.map.array[this.row][this.column] = 0;
      console.log(this.gotJoe);
    }
  }

  feedTheTiger() {
    if (this.gotJoe == true && this.map.array[this.row][this.column] == 6) {
      function timeout() {
        setTimeout(() => {
          alert("You successfully fed your tiger with Joe Exotic!");
        }, 500);
      }
      ctx2.drawImage(
        document.getElementById("fedTiger"),
        50 * this.map.cage[1],
        50 * this.map.cage[0],
        this.height,
        this.width
      );
      timeout();
    }
  }

  moveLeft() {
    if (this.column > 0 && this.map.array[this.row][this.column - 1] !== 1) {
      ctx2.clearRect(this.xPos, this.yPos, this.width, this.height);
      this.direction = 3;
      this.column = this.column - 1;
      this.xPos = this.xPos - 50;
      ctx2.fillStyle = "lightgray";
      ctx2.fillRect(this.xPos + 50, this.yPos, this.width, this.height);
      ctx2.drawImage(this.image, this.xPos, this.yPos, this.height, this.width);
    }
    this.pickItem();
    this.get_joe();
    this.feedTheTiger();
  }

  moveRight() {
    if (this.column < 14 && this.map.array[this.row][this.column + 1] !== 1) {
      ctx2.clearRect(this.xPos, this.yPos, this.width, this.height);
      this.direction = 4;
      this.column = this.column + 1;
      this.xPos = this.xPos + 50;
      ctx2.fillStyle = "lightgray";
      ctx2.fillRect(this.xPos - 50, this.yPos, this.width, this.height);
      ctx2.drawImage(this.image, this.xPos, this.yPos, this.height, this.width);
    }
    this.pickItem();
    this.get_joe();
    this.feedTheTiger();
  }

  moveUp() {
    if (this.row > 0 && this.map.array[this.row - 1][this.column] !== 1) {
      ctx2.clearRect(this.xPos, this.yPos, this.width, this.height);
      this.direction = 1;
      this.row = this.row - 1;
      this.yPos = this.yPos - 50;
      ctx2.fillStyle = "lightgray";
      ctx2.fillRect(this.xPos, this.yPos + 50, this.width, this.height);
      ctx2.drawImage(this.image, this.xPos, this.yPos, this.height, this.width);
    }
    this.pickItem();
    this.get_joe();
    this.feedTheTiger();
  }

  moveDown() {
    if (this.row < 14 && this.map.array[this.row + 1][this.column] !== 1) {
      ctx2.clearRect(this.xPos, this.yPos, this.width, this.height);
      this.direction = 2;
      this.row = this.row + 1;
      this.yPos = this.yPos + 50;
      ctx2.fillStyle = "lightgray";
      ctx2.fillRect(this.xPos, this.yPos - 50, this.width, this.height);
      ctx2.drawImage(this.image, this.xPos, this.yPos, this.height, this.width);
    }
    this.pickItem();
    this.get_joe();
    this.feedTheTiger();
  }

  // win() {}

  draw(ctx) {
    ctx.drawImage(this.image, this.xPos, this.yPos, this.height, this.width);
  }
}
