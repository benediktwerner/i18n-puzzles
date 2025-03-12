import * as fs from "fs";

let result = 0;
let x = 0;

fs.readFileSync("input.txt", "utf8")
  .split(/\n/g)
  .map((line) => [...line])
  .forEach((line) => {
    if (line[x] === "💩") {
      result++;
    }
    x = (x + 2) % line.length;
  });

console.log(result);
