<?php
    # get the values that the user entered on the form
    $firstname = $_POST['first_name'];
    $lastname = $_POST['last_name'];
    $city = $_POST['city'];
    $number = $_POST['phone_number'];
    $email = $_POST['email_address'];

    if ((strlen($firstname) == 0) or (strlen($lastname) == 0) or (strlen($city) == 0) or (strlen($number) == 0) or (strlen($email) ==0))
    {
        echo "You must fill in all the fields";
        exit;
    }

    # connect to the database
    $con = mysqli_connect("localhost", "root", "root123", "onlineStore");

    #insert the values into the database
    $sql = "insert into contacts(first_name, last_name, city, phone_number, email_address) values('" . $firstname . "','" . $lastname . "','" . $city . "','" . $number . "','" . $email . "')";

    echo $sql;
    echo "<br>";

    if (mysqli_query($con, $sql))
    {
        echo "Thank you for inserting a new contact";
    }

    # close the connection
    mysqli_close($con);
?>