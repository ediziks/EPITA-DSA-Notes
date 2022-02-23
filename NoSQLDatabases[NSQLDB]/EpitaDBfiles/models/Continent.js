const mongoose = require('mongoose');

const ContinentModel = mongoose.model('Continent', {
    name: {
        type: String,
        required: true,
        unique: true
    },
    countries: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Country'
    }]
});

module.exports = ContinentModel;