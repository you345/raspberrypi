<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>LedTest</title>
        <!-- BootstrapのCSSを読み込み -->
        <link href="css/bootstrap/bootstrap.css" rel="stylesheet">
        <!-- BootstrapのJSを読み込み -->
        <!-- ※必ず先にJQueryを読み込む -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- ※その後にBootstrapのJSを読み込む -->
        <script src="js/bootstrap.min.js"></script>　　　　　　　　　　　　　　　　　　　　　　　　　　　
    </head>
<body>
<?php
if(isset($_POST["start"])) {
        echo "<p>LED Light ON</p>";
        $path ='python /home/pi/ledstart.py';
        exec($path);
}
else if(isset($_POST["stop"])) {
        echo "<p>LED Light OFF</p>";
        $path ='python /home/pi/ledstop.py';
        exec($path);
}

?>

<div class="container">
	<div class="row">	
		<div class="col-md-4">    <!-- 12分割中4を割り当て -->
			12分割中4を割り当て

<form method="POST" action="">
<input type="submit" value="start" name="start">　
<input type="submit" value="stop" name="stop">　
</form>
		</div>
		<div class="col-md-4">    <!-- 12分割中4を割り当て -->
			12分割中4を割り当て
<form method="POST" action="">
<input type="submit" value="start" name="start">　
<input type="submit" value="stop" name="stop">　
</form>
		</div>
		<div class="col-md-4">    <!-- 12分割中4を割り当て -->
			12分割中4を割り当て
<form method="POST" action="">
<input type="submit" value="start" name="start">　
<input type="submit" value="stop" name="stop">　
</form>
		</div>
	</div>
</div>
</body>
</html>
