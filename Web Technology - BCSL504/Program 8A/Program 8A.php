<?php
$counterFile = "counter.txt";

if (!file_exists($counterFile)) {
    file_put_contents($counterFile, "0");
}

$currentCount = file_get_contents($counterFile);

$newCount = $currentCount + 1;

file_put_contents($counterFile, $newCount);
?>

<!DOCTYPE html>
<html lang="en">

<head>

    <title>Visitor Counter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 100vh;
            background-color: #f4f4f9;
            color: #333;
        }

        .container {
            background: #fff;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            margin: 0 auto;
            width: 60%;
        }

        h1 {
            font-size: 2.5em;
            margin: 0;
        }

        p {
            font-size: 1.2em;
            color: #555;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Welcome to Our Website!</h1>
        <p>You are visitor number: <strong><?php echo $newCount; ?></strong></p>
    </div>
</body>

</html>