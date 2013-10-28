var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return d.tooltip;
  })

var margin = {top: 10, right: 10, bottom: 100, left: 100},
    margin2 = {top: 430, right: 10, bottom: 20, left: 100},
    width = $("#focus").width()-110,
    height = 500 - margin.top - margin.bottom,
    height2 = 500 - margin2.top - margin2.bottom;

var parseDate = d3.time.format("%m %Y").parse;

var x = d3.time.scale().range([0, width]),
    x2 = d3.time.scale().range([0, width]),
    y = d3.scale.linear().range([height, 0]),
    y2 = d3.scale.linear().range([height2, 0]);

var xAxis = d3.svg.axis().scale(x).orient("bottom"),
    xAxis2 = d3.svg.axis().scale(x2).orient("bottom"),
    yAxis = d3.svg.axis().scale(y).orient("left");

var brush = d3.svg.brush()
    .x(x2)
    .on("brush", brushed);

var getX = function(d){
  return x(d.date);
};

var getY = function(d){
  return y(d.value);
}

var area = d3.svg.area()
    .interpolate("monotone")
    .x( getX )
    .y0(height)
    .y1( getY );

var area2 = d3.svg.area()
    .interpolate("monotone")
    .x(function(d) { return x2(d.date); })
    .y0(height2)
    .y1(function(d) { return y2(d.value); });

var svg = d3.select("#focus").append("svg")
    .attr("width", "100%")
    .attr("height", height + margin.top + margin.bottom);

svg.call(tip);

svg.append("defs").append("clipPath")
    .attr("id", "clip")
  .append("rect")
    .attr("width", width)
    .attr("height", height);

var focus = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var context = svg.append("g")
    .attr("transform", "translate(" + margin2.left + "," + margin2.top + ")");

//d3.json("sp501.json", function(error, data) {
function loadD3(data){
  data.forEach(function(d) {
    d.date = parseDate(d.date);
    d.value = +d.value;
  });

  x.domain(d3.extent(data.map(function(d) { return d.date; })));
  y.domain([0, d3.max(data.map(function(d) { return d.value; }))]);
  x2.domain(x.domain());
  y2.domain(y.domain());

  focus.append("path")
      .datum(data)
      .attr("clip-path", "url(#clip)")
      .attr("d", area);

  focus.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  focus.append("g")
      .attr("class", "y axis")
      .call(yAxis);

  context.append("path")
      .datum(data)
      .attr("d", area2);

  context.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height2 + ")")
      .call(xAxis2);

  context.append("g")
      .attr("class", "x brush")
      .call(brush)
    .selectAll("rect")
      .attr("y", -6)
      .attr("height", height2 + 7);

  // ploting the points
  focus
    .selectAll() 
    .data(data) 
    .enter().append("circle")
    .attr("fill", function(d){
      if(d.anomaly == true) return "#c0392b";
      else return "black";
      })
    .attr("opacity", function(d){
      if (d.anomaly == false) return 0.2;
    })
    .attr("r", 4)
    .attr("cx", getX)
    .attr("cy", getY)
    .on("click", function(d){
        location.href='/ponto/'+d.id;
    })
    .on("mouseover", function(d){
      d3.select(this).attr("opacity", 1);
      tip.show(d);
    })
    .on("mouseout", function(d){
      if (d.anomaly == false) d3.select(this).attr("opacity", 0.2);
      tip.hide(d);
    });
}

loadD3(data);

function brushed() {
  x.domain(brush.empty() ? x2.domain() : brush.extent());
  focus.select("path").attr("d", area);
  focus.select(".x.axis").call(xAxis);
  focus.selectAll("circle")
    .attr("r", function(d){
      minmax_date = x.domain();
      show_me = (d.date > minmax_date[0] && d.date < minmax_date[1]); 
      if (show_me) {
        return 4;
      } else{
        return 0;
      }
      })
    .attr("cx", getX) 
    .attr("cy", getY);
}


