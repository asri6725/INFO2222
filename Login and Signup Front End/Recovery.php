<?php
  if($POST["submitted"]){
    $url = "http://localhost:2000/login"
    //the above must be a url to a reset - for whoever is in charge of backend


    $email = $_POST["email"];

    $to = $email;

    $subject = "Reset your STUD HELP password";

    $message = "<p> You have recently requested to reset your password....";

    $message .= "<p> here is your reset link: <br>";

    $message .= '<a href = "' .$url . '">' .$url . '</a></p>';

    $headers = "From: STUD HELP <zane.artesi@hotmail.com>\r\n";
    //email hould be changed
    $headers.= "Reply-To: zane.artesi@hotmail.com\r\n";
    $headers.= "Content-type: text/html\r\n";

    mail($to, $subject, $message, $headers);

  }

 ?>
