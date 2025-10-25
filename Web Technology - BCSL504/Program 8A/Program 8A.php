<!-- 8a. Develop a PHP program (with HTML/CSS) to keep track of the number of visitors
visiting the web page and to display this count of visitors, with relevant headings. -->

<?php
// File to store the visitor count
$counter_file = "counter.txt";
// Check if the file exists, if not create it
if (!file_exists($counter_file)) {
file_put_contents($counter_file, "0");
}
// Read the current count
$count = (int)file_get_contents($counter_file);
// Increment the count
$count++;
// Save the new count
file_put_contents($counter_file, $count);
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Visitor Counter</title>
<style>
body {
font-family: Arial, sans-serif;
background-color: #e8f0fe;
text-align: center;
padding-top: 50px;
}
.container {
background-color: #ffffff;
width: 400px;
margin: auto;
padding: 30px;
border-radius: 10px;
box-shadow: 0 0 10px #ccc;
}
h1 {
color: #003366;
}
p {
font-size: 20px;
color: #333;
}
.count {
font-size: 36px;
font-weight: bold;
color: #4CAF50;
}
</style>
</head>
<body>
<div class="container">
<h1>Welcome to My Website</h1>
<p>You are visitor number:</p>
<div class="count"><?php echo $count; ?></div>
</div>
</body>
</html>