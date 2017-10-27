<html>
	<head>
		<title>LEN Abstimmung</title>
	</head>

	<body>
		<?php	
			echo 'fertig ;)';
			$frage = htmlspecialchars($_POST["frage"]);
			$anzahl = htmlspecialchars($_POST["anzahl"]);
			$choise = htmlspecialchars($_POST["choise"]);
			exec($cmd . "python mentimeterN.py " . $frage . " " . $anzahl . " ". $choise);
		?>
	</body>
</html>