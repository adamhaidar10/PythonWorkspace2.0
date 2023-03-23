<?php
    # get the value entered by the user
    $license_plate = $_POST['license'];
   
    if (strlen($license_plate) == 0)
    {
        echo "You must fill in the field";
        exit;
    }


    # connect to the database
    $con = mysqli_connect("localhost", "root", "root123", "cars");

    echo "<h1>Search results</h1><br><hr><br>";

    # query the database
    $sql = "select * from our_cars where license_plate like '%" . $license_plate . "%'";

    
    echo "<br>";

    $res = mysqli_query($con, $sql);

    # do something with the results
    while($row = mysqli_fetch_array($res))
    {
        echo $row["make"] . " : " . $row["model"] . " : " . $row["colour"] . " : " . $row["year"] . " : " . $row["license_plate"] . " : " . $row["location"] . " : " . $row["purchased_from"] . " : " . $row["purchase_price"] . " : " . $row["selling_price"];

        echo "<hr>";
    }

    # close the connection
    mysqli_close($con);
?>