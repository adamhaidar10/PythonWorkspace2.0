<?php
    # connect to the database
    $con = mysqli_connect("localhost", "root", "root123", "cars");

    # run a query on the database
    $sql = "select * from our_cars";
    $res = mysqli_query($con, $sql);

    echo '<table cellpadding="10px" border="1px">';
    echo "<tr><th>Make</th><th>Model</th><th>City</th><th>Colour</th><th>Year</th><th></tr>";

    # loop through the results
    # show the output in the browser
    while($row = mysqli_fetch_array($res))
    {
        echo "<tr>";
        
        // echo "<td>" . $row['first_name'] . "</td><td>". $row['last_name'] . "</td>"  ;
        echo "<td>" . $row['first_name'] . "</td><td>". $row['last_name'] . "</td><td>". $row['city'] . "</td><td>" . $row['phone_number'] . "</td><td>" . $row['email_address'] . "</td>";


        echo "</tr>";
    }

    echo "</table>";

    # close everything
    mysqli_free_result($res);
    mysqli_close($con);    
?>