const express = require("express");
const router = express.Router();

const CountryModel = require("../models/Country");

router.get('/', async (req, res) => {
    const countries = await CountryModel.find().populate("continent");
    res.status(200).json(countries);
});

router.get('/:id', async (req, res) => {
    const countryId = req.params.id;
    const countries = await CountryModel.find({
      _id: countryId
    });
    // const countries = await CountryModel.findById(countryId); // this is the same as above

    res.status(200).json(countries);
});

router.post("/", async (req, res) => {
  console.log(req.body);
  const {name, isoCode} = req.body;
  const country = await CountryModel.create({
    name: name, 
    isoCode
  });

  /*const country = await CountryModel.create({
    name: "France",
    isoCode: "FR",
  });*/
  
  res.status(200).json(country);
});

router.delete("/:id", async (req, res) => {
  const countryId = req.params.id;
  await CountryModel.findOneAndDelete({
    _id: countryId
  });

  res.status(200).json({ msg: "Country deleted"});
});

router.put("/:id", async (req, res) => {
  const countryId = req.params.id;
  const {name, isoCode, population, continent} = req.body;
  const country = await CountryModel.findOneAndUpdate({
    _id: countryId
  },{
    name,
    isoCode: isoCode,
    population: population,
    continent: continent
  },{
    new: true
  });
  res.status(200).json(country);
});

// Number 1: Get the countries including substring
router.get("/search/:query?", async (req, res) => {
  const query = req.params.query;
  const result = await CountryModel.find({
    name: {$regex: query, $options: "i"}
  });
  res.status(200).json(result);
});

// Number 6: Gets all countries ordered by population in ascending order
router.get('/all/bypop', async (req, res) => {
  const countries = await CountryModel.find()
    .sort({population: 1});
  res.status(200).json(countries);
});

// Number 7: Gets countries where population is greater than 100000 and including u in the country name
router.get('/population/andu', async (req, res) => {
  const countries = await CountryModel.find({
    population: {$gt: 100000},
    name: {$regex: "u", $options: "i"}
  });
  res.status(200).json(countries);
});

module.exports = router;