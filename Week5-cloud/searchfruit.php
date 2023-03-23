<?php
    # get the value entered by the user
    $fruitname = $_POST["fruitname"];

    if ( strlen($fruitname) == 0 )
    {
        echo "You must enter a search term";
        exit;
    }

    # connect to the database
    $con = mysqli_connect("localhost", "root", "root123", "fruitshop");

    echo "<h1>Search results</h1><br><hr><br>";

    # query the database
    $sql = "select fruit_name, fruit_quantity from fruit where fruit_name like '%" . $fruitname . "%'";

    echo $sql;
    echo "<br>";

    $res = mysqli_query($con, $sql);

    # do something with the results
    while($row = mysqli_fetch_array($res))
    {
        echo $row["fruit_name"] . " : " . $row["fruit_quantity"];
        echo "<hr>";
    }

    # close the connection
    mysqli_close($con);
?>