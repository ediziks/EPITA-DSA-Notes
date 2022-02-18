const mongoose = require('mongoose');

const ContinentModel = mongoose.model('Continent', {
    name: {
        type: String,
        required: true,
        unique: true
    },
    // isoCode: {
    //     type: String
    // },
    countries: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Country'
    }]
});

module.exports = ContinentModel;