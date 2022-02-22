require("dotenv").config();
// console.log(process.env) // remove this after you've confirmed it working

const express = require("express");

require("./conf/database");
const countriesRoutes = require("./routes/countries");
const continentsRoutes = require("./routes/continents");

const app = express();
app.use(express.json());

app.use("/countries", countriesRoutes);
app.use("/continents", continentsRoutes);

app.get("/", (request, response) => {
  response.status(200).json({msg: "It's working!"});
});

const port = 3000;

app.listen(3000, () => {
  console.log(`Server is running on http://localhost:${port}`);
});