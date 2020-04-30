import { data } from './data.js'


let canvas = document.getElementById("gameScreen")
let ctx2 = canvas.getContext("2d")


export default class Player {
    constructor(game){

        //player's sprite
        this.image = document.getElementById("carole");

        //player's size
        this.width = 50;
        this.height = 50;
        //player move
        this.direction = 0;
        this.map = data.map1

        //player current row and column
        this.row = this.map.startingPoint[0];
        this.column = this.map.startingPoint[1];

        //player current coordinates x & y
        // this.xPos = this.column;
        // this.yPos = this.row;
        this.xPos = 50 * this.map.startingPoint[1];
        this.yPos = 50 * this.map.startingPoint[0];

        //player's in game inventory
        this.inventory = [];

    }


    moveLeft(){
        console.log('leftKey pressed')
        console.log(this.row, this.column)
        if (this.column > 0 && this.map.array[this.row][this.column - 1] != 1) {
            ctx2.clearRect(this.xPos, this.yPos, this.width, this.height);

            this.direction = 3
            this.column = this.column - 1
            this.xPos = this.xPos - 50
            console.log(this.xPos)
            ctx2.fillStyle="lightgray"
            ctx2.fillRect(this.xPos + 50, this.yPos, this.width, this.height);
            ctx2.fillStyle="red"
            ctx2.fillRect(this.xPos, this.yPos, this.width, this.height);
        }
    }

    moveRight(){
        console.log('right Key pressed')
        console.log(this.row, this.column)
        if (this.column < 14 && this.map.array[this.row][this.column + 1] != 1) {
            ctx2.clearRect(this.xPos, this.yPos, this.width, this.height);
            this.direction = 4
            this.column =this.column + 1
            this.xPos = this.xPos + 50
            console.log(this.xPos)
            ctx2.fillStyle="lightgray"
            ctx2.fillRect(this.xPos - 50, this.yPos, this.width, this.height);
            ctx2.fillStyle="red"
            ctx2.fillRect(this.xPos, this.yPos, this.width, this.height);
        }
    }

    moveUp(){
        console.log('up Key pressed')
        console.log(this.row, this.column)
        if (this.row > 0 && this.map.array[this.row - 1][this.column] != 1) {
            ctx2.clearRect(this.xPos, this.yPos, this.width, this.height);
            console.log("row", this.row)
            this.direction = 1
            this.row = this.row -1
            this.yPos = this.yPos -50
            ctx2.fillStyle="lightgray"
            ctx2.fillRect(this.xPos, this.yPos + 50, this.width, this.height);
            ctx2.fillStyle="red"
            ctx2.fillRect(this.xPos, this.yPos, this.width, this.height);
        }
    }

    moveDown(){
        console.log('down Key pressed')
        console.log(this.row, this.column)
        if (this.row < 14 && this.map.array[this.row + 1][this.column] != 1) {
            ctx2.clearRect(this.xPos, this.yPos, this.width, this.height);
            this.direction = 2
            this.row = this.row + 1
            this.yPos = this.yPos + 50
            console.log(this.yPos)
            ctx2.fillStyle="lightgray"
            ctx2.fillRect(this.xPos, this.yPos - 50, this.width, this.height);
            ctx2.fillStyle="red"
            ctx2.fillRect(this.xPos, this.yPos, this.width, this.height);
        }
    }

    pickItem(){
        // if (map1.array[this.row][this.column] == 2) {
        //     this.inventory.push() //this isn't right but something like this
        // }
        
        //pick up item function
        //when player approached some certain coordinate in the map
        //pick up the item
    }

    //once you have 3 sardine oils, you can unlock door
    unlockDoor(){
        //check if the next position is the door
        //check if the player has 3 sardine oil
        //if so, unlock the door
    }

    feedTheTiger(){
        //check if the player at the finish line (the coordinate)
        //check if the player has the man
        //"the man saw a tiger and the tiger ate the man"
        //playerWins
    }

    // move(value){
    //     console.log(this.map)
    //     console.log(this.map.startingPoint)
    //     console.log(this.row, this.column)
    //     switch(value){
    //         case 'up':
    //             if (this.row > 0 && this.map.array[this.row - 1][this.column] != 1) {
    //                 console.log("row", this.row)
    //                 this.direction = 1
    //                 this.row = this.row -1
    //                 this.yPos = this.yPos -50
    //             }
    //         case 'down':
    //             if (this.row < 14 && this.map.array[this.row + 1][this.column] != 1) {
    //                 this.direction = 2
    //                 this.row = this.row + 1
    //                 this.yPos = this.yPos + 50
    //             }
    //         case 'left':
    //             alert("LEFT MOFO")
    //             if (this.column > 0 && this.map.array[this.row][this.column - 1] != 1) {
    //                 this.direction = 3
    //                 this.column = this.column - 1
    //                 this.xPos = this.xPos - 50
    //             }
    //         case 'right':
    //             if (this.column < 14 && this.map.array[this.row][this.column + 1] != 1) {
    //                 this.direction = 4
    //                 this.column =this.column + 1
    //                 this.xPos = this.xPos + 50
    //             }
            
    //     }
    // }

    //pick up item
    

    draw(ctx){
        // sprite test
        // ctx.drawImage(
        //     this.image,
        //     this.row,
        //     this.column,
        //     this.height,
        //     this.width
        // );
        ctx.fillStyle = "red";
        ctx.fillRect(this.xPos, this.yPos, this.width, this.height);

        ctx.width = ctx.width
        
    }

    // update(dt) {
    //     this.position.x += this.speed;
    
    //     if (this.position.x < 0) this.position.x = 0;
    
    //     if (this.position.x + this.width > this.gameWidth)
    //       this.position.x = this.gameWidth - this.width;
    //   }
}