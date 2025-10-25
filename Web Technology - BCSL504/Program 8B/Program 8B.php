<!-- 8b. Develop a PHP program (with HTML/CSS) to sort the student records which are stored
in the database using selection sort. -->

Sql file
CREATE DATABASE IF NOT EXISTS school;
USE school;
CREATE TABLE IF NOT EXISTS students (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
marks INT NOT NULL
);
INSERT INTO students (name, marks) VALUES
('Alice', 82),
('Bob', 76),
('Charlie', 91),
('David', 68),
('Eva', 89);
.php file
<?php
// Database connection
$conn = new mysqli("localhost", "root", "", "school");
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}
// Fetch student data from database
$result = $conn->query("SELECT * FROM students");
$students = array();
if ($result->num_rows > 0) {
while ($row = $result->fetch_assoc()) {
$students[] = $row;
}
}
// Selection Sort on marks
$n = count($students);
for ($i = 0; $i < $n - 1; $i++) {
$min_idx = $i;
for ($j = $i + 1; $j < $n; $j++) {
if ($students[$j]['marks'] < $students[$min_idx]['marks']) {
$min_idx = $j;
}
}
// Swap
$temp = $students[$i];
$students[$i] = $students[$min_idx];
$students[$min_idx] = $temp;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Sorted Student Records</title>
<style>
body {
font-family: Arial, sans-serif;
background-color: #eef;
padding: 20px;
text-align: center;
}
table {
margin: auto;
border-collapse: collapse;
width: 60%;
background-color: #fff;
box-shadow: 0 0 10px #aaa;
}
th, td {
padding: 12px;
border: 1px solid #444;
}
th {
background-color: #003366;
color: white;
}
tr:nth-child(even) {
background-color: #f2f2f2;
}
h2 {
color: #003366;
}
</style>
</head>
<body>
<h2>Student Records Sorted by Marks (Ascending)</h2>
<table>
<tr>
<th>ID</th>
<th>Name</th>
<th>Marks</th>
</tr>
<?php foreach ($students as $student): ?>
<tr>
<td><?php echo $student['id']; ?></td>
<td><?php echo htmlspecialchars($student['name']); ?></td>
<td><?php echo $student['marks']; ?></td>
</tr>
<?php endforeach; ?>
</table>
</body>
</html>
<?php $conn->close(); ?>
