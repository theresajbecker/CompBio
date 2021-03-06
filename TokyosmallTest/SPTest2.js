/*
This demo visualises the railway stations in Tokyo (東京) as a graph.

This demo gives examples of

- loading elements via ajax
- loading style via ajax
- using the preset layout with predefined positions in each element
- using motion blur for smoother viewport experience
- using `min-zoomed-font-size` to show labels only when needed for better performance
*/

  $(document).ready(function(){
// uses ajax to fetch network files from rawgit stores at variable graphP
   var graphP = $.ajax({
    url: 'https://rawgit.com/theresajbecker/CompBio/master/TokyosmallTest/TestData/FinalNetwork3-8-25.json',
    type: 'GET',
    dataType: 'json'
  }).done(function(graphP) {  
    // .done required to sync asynchronous fetching
    //returns graphP which is json struct
    // takes graphP.elements and stores as elements - move one level in to the struct 
    var elements = graphP.elements;
    
    //instantiates struct 
    var cy = window.cy = cytoscape({
      // creates container 
      container: document.getElementById('cy'),
      style: cytoscape.stylesheet()
      //sets css for nodes - see cystoscape.js documention 
        .selector('node')
          .css({
            'content': 'data(id)',
            // for tot mutations between 0 and 10 map to font size from 0 to 10
            'font-size' : 'dataData(total_mutations, 0, 498, 10, 25)',
            'height': 'mapData(total_mutations, 86, 498, 10, 60)',
            'width': 'mapData(total_mutations, 86, 498, 10, 60)',
            
            //'color' : 'black',
            //node opacity 
            'background-opacity': 'mapData(total_mutations, 5, 10, 1, 1)',
            'border-opacity': 'mapData(total_mutations, 5, 10, 0, 0)',
            //text-opacity is for both background and outline
            'text-opacity': 'mapData(total_mutations, 5, 10, 1, 1)',
            'text-valign': 'center',
            'text-outline-width': 0,
            'text-outline-color': 'black',
            'background-color': 'mapData(total_mutations, 200, 500, yellow, red)',
      })
    .selector(':selected')
      .css({
        'border-width': .5,
        'border-color': '#333'
      })
    .selector('edge')
      .css({
        'opacity': 'mapData(count, 26, 124, .25, 1)',
        'width': 'mapData(count, 26, 124, .5, 2)',
        'line-color': 'black',
      }),
      layout: {
        //cose is force directed layout 
        name: 'cose',
        paddint: 10
      },

      elements: elements,
      animate: true, // whether to show the layout as it's running
      maxSimulationTime: 4000, // max length in ms to run the layout
      ungrabifyWhileSimulating: false, // so you can't drag nodes during layout
      fit: true, // whether to fit the viewport to the graph
      padding: 30, // padding on fit
      boundingBox: undefined, // constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
      random: false, // whether to use random initial positions
      infinite: false, // overrides all other options for a forces-all-the-time mode
      ready: undefined, // callback on layoutready
      stop: undefined, // callback on layoutstop

      // springy forces
      stiffness: 400,
      repulsion: 400,
      damping: 0.5

    }); // end init

}); // end graphP function 
}); // dom ready 