function add_chart() {
    console.log("Creating chart");
    Highcharts.setOptions({
      global: {
        useUTC: false
      }
    });
    chart = new Highcharts.Chart({
      chart: {
        alignTicks: false,
        renderTo: 'container',
        type: 'spline',
        marginRight: 10,
        backgroundColor: 'transparent',
        events: {
        },
        resetZoomButton: {

        },
        resetZoomButton: {},
        zoomType: 'x'
        // width: 1500,
        // scrollablePlotArea: {
        //     minWidth: 1500,
        //     opacity: 0,
        //     scrollPositionX: 1
        // }
      },
      title: {
        style: {color: '#EDC521'}, 
        text: 'Select a Stock'
      },
      xAxis: {
        min: Date.parse(new Date()) - 1 * 60 * 1000,
        type: 'datetime',
        tickPixelInterval: 150,
        // tickInterval: 3600*1000,
        plotLines: [{
            value: 0,
            width: 1,
            color: '#CCCCCC'
          }],
        labels: {
            style: {color: '#CCCCCC'}
        }
      },
      yAxis: {
        title: {
          text: 'Price：$',
          style: {color: '#CCCCCC'}, 
        },
        plotLines: [{
          value: 0,
          width: 1,
          color: '#CCCCCC'
        }],
        gridLineColor: '#CCCCCC',
        labels: {
            style: {color: '#CCCCCC'}
        }
      },
      tooltip: {
        formatter: function () {
          return '<b>' + this.series.name + '</b><br/>' +
            Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
            Highcharts.numberFormat(this.y, 2);
        }
      },
      legend: {
        enabled: true
      },
      exporting: {
        enabled: true
      },
      series: [],
    });
  };