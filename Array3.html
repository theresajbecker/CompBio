
<html>
<head>
  <title>Springy.js image node demo</title>
</head>
<body>
<script src="jquery-1.11.3.js"></script>
<script src="springy.js"></script>
<script src="springyui.js"></script>

<!--<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>-->
     
<script/>  
$(document).ready(function(){
  $.ajax({
    url: 'https://rawgit.com/theresajbecker/CompBio/master/SuperSmallNodes.json',
    type: 'GET',
    dataType: 'json'
  }).done(function(graphP) {  
    
    console.log(graphP);

    
    var graph = new Springy.Graph();
    var nodeArray = []

    for ( i = 0  ; i < graphP.elements.nodes.length ; i++ ) { 
        var Nlabel1 =  graphP.elements.nodes[i].data.label
        var Nmass =  graphP.elements.nodes[i].data.mass

        var NN1 = graph.newNode({label: Nlabel1}, {'text-outline-width': Nmass});
        nodeArray.push(NN1)
        }
        console.log(nodeArray)

        function getByValue(arr, value) {
          for (var n=0; n < nodeArray.length; n++) {
          console.log("Testing call")
          console.log("value is")
          console.log(value)
          console.log("n is")
          console.log(n)
            if (arr[n].data.label == value) {
            console.log("below should be the object of element")
            return arr[n];
            }
          }
        }


        function getSourceNode(graphP) {
          for (var s=0; s < graphP.elements.edges.length; s++) {
          console.log("graphP.elements.edges.length")
          console.log(graphP.elements.edges.length)
            console.log("s is now")
            console.log(s)
            var getSource = graphP.elements.edges[s].data.source
            var getTarget = graphP.elements.edges[s].data.target
            console.log("Source")
            console.log(getSource)
            console.log("Target")
            console.log(getTarget)
            console.log("NNNNOOOOOOOODE ARRAY")
            console.log(nodeArray)
            console.log("getting value of source node array")
            graph.newEdge(getByValue(nodeArray, getSource),getByValue(nodeArray, getTarget));

        }
        }

    getSourceNode(graphP)

    
        console.log('WINDOW')
jQuery(function(){
  var springy = window.springy = jQuery('#springydemo').springy({
    graph: graph,
    nodeSelected: function(node){
      console.log('Node selected: ' + JSON.stringify(node.data));
    }
  });
}); 

    });  
        

});
</script>
    <div>
<canvas id="springydemo" width="800" height="400" style="border: 1px solid black;"></canvas>
</div>


</body>
</html>