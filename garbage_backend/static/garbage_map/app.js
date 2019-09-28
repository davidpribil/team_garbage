class RoiCollector {

    constructor(map) {
        this.map = map
        this.bounds = null
    }

    displayPolygon(latlngs) {
        var polygon = L.polygon(latlngs, { color: 'red' }).addTo(this.map);
        this.handleBounds(polygon)
        return polygon;
    }

    displayPolyLine(latlngs) {
        var polyLine = L.polyline(latlngs, { color: 'red' }).addTo(this.map);
        this.handleBounds(polyLine)
        return polyLine;
    }

    handleBounds(poly) {
        let bounds = poly.getBounds();
        if (this.bounds === null) {
            this.bounds = bounds;
        } else {
            this.bounds.extend(bounds);
        }
    }

    centerMap() {
        this.map.maxZoom = 15;
        this.map.fitBounds(this.bounds);
    }

}