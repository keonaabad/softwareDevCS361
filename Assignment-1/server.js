const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware to parse incoming text data
app.use(express.text()); 

// Serve static files from the 'images' directory
app.use('/images', express.static(path.join(__dirname, 'images')));

// Paths to the text files used for communication
const prngFilePath = path.join(__dirname, 'prng-service.txt');
const imageFilePath = path.join(__dirname, 'image-service.txt');

// Serve the index.html file at the root route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Endpoint to trigger the PRNG Service
app.get('/trigger-prng', (req, res) => {
    fs.writeFile(prngFilePath, 'run', (err) => {
        if (err) {
            console.error('Error triggering PRNG Service:', err);
            return res.status(500).send('Error triggering PRNG Service');
        }

        // Wait for the PRNG Service to generate the random number
        setTimeout(() => {
            fs.readFile(prngFilePath, 'utf8', (err, data) => {
                if (err) {
                    console.error('Error reading random number:', err);
                    return res.status(500).send('Error reading random number');
                }
                console.log(`Random number generated: ${data.trim()}`);
                res.send(data.trim()); // Send the generated random number to the UI
            });
        }, 1000); // Wait 1 second for the PRNG Service to complete
    });
});

// Endpoint to pass the random number to the Image Service
app.post('/image-service', (req, res) => {
    const randomNumber = req.body.trim();
    fs.writeFile(imageFilePath, randomNumber, (err) => {
        if (err) {
            console.error('Error sending random number to Image Service:', err);
            return res.status(500).send('Error sending random number to Image Service');
        }

        // Wait for the Image Service to generate the image path
        setTimeout(() => {
            fs.readFile(imageFilePath, 'utf8', (err, data) => {
                if (err) {
                    console.error('Error reading image path:', err);
                    return res.status(500).send('Error reading image path');
                }
                const imagePath = `/images/${path.basename(data.trim())}`;
                console.log(`Serving image path to client: ${imagePath}`); // Log the image path for debugging
                res.send(imagePath); // Send the relative image path to the UI
            });            
        }, 1000); // Wait 1 second for the Image Service to complete
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
