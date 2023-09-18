const graphDiv = document.getElementById("graph");
let params = new URLSearchParams(window.location.search)
var layout = {
    title: "Spotify Data",
    xaxis: {
        title: params.get('xAxis')
    },
    yaxis: {
        title: params.get('yAxis')
    }
}

fetch(
    //"https://oa-2023-24-backend.onrender.com" //use "http://localhost:3000" if running sample express backend locally, or replace with your own backend endpoint url
    ("https://dssd-application.onrender.com/?" +window.location.href.split('?')[1])
    
).then(async res => {
    Plotly.newPlot( graphDiv, [ await res.json() ], layout); 
})

