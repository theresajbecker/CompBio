$(function(){ // on dom ready

var cy = cytoscape({
  container: $('#cy')[0],
  
  style: cytoscape.stylesheet()
    .selector('node')
      .css({
        'content': 'data(name)',
        'text-valign': 'center',
        'color': 'white',
        'text-outline-width': 2,
        'text-outline-color': '0D3281',
        'background-color': 'yellow',
        'border-width': 3,
        'border-color': 'red'
      })
    .selector('edge')
      .css({
        'width': 2,
        'line-color': '#A901DB',
        'edgeLength': 'data(weight)'
      })
    .selector(':selected')
      .css({
        'background-color': 'black',
        'line-color': 'black',
        'target-arrow-color': 'black',
        'source-arrow-color': 'black',
        'text-outline-color': 'black'
      }),
  
  elements: {
    nodes: [
      { data: { id: 'desktop', name: 'Cytoscape', href: 'http://cytoscape.org' } },
      { data: { id: 'js', name: 'Cytoscape.js', href: 'http://js.cytoscape.org' } },
      { data: { id: '1', name: 'Node1', href: 'https://www.youtube.com/watch?v=QL6Ws4i07is'} },
      { data: { id: '2', name: 'Node2'} },
      { data: { id: '3', name: 'Node3'} },
      { data: { id: '4', name: 'Node4'} },
      { data: { id: '5', name: 'Node5'} },
      { data: { id: '6', name: 'Node6'} },
      { data: { id: '7', name: 'Node7'} },
    ],
    edges: [
      { data: { source: 'desktop', target: 'js' } },
      { data: { source: 'js', target: '1' } },
      { data: { source: '2', target: '1' } },
      { data: { source: '2', target: '3' } },
      { data: { source: '3', target: '4' } },
      { data: { source: '4', target: '5' } },
      { data: { source: '5', target: '6' } },
      { data: { source: '6', target: '7' } },
      { data: { source: 'js', target: '7' } },
      { data: { source: '4', target: 'js' } },
      { data: { source: '2', target: '5', weight: 0 } },
      { data: { source: '2', target: '7', weight: 100 } },
    ]
  },
  
  layout: {
    name: 'cose',
    padding: 10,
    edgeElasticity : 100
  }
});
  
cy.on('tap', 'node', function(){
  try { // your browser may block popups
    window.open( this.data('href') );
  } catch(e){ // fall back on url change
    window.location.href = this.data('href'); 
  } 
});

}); // on dom ready