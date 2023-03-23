<?php
$make = $_POST['make'];
$model = $_POST['model'];
$colour = $_POST['colour'];
$year = $_POST['year'];
$license_plate = $_POST['plate'];
$location = $_POST['location'];
$purchased_from = $_POST['purchasedfrom'];
$purchase_price = $_POST['purchaseprice'];
$selling_price = $_POST['sellingprice'];

    if ((strlen($make) == 0) or (strlen($model) == 0) or (strlen($colour) == 0) or (strlen($year) == 0) or (strlen($license_plate) ==0) or (strlen($location) == 0) or (strlen($purchased_from) == 0) or (strlen($purchase_price) == 0) or (strlen($selling_price)== 0))
    {
        echo "You must fill in all the fields";
        exit;
    }

    # connect to the database
    $con = mysqli_connect("localhost", "root", "root123", "cars");

    #insert the values into the database
    $sql = "insert into our_cars(make, model, colour, year, license_plate, location, purchased_from, purchase_price, selling_price) values('" . $make . "','" . $model . "','" . $colour . "','" . $year . "','" . $license_plate . "','" . $location . "','" . $purchased_from . "','" . $purchase_price . "','" . $selling_price . "')";

    
    echo "<br>";

    if (mysqli_query($con, $sql))
    {
        echo "Thank you for inserting a new car";
    }

    # close the connection
    mysqli_close($con);

    
?>