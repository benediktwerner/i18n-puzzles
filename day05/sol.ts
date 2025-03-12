/*
 * JS uses UTF-16, which leads to emoji (or more generally, code points from U+010000 to U+10FFFF) being represented by two characters.
 * These codepoints are represented by a high-low surrogate pair.
 * The first code unit is a high surrogate (0xD800–0xDBFF) and the second is a low surrogate (0xDC00–0xDFFF).
 * https://en.wikipedia.org/wiki/UTF-16
 */

import * as fs from "fs";

function isSurrogate(code: number): boolean {
  return code >= 0xd800 && code <= 0xdfff;
}

function determineWidth(line: string): number {
  let width = 0;
  for (let i = 0; i < line.length; i++) {
    width += 1;
    if (isSurrogate(line.charCodeAt(i))) {
      i += 1;
    }
  }
  return width;
}

function charAt(line: string, x: number): string {
  let xx = 0;
  for (let i = 0; i < x; i++) {
    xx += isSurrogate(line.charCodeAt(xx)) ? 2 : 1;
  }
  return isSurrogate(line.charCodeAt(xx)) ? line[xx] + line[xx + 1] : line[xx];
}

const lines = fs.readFileSync("input.txt", "utf8").split(/\n/g);
const width = determineWidth(lines[0]);

let result = 0;
let x = 0;

lines.forEach((line) => {
  if (charAt(line, x) === "💩") {
    result += 1;
  }
  x = (x + 2) % width;
});

console.log(result);
