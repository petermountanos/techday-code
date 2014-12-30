
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Wantagh TechDay">
  <meta name="keywords" content="Wantagh, TechDay, technology, STEM, wantagh high school">
  <meta name="author" content="Wantagh TechDay">
  <title>Information | Wantagh TechDay</title>

  <!--include bootstrap -->
  <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
  <link href="dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="css/styles.css" rel="stylesheet">
  <link href="css/carousel.css" rel="stylesheet">
  <link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">
  <link rel="icon" href="img/favicon.ico" type="image/x-icon">
  <script src="js/customtabs.js"></script>
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

<body data-spy="scroll" data-target=".navbar">
  <div class="container">
    <nav id="top_fixed_nav" class="navbar navbar-default navbar-fixed-top navbar-inverse" role="navigation">
        <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
            <a class="navbar-brand" href="index.php"><strong>Wantagh TechDay</strong></a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li><a href="index.php">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#sections">Sections</a></li>
            <li><a href="#registration">Registration</a></li>
          </ul>

          <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-target="#" data-toggle="dropdown" role="button" aria-expanded="false"
              aria-labelledby="bs-example-navbar-collapse-1">More <span class="caret"></span></a>
              <ul class="dropdown-menu" role="menu">
                <li role="presentation" class="dropdown-header">Links</li>
                <li><a href="index.php">Home</a></li>
                <li><a href="http://goo.gl/forms/OwYrfpmwIM" target="_blank">Student Form</a></li>
                <li><a href="http://goo.gl/forms/344IE4vf8C" target="_blank">Teacher Form</a></li>
                <li><a href="http://goo.gl/forms/344IE4vf8C" target="_blank">Volunteer Form</a></li>
                <li class="divider"></li>
                <li role="presentation" class="dropdown-header">Social Media</li>
                <li><a href="http://facebook.com/wantaghtechday" target="_blank">Facebook</a></li>
                <li><a href="http://twitter.com/wantaghTechDay" target="_blank">Twitter</a></li>
                <li><a href="contact.php">Contact Us</a></li>                 
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div id="myCarousel" class="carousel slide" data-ride="carousel">
      <!-- Indicators -->
      <ol class="carousel-indicators">
        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
        <li data-target="#myCarousel" data-slide-to="1"></li>
        <li data-target="#myCarousel" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner" role="listbox">
        <div class="item active">
          <img src="img/carousel/IMG_9301.JPG" alt="First slide">
          <div class="container">
            <div class="carousel-caption">
              <h1 style="font-weight:bold;">Learn</h1>
              <p style="font-weight:bold;">Exposing students to computer science education in grades K-12 gives them critical thinking skills needed for their success in the 21st century and for strengthening the workforce.</p>
              <p><a class="btn btn-lg btn-primary" href="http://goo.gl/forms/OwYrfpmwIM" role="button" target="_blank">Register today!</a></p>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="img/carousel/IMG_9241.JPG" alt="Second slide">
          <div class="container">
            <div class="carousel-caption">
              <h1 style="font-weight:bold;">Innovate</h1>
              <p style="font-weight:bold;">Computer science enables innovation, economic growth and is an integral element of culture. It shapes how people interact with each other and the world around them, and it impacts jobs, health care, national defense and energy, among other fields.</p>
              <p><a class="btn btn-lg btn-primary" href="http://goo.gl/forms/OwYrfpmwIM" role="button" target="_blank">Register today!</a></p>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="img/carousel/IMG_9317.JPG" alt="Third slide">
          <div class="container">
            <div class="carousel-caption">
              <h1 style="font-weight:bold;">Collaborate</h1>
              <p style="font-weight:bold;">The Bureau of Labor Statistics projects that by the year 2020, there will be 4.2 million jobs in computing and information technology in the U.S., putting these fields among the fastest growing occupational fields.</p>
              <p><a class="btn btn-lg btn-primary" href="http://goo.gl/forms/OwYrfpmwIM" role="button" target="_blank">Register today!</a></p>
            </div>
          </div>
        </div>
      </div>
      <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div><!-- /.carousel -->

        <section id="about">
          <h1>About</h1>
          <article style="padding-top:35px;padding-bottom:35px;">
          <p align="justify">
            Wantagh TechDay is an annual event created by Wantagh School District alumni to promote computer science education.  
            Motivated by <u><a href="http://code.org">code.org’s initiative</a></u>, the Wantagh TechDay team seeks to provide
            the opportunity for exposure to the practical skills of computer science that students could otherwise miss out on.  
            As computers become smaller, more efficient and more powerful, they will exert a stronger influence in all fields 
            and it will become necessary to understand basic notions of how they work and how they can be used. But beyond just 
            giving students a useful tool, we hope to cultivate the joy and enthusiasm we ourselves feel for this rewarding approach 
            to problem solving. Most importantly, when approached the right way, computer science can be fun and our ultimate goal is
            to share the amusement!
          </p>
          <p align="justify">
            Wantagh TechDay exposes students in <strong>5th - 12th grade</strong> to computer science through a project-oriented day in which 
            they learn and utilize a broad array of skills.  Students are organized into small classes based on their experience levels
            and receive instruction from a lecturer and classroom assistants.  By the end of the day, students will have completed a 
            project that will remain accessible.  It is our hope that students will also walk away with the inspiration and ingenuity 
            to attempt a project of their own.            
          </p> <br>

          <ul class="nav nav-tabs">
            <li class="active"><a href="#who" data-toggle="tab">Who</a></li>
            <li><a href="#when" data-toggle="tab">When</a></li>
            <li><a href="#where" data-toggle="tab">Where</a></li>
            <li><a href="#why" data-toggle="tab">Why</a></li>
            <li><a href="#how" data-toggle="tab">How</a></li>
            <li><a href="#teachers" data-toggle="tab">Teachers</a></li>
          </ul>

            <div class="tab-content">
              <div class="tab-pane active" id="who">
                <h3>Wantagh Students Grades 5 - 12</h3><br>
                <p align="justify">
                    After the overwhelming positive feedback from TechDay 2014, and a Brown Bag Seminar at Wantagh Elementary School, 
                    the members of the TechDay team felt that the invitation should be extended to 5th graders as well. Therefore, 
                    Wantagh students in grades <strong>5 - 12</strong> are eligible to sign up. However, please note that 5th grade students <i>must</i> be picked up
                    by a parent or legal guardian at the conclusion of the event. There are no other requirements for signing up other than
                    being excited to learn! So don't worry if you have no prior experience with coding, most of the students won't - there's no
                    reason to be intimidated or feel like you don't know enough to come. 
                </p>
              </div>

              <div class="tab-pane" id="when">
                <h3>Saturday, January 10th, 2015</h3> <br>
                <p align="justify">
                  Wantagh TechDay will be taking place on Saturday, January 10th, 2015 from the hours of 11:00 A.M. to 4:00 P.M.
                  While the actual schedule won’t be finalized until after registration has closed, feel free to check out 
                  <a href="img/schedule_2014.pdf" target="_blank"><u>last year’s schedule</u></a> here to get a general idea of 
                  what you or your child will be doing.
                </p>
              </div>
              <div class="tab-pane" id="where">
                <h3>Wantagh High School</h3> <br>
                <p align="justify">
                    Wantagh TechDay will be taking place at Wantagh High School, which is located at:
                    <address style="align:center">
                      <strong>Wantagh High School</strong><br>
                      3301 Beltagh Avenue<br>
                      Wantagh, NY 11793<br>
                    </address>
                    After registration, you will be given a schedule that outlines specific room numbers and 
                    which course section you have been placed in. 
                </p>
              </div>
              
              <div class="tab-pane" id="why">
                <h3>Learning to code is important!</h3> <br>
                <p align="justify">
                    Computer Science is one of the fastest growing fields in the modern world. With an estimated 1.4 
                    million new computer science jobs expected over the next 10 years, as well as the assimilation of 
                    tech startup founders into pop culture, one would expect to see the supply of qualified computer 
                    programmers skyrocketing as well. Yet there is expected to be only 400,000 qualified candidates 
                    to fill such positions. This discrepancy is alarming, yet at the same time it provides educators – 
                    especially at the primary and secondary levels – with the opportunity to better equip students for 
                    success in emerging and expanding job markets. 
                </p>
              </div>

              <div class="tab-pane" id="how">
                <h3>Register Today!</h3> <br>
                <p align="justify">
                  If you are interested in technology, we highly encourage you to sign up today! As time progresses, the 
                  ability to code will only become a more and more valuable skill. Like learning any language, it is always 
                  best to start young. Check out the <a href="#registration"><u>registration section</u></a> to find out how
                  to sign up!
                </p>
              </div>

            <div class="tab-pane" id="teachers">
              <h3>Wantagh TechDay Team</h3> <br>
                <p align="justify">
                  The Wantagh TechDay team is composed of Wantagh High School Alumni who have a passion for technology, 
                  and are eager to share their knowledge with fellow students. Most are computer science majors or minors, 
                  but we also have a few who are completely self-taught! Our teachers come from schools like Brown University,
                  University of Delaware, Duke University, Hofstra University, New York University, University of Pennsylvania, 
                  Stony Brook University, and Villanova University. We even have a senior from Wantagh High School on our team! 
                  If you’re interested in joining our team, please see the <a href="#registration"><u>registration section</u></a> 
                  below.
                </p>
            </div>
          </div>
          </article>
        </section>

        <section id="sections">
			<h1>Sections</h1>
			<article style="padding-top:35px;padding-bottom:35px;">
      <p align="justify">
        This year, we have not yet devoted specific sections to register for. Based on feedback from students, we will be placing students in specific sections based on experience level and interests. We want to maximize everyone’s potential through this event, so by grouping you with similar students, we can personalize the curriculum to that group’s interests and skill level. However, you shouldn’t be hesitant to register if you have no experience, most of the students who will register won’t have any either!  After you’ve received your placement and you feel that you’ve been placed in the wrong section, we are very flexible and will work with you to find the appropriate place for you.
      </p>
      <p align="justify">
        If you would like to get an idea of what potential section you can be enrolled in, we’ve outlined last year’s sections below. We will most likely be using Scratch and Python again, so if you’d like to get a head start, you should check out the projects below! Don’t get intimidated by it though, all of our students were able to complete their projects last year, and most had never even heard of coding before!
      </p>
      <br>
			<ul class="nav nav-tabs">
	        	<li class="active"><a href="#cs001" data-toggle="tab">CS.001</a></li>
	        	<li><a href="#cs002" data-toggle="tab">CS.002</a></li>
	        	<li><a href="#cs003" data-toggle="tab">CS.003</a></li>
			</ul>

			<div class="tab-content">
		          <div class="tab-pane active" id="cs001">
		          <article class="bs-callout" >
		            <h4 style="float:left">CS.001 Introduction to Scratch</h4>
		            <br><br>
		            <p style="float:left"><em>Instructors: Anthony Consoli, Chris Fiscella, Richard Myers, Paulina Renda</em></p>
		            <br><p></p>
		              <ul>
		                <li>
		                  The beginner-level course required absolutely no prior experience, and was recommended for 6th - 8th graders. 
		                  Students learned how to think like a programmer through MIT’s Scratch programming language - specially designed
		                  to help educate students in computer programming. Our only expection for CS.001 was for students to be exited to learn!
		                </li>
		                <li>
        							<strong>Project: </strong><u><a href="http://scratch.mit.edu/projects/3310840/" target="_blank">Super Swimmer</a></u> is a game
        							that was created by our team in order to introduce the basics of programming to students. It has become quite popular
        							throughout the Scratch community. In this course, each student was given their own Scratch account, and after implementing
        							some of the Super Swimmer functionality, they were able to expand upon the game. Feel free to "remix" this project!
        						</li>
                    <li>
                      <strong>Resources: </strong> Here are links to the <u><a href="img/cs001_slides.pdf" target="_blank">powerpoint presentation 
                      </a></u>used, and the <u><a href="img/cs001_cheat.pdf" target="_blank">cheat sheet</a></u> given out, enjoy!
                    </li>
		              </ul>
				</article>
				</div>
					
				<div class="tab-pane" id="cs002">
				<article class="bs-callout" >
					<h4 style="float:left">CS.002 Introduction to Python</h4>
					<br><br>
					<p style="float:left"><em>Instructors: Daniel Charytonowicz & Kenny Peluso</em></p>
					<br><p></p>
					<ul>
						<li>
							The intermediate course was recommended for beginning students in high school
							or middle school students who show a particular aptitude for math and science.
							The course again stressed teaching the same logical tools to help students
							think like programmers. It was taught in Python, which is more advanced
							than Scratch.
						</li>
						<li>
							<strong>Project: </strong><u><a href="http://en.wikipedia.org/wiki/Blackjack">Blackjack</a></u>
							is a popular card game, in fact, according to Wikipedia it is the most widely played casino banking game in 
							the world. We had students recreate the basics of this game in Python, with the help of some code adapted from
							Allan Lavell at Pygame. If you'd like to download the source code for the project, you can find it here: 
							<u><a href="src/blackjack.zip">Blackjack Source Code</a></u>.
						</li>
            <li>
              <strong>Resources: </strong> Here are links to the <u><a href="img/cs002_slides.pdf" target="_blank">powerpoint presentation 
              </a></u>used, enjoy!
            </li>
					</ul>
				</article>
				</div>

				<div class="tab-pane" id="cs003">
				<article class="bs-callout" >
					<h4 style="float:left">CS.003 Advanced Introduction to Python</h4>
					<br><br>
					<p style="float:left"><em>Instructors: Peter Mountanos & Sean Whiteman</em></p>
					<br><p></p>
					<ul>  
						<li>
							The advanced course was recommended for those with prior computer
							science experience or those with a strong background in math or sciences.  
							Because of the accelerated and relatively advanced nature of the course, students
							would've ideally had taken an honors or AP course in the sciences or in math. The
							course was taught in Python and covered more ground than CS.002.
						</li>
						<li>
							<strong>Project: </strong><u><a href="http://en.wikipedia.org/wiki/Breakout_(video_game)">Breakout</a></u>
							was a popular 1970's video game made by Atari. We had students recreate this game in Python, with the help
							of some code adapted from Professor Walker White at Cornell University. If you'd like to download the source
							code for the project, you can find it here: <u><a href="src/breakout.zip">Breakout Source Code</a></u>.
						</li>
            <li>
              <strong>Resources: </strong> Here are links to the <u><a href="img/cs003_slides.pdf" target="_blank">powerpoint presentation 
              </a></u>used, <u><a href="img/cs003_instructions.pdf" target="_blank">instructions</a></u> and the <u><a href="img/cs003_cheat.pdf" target="_blank">cheat sheet</a></u> given out, enjoy!
            </li>
					</ul>
				</article>
				</div>
			</div>
        </section>

        <section id="registration">
          <h1>Registration</h1>
          <article style="padding-top:35px;padding-bottom:35px;">
          <p align="justify">
            Registration for Wantagh TechDay 2015 is scheduled to take place between <strong>Tuesday, November 18th, 2015</strong> and 
            <strong>Friday, December 12th, 2014</strong>. Interested students and parents can fill out a <u><a href="http://goo.gl/forms/OwYrfpmwIM"
            target="_blank">registration form here</a></u>. To help better shape the curriculum to students’ interests and abilities,
            we ask for relevant background information and experience, as well as standard contact information. For any questions,
            comments or concerns, please feel free to email <u><a href="mailto:wantagh.technology@gmail.com">wantagh.technology@gmail.com</a></u>. 
            After registration is finalized and processed, we will update our site.  Remember, this is only to help the Wantagh TechDay staff
            create a more personal, individual and exciting experience. Students need not be intimidated, and those with all interests and of all
            experience levels are welcome and encouraged to register!
          </p>
          <p align="justify">
            Those who are interested to get involved with our TechDay team can fill out a <u><a href="http://goo.gl/forms/344IE4vf8C" target="_blank">
            teacher/volunteer registration form</a></u>. We are constantly on the lookout for new talent to join our teaching staff, so don't hesitate 
            to reach out to us! We primarily work in Python and Scratch (developed by MIT Media Lab), but we are always looking to expand to new technologies.
            Don't worry if you're not familiar with either of these languages, we're more than happy to catch you up. Even if you're not a programmer, we can
            still use your help! For any questions concerning becoming a volunteer or teacher, please feel free to email 
            <u><a href="mailto:wantagh.technology@gmail.com">wantagh.technology@gmail.com</a></u>.
          </p>
          </article>
        </section>

        <section id="contact">
          <h1></h1>
          <address style="padding-top:5px;">
            <h4 style="float:right;">Wantagh TechDay  |  January 10th, 2015 | 
            <a href="mailto:wantagh.technology@gmail.com">wantagh.technology@gmail.com</a> | 
            <a href="http://facebook.com/wantaghtechday">@WantaghTechDay</a></h4>
          </address>
        </section>
      </div>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
      <script src="dist/js/bootstrap.min.js"></script>
      <script>
      $('.carousel').carousel({
        interval: 10000
        });
     </script>        
    </body>
</html>