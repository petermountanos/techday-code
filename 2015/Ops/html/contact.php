
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Wantagh TechDay">
    <meta name="keywords" content="Wantagh, TechDay, technology, STEM, wantagh high school">
    <meta name="author" content="Wantagh TechDay">
    <link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">
    <link rel="icon" href="img/favicon.ico" type="image/x-icon">

    <title>Contact | Wantagh TechDay</title>

    <!-- Bootstrap core CSS -->
    <link href="dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/cover.css" rel="stylesheet">
    <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-56786861-1', 'auto');
  ga('require', 'displayfeatures');
  ga('send', 'pageview');

</script>
  </head>
  <body>
    <div class="site-wrapper">

      <div class="site-wrapper-inner">

        <div class="cover-container">

          <div class="masthead clearfix">
            <div class="inner">
              <nav>
                <ul class="nav masthead-nav">
                  <li><a href="index.php">Home</a></li>
                  <li><a href="info.php">Information</a></li>
                  <li><a href="http://goo.gl/forms/IMrYFTHm5i" target="_blank">Registration</a></li>
                  <li class="active"><a href="#">Contact</a></li>
                </ul>
              </nav>
            </div>
          </div>
          <div class="main">
            <h1>Contact</h1><hr>

            <?php

// Check for form submission:

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Form Validation:
    if (!empty($_POST['name']) && !empty($_POST['email']) && !empty($_POST['message'])) {

        $email_to = "wantagh.technology@gmail.com";
        $email_subject = "WEBSITE: Wantagh TechDay";
        $email_from = $_POST['email'];
        
        // Create Message
        $email_message = "Form details below.\n\n";
     
        function clean_string($string) {
            $bad = array("content-type","bcc:","to:","cc:","href");
            return str_replace($bad,"",$string);
        }
     
        $email_message .= "Name: ".clean_string($_POST['name'])."\n";
        $email_message .= "Email: ".clean_string($_POST['email'])."\n";
        $email_message .= "Comments: ".clean_string($_POST['message'])."\n";

        $headers = 'From: '.$email_from."\r\n".
        'Reply-To: '.$email_from."\r\n" .
        'X-Mailer: PHP/' . phpversion();

        // Send Message
        @mail($email_to, $email_subject, $email_message, $headers);

        // Print Results
        echo '<p style="color:green">Thank you for your message, we will get back to you as soon as possible!</p>';
    }
    else {
      echo '<p style="color:red;">Invalid form input, please try again.</p>';
    }
}
 // END 
?>
        
            <form role="form" method="post" action="contact.php">
  
              <div class="form-group">
                <label for="exampleInputPassword1">Name</label>
                  <input name="name" type="text" class="form-control" id="name_input" placeholder="Enter name"
                  value="<?php if(isset($_POST['name'])) echo $_POST['name'];?>">
              </div>

              <div class="form-group">
                <label for="exampleInputEmail1">Email address</label>
                  <input name="email" type="email" class="form-control" id="email_input" placeholder="Enter email"
                  value="<?php if(isset($_POST['email'])) echo $_POST['email'];?>">
              </div>
  
              <div class="form-group">
                <label for="message_input">Message</label>
                  <textarea name="message" class="form-control" id="message_input" rows="3" placeholder="Enter Mesage"
                  value="<?php if(isset($_POST['message'])) echo $_POST['message'];?>"></textarea>
                </div>
              
              <button type="submit" class="btn btn-default">Submit</button>
            </form>
          </div>
          
          <div class="mastfoot">
            <div class="inner">
              <p>Wantagh TechDay | January 10th, 2015 | <a href="https://twitter.com/wantaghTechDay">@WantaghTechDay</a></p>
            </div>
          </div>

        </div>

      </div>

    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="dist/js/bootstrap.min.js"></script>
    <script src="dist/js/docs.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="dist/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
