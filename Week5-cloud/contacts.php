<?php
    # connect to the database
    $con = mysqli_connect("localhost", "root", "root123", "onlineStore");

    # run a query on the database
    $sql = "SELECT * FROM contacts";
    $res = mysqli_query($con, $sql);

    echo '<table cellpadding="10px" border="1px">';
    echo "<tr><th>First Name</th><th>Last Name</th><th>City</th><th>Phone Number</th><th>Email Address</th></tr>";

    # loop through the results
    # show the output in the browser
    while($row = mysqli_fetch_array($res))
    {
        echo "<tr>";
        echo "<td>" . $row['first_name'] . "</td><td>" . $row['last_name'] . "</td><td>" . $row['city'] . "</td><td>" . $row['phone_number'] . "</td><td>" . $row['email_address'] . "</td>";
        echo "</tr>";
    }

    echo "</table>";

    # close everything
    mysqli_free_result($res);
    mysqli_close($con);


?>
