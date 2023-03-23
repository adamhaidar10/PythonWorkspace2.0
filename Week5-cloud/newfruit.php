<?php
    # get the values that the user entered on the form
    $fruitname = $_POST['fruitname'];
    $fruitquantity = $_POST['fruitquantity'];

    if ( (strlen($fruitname) == 0) or (strlen($fruitquantity) == 0) )
    {
        echo "You must fill in all the fields";
        exit;
    }

    # connect to the database
    $con = mysqli_connect("localhost", "root", "root123", "fruitshop");

    #insert the values into the database
    $sql = "insert into fruit(fruit_name, fruit_quantity) values('" . $fruitname . "', '" . $fruitquantity . "')";

    echo $sql;
    echo "<br>";

    if (mysqli_query($con, $sql))
    {
        echo "Thank you for inserting a new fruit";
    }

    # close the connection
    mysqli_close($con);
?>