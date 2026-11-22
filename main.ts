// Entry point: copy entry.png into the output directory.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath as urlToPath } from "node:url";

const root = dirname(urlToPath(import.meta.url));
const source = resolve(root, "entry.png");
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = resolve(targetDir, "entry.png");

if (!existsSync(source)) {
  throw new Error(`missing ${source}`);
}

const image = readFileSync(source);
const signature = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
for (let i = 0; i < signature.length; i++) {
  if (image[i] !== signature[i]) {
    const seen = [...image.subarray(0, 4)].map((b) => b.toString(16)).join(" ");
    throw new Error(`entry.png is not a PNG image (starts with ${seen})`);
  }
}
if (image.length > 1024 * 1024) {
  throw new Error(`entry.png is ${image.length} bytes, over the 1 MiB limit`);
}

mkdirSync(targetDir, { recursive: true });
writeFileSync(target, image);
console.log(`entry.png (${image.length} bytes) -> ${target}`);
