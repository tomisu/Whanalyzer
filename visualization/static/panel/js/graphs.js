queue()
    .defer(d3.json, STATIC_URL+"panel/data/data.json")
    .defer(d3.json, STATIC_URL+"panel/geojson/galicia.json")
    .await(makeGraphs);

var allRecords;
var ndx;
var idDim;

//Grupos
var numByDate;
var numByUser;
var numBySexo;
var numByConcejo;

//Charts
var hoursLineChart;
var usersRowChart;
var dateBarChart;
var dayBarChart;

var charts = [];

var personaActiva = -1;

var defaultMessageNumber = 10;
var currentMessageNumber = defaultMessageNumber;
var extraMessageNumber = 10;

$(document).ready(function(){

	$("#more-bar").on('click', function(){
		updateRecords(idDim, true);
	})



});

$( window ).resize(function() {
	resizeCharts();

	
});

function endall(transition, callback) { 
    if (transition.size() === 0) { callback() }
    var n = 0; 
    transition 
        .each(function() { ++n; }) 
        .each("end", function() { if (!--n) callback.apply(this, arguments); }); 
  } 

function resetDuration(chart, duration){
	console.log("Reset duration of: " + chart);
	//chart.transitionDuration(duration)
}

function getChartByAnchor(anchor){

	var anchor = "#"+$(anchor).attr("id");
	for (var i = 0; i < charts.length; i++){
		if (charts[i].anchor() == anchor){
			return charts[i];
		}
	}

}

function resizeCharts(){

	for (var i = 0; i < charts.length; i++){
		width = $(charts[i].anchor()).parent().width();
		charts[i].width(width);
		charts[i].transitionDuration(0);
		//Reset animation to original value when the instant transtion ends
		d3.select(charts[i].anchor()).transition().each( "end", function() {
	            var chart = getChartByAnchor(this);
	            chart.transitionDuration(chart.originalDuration);	
	    });
	}
	dc.renderAll();
}



function updateRecords(dim, moreMessages){
	var rowCode = '<tr class="list-person" data-id="##id##"><td class="date">##date##</td><td class="time">##time##</td><td class="user">##user##</td><td class="message">##message##</td></tr>';

	if (moreMessages === undefined){
		currentMessageNumber = defaultMessageNumber;
	} else{
		currentMessageNumber += extraMessageNumber;
	}

	allRecords = dim.bottom(currentMessageNumber);

	var table = $("#list-table");

	$("#list-table .list-person").not("active").remove();

	for (var i = 0; i < allRecords.length; i++){
		var record = allRecords[i];
		var personCode = rowCode.replace("##date##", dateFormat(record.date));
		var personCode = personCode.replace("##time##", record.hour+":"+record.mins);
		var personCode = personCode.replace("##user##", record.user);
		var personCode = personCode.replace("##id##", record.id);
		var personCode = personCode.replace("##message##", record.message);
		var newRow = $(personCode);		
		if (record.id == personaActiva){
			//$(newRow).addClass("active");
		}
		$(table).append(newRow);
	}


}

function cleanData(datos){
	newData = [];
	//Clean data
	for (var i = 0; i < datos.length; i++){
		d = datos[i];

		//console.log(d);
		var regex = /^([\d][\d]?\/[\d][\d]?\/[\d]{4}), ([\d][\d]):([\d][\d]) - (.*?): (.*$)/;
		var result = regex.exec(d);
		if (result == null){
			continue;
		}
		var date = new Date(result[1]);
		var hour = escapeHTML(result[2]);
		var mins = escapeHTML(result[3]);
		var name = escapeHTML(result[4]);
		var message = escapeHTML(result[5]);

		//Swap Sunday to last place
		var dayIndex = date.getDay()-1;
		if (dayIndex < 0) {
			dayIndex = days.length-1;
		}
		var day = days[dayIndex];

		newData.push(
			{
				"id":i,
				"date":date,
				"hour":hour,
				"mins":mins,
				"day":day,
				"user":name,
				"message":message
			}
			)
		/*
		console.log(d);
		console.log(date + "("+day+") at " + hour + " by '"+ name + "': " + message);
		*/
	}
	return newData;
}

function makeGraphs(error, datos, galiciaJson) {
	var twentysixers = 0;
	
	datos = cleanData(datos);

	//Create a Crossfilter instance
	ndx = crossfilter(datos);


	//Define Dimensions


	var userDim = ndx.dimension(function(d) { 
		return d["user"];
	});
	
	var dateDim = ndx.dimension(function(d) { 
		//if (d["Idade"] != 0){
			return d["date"];
		//}
	});
	var hourDim = ndx.dimension(function(d) { 
			return d["hour"];
	});
	var dayDim = ndx.dimension(function(d) { 
			return d["day"];
	});

	idDim = ndx.dimension(function(d){ return d["id"]});

	numByUser = userDim.group();
	numByDate = dateDim.group();
	numByHour = hourDim.group();
	numByDay = dayDim.group();

	var all = ndx.groupAll();

	updateRecords(idDim);

    //Charts
	usersRowChart = dc.rowChart("#sucesos-bar-chart");
	dateBarChart = dc.lineChart("#edad-chart");
	
	dayBarChart = dc.rowChart("#day-bar-chart");

	//Get the minimum non-0 age
	
	
	var dates = numByDate.top(Infinity);
	var min = new Date(2050, 0, 1);
	for (var i = 0; i < dates.length; i++){
		if (dates[i].key < min){
			min = dates[i].key;
		}
	}

	var minDate = min;//dateDim.bottom(1)[0]["Idade"];
	var maxDate = dateDim.top(1)[0]["date"];


	dateBarChart
		.width(1000)
		.height(160)
		.margins({top: 10, right: 50, bottom: 30, left: 50})
		.dimension(dateDim)
		.group(numByDate)
		.transitionDuration(500)
		.x(d3.time.scale().domain([minDate, maxDate]))
		.elasticY(true)		
		.renderLabel(true)	
		.on("filtered", function (){
			updateRecords(idDim);			
		})
		.yAxis().ticks(3);	

	hoursLineChart = dc.lineChart("#hours-line-chart");
	width = $("#hours-line-chart").parent().width();
	hoursLineChart
		.width( width)
		.height(200)
		.margins({top: 10, right: 50, bottom: 30, left: 50})
		.dimension(hourDim)
		.group(numByHour)
		.transitionDuration(500)
		.x(d3.scale.linear().domain([0,23]))
		.elasticY(true)		
		.renderLabel(true)	
		.on("filtered", function (){
			updateRecords(idDim);			
		})
		.yAxis().ticks(3);	

	usersRowChart
        .width(500)
        .height(500)
        .dimension(userDim)
        .group(numByUser)    
        .cap(11)
        .ordering(function(d){ return d.calls;})
        .elasticX(true)	
        .othersGrouper(false) //Removes "Other" from the list
        .on("filtered", function (){
			updateRecords(idDim);			
		})
        .xAxis().ticks(4);

    dayBarChart
    	.width(500)
        .height(250)
        .dimension(dayDim)
        .group(numByDay)    
        .cap(10)
        .ordering(function(d){ return days.indexOf(d.key);})
        .elasticX(true)	
        .othersGrouper(false) //Removes "Other" from the list
        .on("filtered", function (){
			updateRecords(idDim);			
		})
        .xAxis().ticks(4);

    charts.push(dateBarChart);
    charts.push(hoursLineChart);
    charts.push(usersRowChart);
    charts.push(dayBarChart);

    for (var i = 0; i < charts.length; i++){
		charts[i].originalDuration = [charts[i].transitionDuration()].slice(0);
	}

    dc.renderAll();

};