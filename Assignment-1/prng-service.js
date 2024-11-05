const fs = require('fs');

// File where the PRNG service reads and writes
const prngFilePath = 'prng-service.txt';

// Function to generate a psuedo-random number
function generateRandomNumber() {
  return Math.floor(Math.random() * 100); // Generates a number beetween 0 and 99   
}

// Function to trigger the PRNG service manually
function runPRNGService() {
    const randomNumber = generateRandomNumber();
    fs.writeFile(prngFilePath, randomNumber.toString(), (err) => {
        if (err) {
            console.error('Error writing to the file:', err);
        } else {
            console.log(`Generated random number: ${randomNumber}`);
        }
    });
}

// Run the PRNG service when the program is executed
runPRNGService();