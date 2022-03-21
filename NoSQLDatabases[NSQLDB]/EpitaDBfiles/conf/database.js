const mongoose = require('mongoose');

mongoose.connect(process.env.MONGO_URL, {family:4}, (error) => {
    if (error) throw error;

    console.log("Connected to database!");
});