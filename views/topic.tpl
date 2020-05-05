<!DOCTYPE html>
<html>
<head>
<style>
* {
  box-sizing: border-box;
}

body {
  font-family: Arial;
  padding: 10px;
  background: #f1f1f1;
}

/* Header/Blog Title */
.header {
  padding: 30px;
  text-align: center;
  background: white;
}

.header h1 {
  font-size: 50px;
}

/* Style the top navigation bar */
.topnav {
  overflow: hidden;
  background-color: #333;
}

/* Style the topnav links */
.topnav a {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* Change color on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Create two unequal columns that floats next to each other */
/* Left column */
.leftcolumn {
  float: left;
  width: 65%;

}

/* Right column */
.rightcolumn {
  float: left;
  width: 35%;
  background-color: #f1f1f1;
  padding-left: 20px;
}

/* Add a card effect for articles */
.card {
  background-color: white;
  padding: 20px;
  margin-top: 20px;
  border-radius: 15px;
}
.username{
  font-size: 12px;
  margin: -5px;
  text-indent: 2%;
}
.question{
  background-color:  #C0C0C0;
  border-radius: 15px;
  padding: 1%;
}
.commentdiv{
  padding-top: 10px;
  text-indent: 5%;
}
.comment{
  font-size: 18px;
  width: 80%;
}
.submit_btn{
  font-size: 16px;
  cursor: pointer;
}

.ttl{
  font-size: 28px;
  border-top-width: 1px;
  border-left-width: 1px;
  border-right-width: 1px;
  border-bottom-width: 1px;
  height: 40px;
  text-align: left;
  text-indent: 10px;
}
.txt{
  font-size: 20px;
  border-top-width: 1px;
  border-left-width: 1px;
  border-right-width: 1px;
  border-bottom-width: 1px;
  width: 100%;
}
#textdiv{
  text-indent: 40px;
}
.userComment{
  margin-top: 1%;
  background-color:  #C0C0C0;
  border-radius: 15px;
  text-indent: 10px;
  padding: 0.2%;
  font-size: 26px;
}
.disclaimer {
  font-size: 18px;
  background-color: white;
  padding: 20px;
  margin-top: 20px;
  height: 200px;
  border-radius: 15px;
}

.help{
  background-color: white;
  font-size: 18px;
  padding: 20px;
  margin-top: 20px;
  height: 282px;
  border-radius: 15px;
}
/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

.row{
  padding-top: 20px;
  height: 100%;
  margin-top: -20px;
}

/* Footer */
.footer {
  padding: 20px;
  text-align: center;
  background: #ddd;
  margin-top: 60px;
}

#submitdiv{
  padding-top: 20px;
  text-align: center;
}
.red_text{
  color: red;
}

.h4{
  font-size: 28px;
  margin-bottom: -5px;
}


/* Responsive layout - when the screen is less than 800px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 800px) {
  .leftcolumn, .rightcolumn {
    width: 100%;
    padding: 0;
  }
}

/* Responsive layout - when the screen is less than 400px wide, make the navigation links stack on top of each other instead of next to each other */
@media screen and (max-width: 400px) {
  .topnav a {
    float: none;
    width: 100%;
  }
}
</style>
</head>
<body>

<div class="header">
  <h1> STUD <span class="red_text">HELP</span>  </h1>
</div>

<div class="topnav">
  <a href="#">Home</a>
  <a href="#">Unit</a>
  <a href="#">Academic Dishonesty</a>
</div>


<div class="row">

  <div class="leftcolumn">
    <div class="card">

        <div class="question">
          <div class="username">
            <p> Johnny Cool: </p>
          </div>
          <div id = titlediv>
          <h1 name="title" class="ttl"style="width:100%";> MY QUESTION TITLE</h1>
          <div id = textdiv>
            <p class="txt"> I have a question about websites! </p>
          </div>
        </div>
      </div>

    <div class="commentdiv">
        <form action="post" method="post">
          <input type="text" class="comment" placeholder="Add your comment here"/>
          <input value="Submit" type="submit" class="submit_btn"/>
        </form>
    </div>


    <div class="userComment">

      <div class="username">
        <p> Bret John: </p>
      </div>

      <div id = titlediv>
      <div id = userCommentdiv>
        <p class="txt"> I have the answer! </p>
      </div>
    </div>
  </div>

    <div class="commentdiv">
        <form action="post" method="post">
          <input type="text" class="comment" placeholder="Reply to this message"/>
          <input value="Submit" type="submit" class="submit_btn"/>
        </form>
    </div>


    </div>

  </div>

  <div class="rightcolumn">
    <div class="disclaimer">
      <h2>A Quick Heads Up!</h2>
      <p> Make sure your post aligns with the University of Sydney's
        <a href="https://www.sydney.edu.au/students/academic-integrity.html">Academic Integrity</a>
        policies and guidlines.
      </p>
    </div>

    <div class="help">
      <h3> Some Helpful Links </h3>

      <ul>
        <li> <a href="https://library.sydney.edu.au/">The USYD Library </a> </li>
        <br>
        <li> <a href="https://canvas.sydney.edu.au/login/canvas">Canvas Login </a> </li>
        <br>
        <li> <a href="https://sydneystudent.sydney.edu.au/">Sydney Studnet Login </a> </li>
        <br>
        <li> <a href="https://us.edstem.org/login">EdStem Login </a> </li>





    </div>
  </div>


</div>

<div class="footer">
  <h2>Footer</h2>
</div>

</body>
</html>
