// // from data.js
// var tableData = data;

// // Get a reference to the table body
// var tbody = d3.select("tbody");


// tableData.forEach((ufodata) => {
//   var row = tbody.append("tr");
//   Object.values(ufodata).forEach((value) => {
//     var cell = row.append("td");
//     cell.text(value);
//   });
// });

// // Select the button
// var button = d3.select("#filter-btn");
// button.on("click", function(){

// // alert("You clicked a button. Great job!");
//     // Select the input element and get the raw HTML node

  
//     // Get the value property of the input element
//   var inputValue = d3.select("#datetime").property("value");
//   var inputCity = d3.select("#city").property("value");
//   var inputCountry = d3.select("#country").property("value");
//   var inputShape = d3.select("#shape").property("value");


//   d3.select("tbody").selectAll("tr").remove();
  
//   // alert(inputValue);
//   // console.log(inputValue);
//   // console.log(data);


//   // let filteredData = tableData;

//   // if (inputValue !== " "){
//   //   filteredData = tableData.filter(ufodata => ufodata.datetime === inputValue)
//   // };
//   // if (inputCity !== " "){
//   //   filteredData = tableData.filter(ufodata => ufodata.city === inputCity)
//   // };
//   // if (inputCountry !== " "){
//   //   filteredData = tableData.filter(ufodata => ufodata.country === inputCountry)
//   // };
//   // if (inputShape !== " "){
//   //   filteredData = tableData.filter(ufodata => ufodata.shape === inputShape)
//   // };

//   let filteredData = tableData.filter(ufodata => ufodata.datetime === inputValue);
//   // filteredData = tableData.filter(ufodata => ufodata.city === inputCity);
//   // filteredData = tableData.filter(ufodata => ufodata.state === inputState);
//   // filteredData = tableData.filter(ufodata => ufodata.country === inputCountry);
//   // filteredData = tableData.filter(ufodata => ufodata.country === inputShape);


//   filteredData.forEach((ufodata) => {
//     var row = tbody.append("tr");
//     Object.values(ufodata).forEach((value) => {
//       var cell = row.append("td");
//       cell.text(value);
//     });
//   });
// });
  







// Assigning the data from data.js to a variable
var tableData = data;

// Get a reference to the table body
var tbody = d3.select("tbody");

// Append values from data.js to the table in HTML file
tableData.forEach((ufodata) => {
  var row = tbody.append("tr");
  Object.values(ufodata).forEach((value) => {
    var cell = row.append("td");
    cell.text(value);
  });
});

// Get a reference to the button
var button = d3.select("#filter-btn");

// Declare a function
button.on("click", function () {
  
  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");
  let inputCity = d3.select("#city").property("value");
  let inputState = d3.select("#state").property("value");
  let inputCountry = d3.select("#country").property("value");
  let inputShape = d3.select("#shape").property("value");

  d3.select("tbody").selectAll("tr").remove();

  // Create a logic to avoid null values
  let filterData = tableData;
  
  if (inputValue !== "") {
    filterData = tableData.filter(ufoRow => ufoRow.datetime === inputValue);
  };
  if (inputCity !== "") {
    filterData = filterData.filter(ufoRow => ufoRow.city === inputCity);
  }
  if (inputState !== "") {
    filterData = filterData.filter(ufoRow => ufoRow.state === inputState);
  }
  if (inputCountry !== "") {
    filterData = filterData.filter(ufoRow => ufoRow.country === inputCountry);
  }
  if (inputShape !== "") {
    filterData = filterData.filter(ufoRow => ufoRow.shape === inputShape);
  }

  // Appending filtered values into the table
  filterData.forEach((ufodata) => {
    var row = tbody.append("tr");
    Object.values(ufodata).forEach(value => {
      var cell = row.append("td");
      cell.text(value);    
    });
  });
});