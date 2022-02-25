const express = require("express");
const router = express.Router();

const ContinentModel = require("../models/Continent");

router.get("/", async (req, res) => {
    const continents = await ContinentModel.find().populate("countries");
    res.status(200).json(continents)
});

router.post("/", async (req, res) => {
    const {name, countries} = req.body;
    const continent = await ContinentModel.create({
        name,
        countries: countries
    });
    res.status(200).json(continent);
});

// Number 3: Send the list of continents with first 3 countries
router.get("/list3", async (req, res) => {
    const continent = await ContinentModel
    .find()
    .populate({
        path: "countries",
        select: "name isoCode population",
        options: {
            limit: 3
        },
        // sort: {
        //     name: 1
        // }
    });
    res.status(200).json(continent)
});

// Number 4: Gets till the 4th country under specified continent ordered by name
router.get("/upto/fourth", async (req, res) => {
    const continentId = req.params.id;
    const fourth = await ContinentModel.find()
        .populate({
            path: "countries",
            select: "name isoCode population",
            options: {
                sort: {
                    name: 1
                },
                perDocumentLimit: 4
            }
        });
    res.status(200).json(fourth);
});

module.exports = router;