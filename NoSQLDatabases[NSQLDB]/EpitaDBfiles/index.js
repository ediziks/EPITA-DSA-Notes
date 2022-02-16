require("dotenv").config();
const { response } = require("express");
// console.log('Hello World!');

// console.log('smt else...');

// console.log(process.env) // remove this after you've confirmed it working

const express = require("express");

require("./conf/database");

const app = express();
app.use(express.json());

const CountryModel = require("./models/Country");

app.get("/", (request, response) => {
  response.status(200).json({ msg: "It's working! smt else..." });
});

app.get("/countries", async (req, res) => {
  const countries = await CountryModel.find();
  res.status(200).json(countries);
});

app.get('/countries/:id', async (req, res) => {
    const countryId = req.params.id;
    const countries = await CountryModel.find({
      _id: countryId
    });
    // const countries = await CountryModel.findById(countryId);
});

app.post("/countries", async (req, res) => {
  console.log(req.body);
  const {name, isoCode} = req.body;
  const country = await CountryModel.create({
    name: name, 
    isoCode
  });

  /*const country = await CountryModel.create({
    name: "France",
    isoCode: "FR",
  });
  
  res.status(200).json(country);*/
});

app.delete("/countries/:id", async (req, res) => {
  const countryId = req.params.id;
  await CountryModel.findOneAndDelete({
    _id: countryId
  });

  response.status(200).json({ msg: "Country deleted" });
});

app.put("/countries/:id", async (req, res) => {
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
  response.status(200).json(country);
});

const port = 3000;

app.listen(3000, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
