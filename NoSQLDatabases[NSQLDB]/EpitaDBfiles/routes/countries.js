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
  const {name, isoCode} = req.body;
  const country = await CountryModel.findOneAndUpdate({
    _id: countryId
  },{
    name,
    isoCode: isoCode
  },{
    new: true
  });
  res.status(200).json(country);
});

// 1st question // not working
router.get("/?search=:search", async (req, res) => {
    const search = req.params.search;
    const countries = await (await CountryModel.find({name: {$regex: search, $options: 'i' }})).forEach(printjson);
    console.log(countries);
    res.status(200).json(countries);
});

module.exports = router;