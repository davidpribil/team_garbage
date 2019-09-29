$(function () {
    $('input[name="predict_date"]').daterangepicker({
        singleDatePicker: true,
        showDropdowns: true,
        minYear: 1901,
        maxYear: parseInt(moment().format('YYYY'), 10),
    }, function (start, end, label) {
        console.log(start.toDate());
        $.ajax({
            url: 'calcResults',
            type: 'GET',
            data: {
                date: start.toDate().toLocaleDateString()
            },
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function (result) {
                // Set prediction string
                document.getElementById('predict_id').innerHTML = result.prediction;
                // Set events
                let ul = document.getElementById('events_ul');
                ul.innerHTML = '';
                for (let idx in result.events) {
                    let li = document.createElement('li');
                    li.innerHTML = result.events[idx];
                    ul.appendChild(li);
                }
                // Set rois
                // Clear old ones
                $('.leaflet-interactive').remove();
                var map = garbageMap;
                let collector = new RoiCollector(map);
                for (let idx in result.rois) {
                    let roi = result.rois[idx];
                    collector.displayRoi(roi);
                }
                collector.centerMap();
            }
        });
    });
});