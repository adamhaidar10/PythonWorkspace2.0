<?php
    $make = $_POST['make'];
    $model = $_POST['model'];

    if ((strlen($make) == 0) && (strlen($model) == 0))
    {
        echo "You must fill in at least one field";
        exit;
    }

    $con = mysqli_connect("localhost", "root", "root123", "cars");

    $sql = "select * from our_cars where make like '%" . $make . "%' and model like '%" . $model ."%'";
    

    // $sql2 = "select * from our_cars where model like '%" . $model . "%'";


    echo "<br>";

    $res = mysqli_query($con, $sql);
    


    while($row = mysqli_fetch_array($res))
    {
        echo $row["make"] . " : " . $row["model"] . " : " . $row["colour"] . " : " . $row["year"] . " : " . $row["license_plate"] . " : " . $row["location"] . " : " . $row["purchased_from"] . " : " . $row["purchase_price"] . " : " . $row["selling_price"];

        echo "<hr>";
    }
   

    mysqli_close($con);

?>
