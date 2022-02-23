const mongoose = require('mongoose');

const CountryModel = mongoose.model('Country', {
    name: {
        type: String,
        required: true,
        unique: true
    },
    isoCode: {
        type: String
    },
    // Number 2: Adds a collection contintent link to countries
    continent: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: "Continent"
    }],
    // Number 5: Adds population field to countries
    population: {
        type: Number,
        default: -1
    },
});

module.exports = CountryModel;