<?php
    # get the value entered by the user
    $firstname = $_POST['firstname'];
    // $lastname = $_POST['last_name'];
    // $city = $_POST['city'];
    // $number = $_POST['phone_number'];
    // $email = $_POST['email_address'];

    if (strlen($firstname) == 0)
    {
        echo "You must fill in all the fields";
        exit;
    }


    # connect to the database
    $con = mysqli_connect("localhost", "root", "root123", "onlineStore");

    echo "<h1>Search results</h1><br><hr><br>";

    # query the database
    $sql = "select first_name, last_name, city, phone_number, email_address from contacts where first_name like '%" . $firstname . "%'";

    echo $sql;
    echo "<br>";

    $res = mysqli_query($con, $sql);

    # do something with the results
    while($row = mysqli_fetch_array($res))
    {
        echo $row["first_name"] . " : " . $row["last_name"] . " : " . $row["city"] . " : " . $row["phone_number"] . " : " . $row["email_address"];
        echo "<hr>";
    }

    # close the connection
    mysqli_close($con);
?>