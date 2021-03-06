import { data } from "./data.js";

let size = 30;

export default function mapBuilder(ctx, map) {
  for (let i = 0; i < map.array.length; i++) {
    for (let j = 0; j < map.array[i].length; j++) {
      switch (map.array[j][i]) {
        case 1:
          console.log(map.array[j][i]);
          ctx.fillStyle = "dimgray";
          ctx.fillRect(i * size, j * size, size, size);
          break;
        default:
          console.log(map.array[j][i]);
          ctx.fillStyle = "lightgray";
          ctx.fillRect(i * size, j * size, size, size);
          break;
      }
    }
  }
}
