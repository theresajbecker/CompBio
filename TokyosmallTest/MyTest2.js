/*
This demo visualises the railway stations in Tokyo (東京) as a graph.

This demo gives examples of

- loading elements via ajax
- loading style via ajax
- using the preset layout with predefined positions in each element
- using motion blur for smoother viewport experience
- using `min-zoomed-font-size` to show labels only when needed for better performance
*/

$(function(){
  
  // get exported json from cytoscape desktop via ajax
  var graphP = $.ajax({
    url: 'https://rawgit.com/theresajbecker/CompBio/master/TokyosmallTest/Tokyosmall2.json', // tokyo-railways.json
    type: 'GET',
    dataType: 'json'
  });
  
  // // also get style via ajax
  // var styleP = $.ajax({
  //   url: 'https://cdn.rawgit.com/maxkfranz/2c23fe9a23d0cc8d43af/raw/', // tokyo-railways-style.cycss
  //   type: 'GET',
  //   dataType: 'text'
  // });
  
  // when both graph export json and style loaded, init cy

  Promise.all([ graphP ]).then(initCy);

  //Promise.all([ graphP, styleP ]).then(initCy);
  
  
  function initCy( then ){

    var loading = document.getElementById('loading');
    var expJson = then[0];
    //taking out style load
    //var styleJson = then[1];
    var elements = expJson.elements;
    console.log(loading )
    loading.classList.add('loaded');
    
    var cy = window.cy = cytoscape({
      container: document.getElementById('cy'),
      //changing layout to cola from { name: 'preset' },
       layout: {
        name: 'springy',
        padding: 10,
        edgeLength : 'data(weight)',
        },
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

    });

  }
});