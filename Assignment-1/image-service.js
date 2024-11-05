const fs = require('fs');
const path = require('path');

// Path to the file used for communication
const imageFilePath = 'image-service.txt';

// Directory where your images are stored
const imagesDir = './images';

// Read all image filenames from the images directory
const images = fs.readdirSync(imagesDir);

// Function to get the image path based on the given index
function getImageByIndex(index) {
    const imageIndex = index % images.length; // Handle the case when index >= number of images
    return path.join(imagesDir, images[imageIndex]);
}

// Watch the image-service.txt file for changes
fs.watchFile(imageFilePath, (curr, prev) => {
    fs.readFile(imageFilePath, 'utf8', (err, data) => {
        if (err) throw err;
        const index = parseInt(data.trim(), 10); // Read the integer index from the file
        if (!isNaN(index)) {
            const imagePath = getImageByIndex(index);
            fs.writeFile(imageFilePath, imagePath, (err) => {
                if (err) throw err;
                console.log(`Selected image path: ${imagePath}`);
            });
        }
    });
});
