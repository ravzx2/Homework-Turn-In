// from data.js
var tableData = data;

tbody = d3.select("tbody")

function displayData(data){ 
    tbody.text("")
    data.forEach(function(sighting){
    new_tr = tbody.append("tr")
    Object.entries(sighting).forEach(function([key, value]){
        new_td = new_tr.append("td").text(value)	
    })
})}

displayData(tableData)

var inputDate = d3.select("#datetime")
// var inputCity = d3.select("#city")
// var inputState = d3.select("#state")
// var inputCountry = d3.select("#country")
// var inputShape = d3.select("#shape")
var button = d3.select("filter-btn")

function changeHandler(){
    d3.event.preventDefault();

    console.log(inputDate.property("value"));
    var new_table = tableData.filter(sighting => sighting.datetime===inputDate.property("value"))
    displayData(new_table)

    // console.log(inputCity.property("value"));
    // var new_table = tableData.filter(sighting => sighting.city===inputCity.property("value"))
    // displayData(new_table)

    // console.log(inputState.property("value"));
    // var new_table = tableData.filter(sighting => sighting.state===inputState.property("value"))
    // displayData(new_table)

    // console.log(inputCountry.property("value"));
    // var new_table = tableData.filter(sighting => sighting.country===inputCountry.property("value"))
    // displayData(new_table)

    // console.log(inputShape.property("value"));
    // var new_table = tableData.filter(sighting => sighting.shape===inputShape.property("value"))
    // displayData(new_table)
}

inputDate.on("change", changeHandler)
// inputCity.on("change", changeHandler)
// inputState.on("change", changeHandler)
// inputCountry.on("change", changeHandler)
// inputShape.on("change", changeHandler)
button.on("click", changeHandler)