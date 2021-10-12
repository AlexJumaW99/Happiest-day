import pandas 
import justpy as jp

df = pandas.read_csv('reviews.csv',parse_dates=['Timestamp'])
df['Weekday'] = df['Timestamp'].dt.strftime('%A')
df['Daynumber'] = df['Timestamp'].dt.strftime('%w')
df = df[df['Rating'] > 4.0]
print(df)

happiest_day = df.groupby(['Weekday', 'Daynumber'])['Rating'].count().reset_index()
happiest_day = happiest_day.sort_values('Daynumber')
print(happiest_day)

chart_def = '''
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Percentage of total Ratings by Course'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Percentage of Total Ratings ',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
'''

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Course Review Analysis', classes = 'text-h3 text-center')
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc_data = [{'name':v1, 'y':v2} for v1,v2 in zip(happiest_day['Weekday'],happiest_day['Rating'])]
    hc.options.series[0].data = hc_data

    return wp

jp.justpy(app)

