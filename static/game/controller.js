export default class Controller {
    constructor(player, game) {
      document.addEventListener("keydown", event => {
        
        switch (event.keyCode) {
          case 37:
            // player.move('left');
            player.moveLeft();
            
            // alert(event.keyCode)
            break;
          case 39:
            // player.move('right');
            player.moveRight();
            // alert(event.keyCode)
            break;
          case 38:
            // player.move('up');
            player.moveUp();
            // alert(event.keyCode)
            break;
          case 40:
            player.moveDown();
            // player.move('down');
            // alert(event.keyCode)
            break;
        }
      });
    }
  }
  