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
   var graphP = $.ajax({
    url: 'https://rawgit.com/theresajbecker/CompBio/master/SuperSmallNodes.json',
    type: 'GET',
    dataType: 'json'
  }).done(function(graphP) {  
    console.log(graphP)

    var loading = document.getElementById('loading');
    var expJson = graphP;
    console.log(expJson)
    //taking out style load
    var elements = expJson.elements;
    console.log("ELEMENTS")
    console.log(elements )
    loading.classList.add('loaded');
    
    var cy = window.cy = cytoscape({

      container: document.getElementById('cy'),
      //changing layout to cola from { name: 'preset' },
      //layout: { name: 'preset' },
      layout: 'springy',
       // layout: {
       //  name: 'springy',
       //  padding: 10,
       //  edgeLength : 'data(weight)',
       //  },
      //attempting to change the style and layout
      //layout: 'springy',
      //taking out style
      //style: styleJson,
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

    }); // end init cytoscape




}); // end graphP function 
}); // dom ready 


