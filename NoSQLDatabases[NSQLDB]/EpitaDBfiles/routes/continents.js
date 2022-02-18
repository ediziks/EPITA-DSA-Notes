const express = require("express");
const router = express.Router();

const ContinentModel = require("../models/Continent");

router.get("/", async (req, res) => {
    const continents = await ContinentModel.find().populate("countries");
    res.status(200).json(continents)
});

module.exports = router;