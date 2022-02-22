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
    continent: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Continent"
    }
});

module.exports = CountryModel;