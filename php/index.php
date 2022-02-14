<?php
$file = file_get_contents("../conf/config.cfg");
preg_match_all("/(.*?)=(.*?)\s/",$file,$xx);
$host = $xx[2][0];
$user = $xx[2][1];
$password = $xx[2][2];
$database = $xx[2][3];
//创建连接
$conn = new mysqli($host,$user,$password,$database);
if ($conn->connect_error){
    die("连接失败:" . $conn->connect_error);
}
//echo "连接成功\n";
$sql = "select * from report";
$result = $conn->query($sql);
if ($result->num_rows > 0){
    while ($row = $result->fetch_assoc()){
        echo json_encode($row);
//        echo $row["content"] . "\n";
        break;
    }
}else{
    echo "0 无";
}

$conn->close();
