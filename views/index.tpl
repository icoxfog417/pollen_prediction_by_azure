<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Pollen Forecast</title>

    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css" rel="stylesheet">
    <script src="//code.jquery.com/jquery-2.1.3.min.js"></script>
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>

</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-static-top" role="navigation">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <a class="navbar-brand" href="#">Pollen Forecast</a>
            </div>
        </div>
    </nav>

    <!-- Page Content -->
    <div class="container">
        <div class="row">
            <div class="col-lg-12 text-center">
                <h1>Pollen Forecast</h1>
                <p>Show forecasts at Tokyo.</p>
                <div>
                    <table class="table table-striped">
                        <thead>
                            <th>Date</th>                            
                            <th>Temperature</th>
                            <th>Rain</th>
                            <th>Wind Speed</th>
                            <th>Pollen Amout(/m3)</th>
                        </thead>
                    % for d in data:
                        % alert = "" if d["predict"] < 100 else "warning" if d["predict"] < 500 else "danger"
                        <tr class="{{alert}}">
                            <td>{{d["forecast"].date.strftime("%m/%d %H")}}時</td>
                            <td>{{d["forecast"].temp}}</td>
                            <td>{{d["forecast"].rain}}</td>
                            <td>{{d["forecast"].wind_speed}}</td>
                            <td>{{d["predict"]}}</td>
                        </tr>
                    % end                    
                    </table>
                </div>
            </div>
        </div>
        <!-- /.row -->

    </div>
    <!-- /.container -->
</body>
</html>