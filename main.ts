// news-image-20261120 entry (Node 22, standard library only).
// The image beside this file is the front page drawn in code by draw_news.py:
// "The World in One Day — Friday, 20 November 2026", five stories reported
// that day (ICJ genocide ruling, Shenzhen summit, Kyiv strikes, Riyadh
// missile, markets slide). This program copies it to /output/entry.png.
//
// The gate takes a whole PNG of at most 1 MiB and 1024 by 1024 pixels;
// entry.png is 1024x1024 and well under the size cap, and the copy is
// byte-identical on every run, so both grader runs write the same bytes.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
