function displayPolygon(map, latlngs) {
    var polygon = L.polygon(latlngs, { color: 'red' }).addTo(map);
    // zoom the map to the polygon
    map.fitBounds(polygon.getBounds());
}
