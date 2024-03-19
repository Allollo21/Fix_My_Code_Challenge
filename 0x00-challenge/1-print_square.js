#!/usr/bin/node

/**
 * This script prints a square with the character '#'.
 * The size of the square is determined by the first argument passed to the program.
 */

const size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
    console.error("Missing or invalid argument");
    console.error("Usage: ./1-print_square.js <size>");
    console.error("Example: ./1-print_square.js 8");
    process.exit(1);
}

const square = Array(size).fill('#'.repeat(size)).join('\n');
console.log(square);

