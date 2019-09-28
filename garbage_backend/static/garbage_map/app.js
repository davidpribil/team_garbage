class RoiCollector {

    constructor(map) {
        this.map = map
        this.bounds = null
    }

    displayRoi(roi) {
        var poly;
        if (roi.geometry == 'Polygon') {
            poly = this.displayPolygon(roi.points, roi.color);
        }
        else {
            poly = this.displayPolyLine(roi.points, roi.color);
        }
        this.addPopup(poly, roi);
        return poly;
    }

    displayPolygon(latlngs, color) {
        var polygon = L.polygon(latlngs, { color: color }).addTo(this.map);
        this.handleBounds(polygon)
        return polygon;
    }

    displayPolyLine(latlngs, color) {
        var polyLine = L.polyline(latlngs, { color: color }).addTo(this.map);
        this.handleBounds(polyLine)
        return polyLine;
    }

    addPopup(poly, roi) {
        var ul = document.createElement("ul");
        for (let idx in roi.popupContent) {
            var li = document.createElement('li');
            ul.appendChild(li);
            li.innerHTML = roi.popupContent[idx]
        }
        poly.bindPopup(ul);
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