// $(function (){
//     TESTER = document.getElementById('tester');
//     var Data = {
//         type: 'scatter',
//         x: 1-1,
//         y: 10,
//         mode: 'lines+markers',
//         name: 'Value',
//         showlegend: true,
//         hoverinfo: 'all',
//         line: {
//             color: 'blue',
//             width: 2
//         },
//         marker: {
//             color: 'blue',
//             size: 8,
//             symbol: 'circle'
//         }
//     }
//
//     var Viol = {
//         type: 'scatter',
//         // x:,
//         // y: ,
//         mode: 'markers',
//         name: 'Violation',
//         showlegend: true,
//         marker: {
//             color: 'rgb(255,65,54)',
//             line: {width: 3},
//             opacity: 0.5,
//             size: 12,
//             symbol: 'circle-open'
//         }
//     }
//
//     var CL = {
//         type: 'scatter',
//         x:[1-1, null,2-1],
//         y: [1, null,1],
//         mode: 'lines',
//         name: 'LCL/UCL',
//         showlegend: true,
//         line: {
//             color: 'red',
//             width: 2,
//             dash: 'dash'
//         }
//     }
//
//     var Centre = {
//         type: 'scatter',
//         x: [],
//         y: [],
//         mode: 'lines',
//         name: 'Centre',
//         showlegend: true,
//         line: {
//             color: 'grey',
//             width: 2
//         }
//     }
//
//     var data = [Data, Viol, CL, Centre]
//
//     var layout = {
//         title: '計數管制圖',
//         xaxis: {
//             zeroline: false
//         },
//         yaxis: {
//             range: [],
//             zeroline: false
//         }
//     }
//
//     Plotly.newPlot('plot', data, layout);
//     console.log(Plotly.BUILD);
// });
