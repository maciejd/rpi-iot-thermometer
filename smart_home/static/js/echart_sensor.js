// Get temperature & humidity 
$(document).ready(
    function() {
        function update_display(temperature, humidity) {
            var date_time = new Date().toLocaleString();
            console.log('DateTime:' + date_time +' Temp:' + temperature + '*C ' + 'Hum:' + humidity);
             // 更新label
             if (temperature != null) {
                $("#text_temperature").html("<b>温度: </b>" + temperature + " *C");
             }
             if (humidity != null) {
                $("#text_humidity").html("<b>湿度: </b>" + humidity + " %");
             }
             $("#refresh_time").html("最新更新时间: " + date_time);
        }

        $("#btn-refresh").click(
            function() {
                console.log('btn-refresh-click');
                $.get("/refresh_data", function(data, status) {
                    console.dir(data);
                    var temperature = data["temperature"];
                    var humidity = data["humidity"];
                    // 弹窗
                    alert("已刷新, 温度:" +  temperature + " *C" + " 湿度:" + humidity + " %");
                    // 更新label
                    update_display(temperature, humidity);
                }
                );	
            }
        );
        
        // // create EChart
        // // https://www.cnblogs.com/Dreamer-1/p/5530221.html
        // var myChart = echarts.init(document.getElementById("chart"));
        // chart_option = {
        //     title: {
        //         text: '温度变化趋势'
        //     },
        //     tooltip: {
        //         trigger: 'axis'   // 坐标轴触发提示框
        //     },
        //     legend: {
        //         show: true,
        //         data: ['温度 (℃)', '湿度 (%)']
        //     },

        //     color: [
        //         '#FF3333',		// 温度变化曲线
        //         '#53FF53'		// 湿度变化曲线
        //     ],

        //     xAxis: {
        //         data: []
        //     },

        //     yAxis: [
        //         {
        //             type: 'value',
        //             name: '温度',
        //             max: 40,
        //             min: -10,
        //             axisLabel: {
        //                 formatter: '{value} ℃'
        //             }
        //         },
        //         {
        //             type: 'value',
        //             name: '湿度',
        //             max: 100,
        //             min: 0,
        //             axisLabel: {
        //                 formatter: '{value} %'
        //             }
        //         }
        //     ],
        //     series: [
        //         {
        //             name: '温度 (℃)',
        //             type: 'line',
        //             smooth: true,
        //             yAxisIndex: 0,
        //             data: []
        //         },

        //         {
        //             name: '湿度 (%)',
        //             type: 'line',
        //             symbol: 'emptyrect',
        //             yAxisIndex: 1,  // 第2个y axis
        //             data: []
        //         }
        //     ]
        // };
        // myChart.setOption(chart_option);
        // myChart.showLoading();  // 数据加载之前显示loading画面
        // var tems = [];		// 存放温度的数组
        // var hums = [];		// 存放湿度的数组
        // var dates = [];		// 时间数组

        // setInterval(function(){
        //     $.get("/refresh_data", function(data, status) {
        //         var temperature = data["temperature"];
        //         var humidity = data["humidity"];
        //         tems.push(temperature);
        //         hums.push(humidity);
        //         dates.push(new Date().toLocaleString());

        //         // 更新label
        //         $("#text_temperature").html("<b>温度: </b>" + temperature + " *C");
        //         $("#text_humidity").html("<b>湿度: </b>" + humidity + " %");
        //         $("#refresh_time").html("最新更新时间: " + new Date().toLocaleString());
        //         myChart.hideLoading();  // 隐藏加载动画
        //         // 更新Echart
        //         myChart.setOption(
        //             {
        //                 xAxis: {
        //                     data: dates    // 填入x轴数据
        //                 },

        //                 series: [
        //                     {
        //                         // 根据name对应相应的系列
        //                         name: '温度',    
        //                         data: tems
        //                     },
        //                     {
        //                         name: '湿度',
        //                         data: hums
        //                     }
        //                 ]
        //             }
        //         );
        //     })

        // }, 20000);

        var websocket_url = location.protocol + '//' + document.domain + ':' + location.port + '/sensor_temperature';
        console.info('SocketURL:' + websocket_url);
        var socketio = io.connect(websocket_url);

        socketio.on('connect', function() {
            console.log('Server is connected!');
        });

        socketio.on('disconnect', function() {
            console.log('Server is disconnected!');
        });

        socketio.on('server_response_sensor_temperature', function(res) {
            var temperature = res.temperature;
            var humidity = res.humidity;
            var date_time = new Date().toLocaleString();
            console.log('DateTime:' + date_time +' Temp:' + temperature + '*C ' + 'Hum:' + humidity);
            // 更新label
            update_display(temperature, humidity);
        });
    }
);
