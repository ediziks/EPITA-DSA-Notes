const mongoose = require('mongoose');

const CountryModel = mongoose.model('Country', {
    name: {
        type: String,
        required: true,
        unique: true
    },
    isoCode: {
        type: String
    }
});

module.exports = CountryModel;