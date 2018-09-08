'use strict';
mapboxgl.accessToken = 'pk.eyJ1IjoicmV1c3RsZSIsImEiOiJjamxzNnYwYjUwYzZ0M3BubTd2ZDRtNHFwIn0.PgxCjIEJpL2svw-dIA1npw';

// Init Map
var map = new mapboxgl.Map({
    container: 'rental-map-container',
    style: 'mapbox://styles/mapbox/dark-v9',
    zoom: 10,
    minZoom: 5,
    maxZoom: 19,
    center: {
        lng: 139.76534107288876,
        lat: 35.68811339789339
    }
    
});

// Disable map rotation using right click + drag
map.dragRotate.disable();

// Disable map rotation using touch rotation gesture
map.touchZoomRotate.disableRotation();

// Init map
map.on('load', function(){
    
    // Load json data
    
    fetch('results.geojson').then(response => {
        return response.json()
        
    }).then(locations => {
        
        locations.features.forEach(marker => {
            let typeProp = marker.properties.type.toLowerCase()
            
            var el = document.createElement('div')
            el.className = 'marker-' + typeProp
            
            new mapboxgl.Marker(el)
                .setLngLat(marker.geometry.coordinates)
                .addTo(map)
            
        })
        
    }).catch(err => {
        if(err){
            console.log(err)
            console.log('json error')
        }
    })
    
})
