<!DOCTYPE html>
<html>
  <head>
    <style>
      #details {
          width: 440px;
          height: 640px;
          background: rgba(255, 255, 255, 1);
          mix-blend-mode: normal;
          border: 8px solid #00F0FF;
          border-radius: 30px;
          margin: auto auto;
          position: absolute;
          top: 0px;
          right: 0px;
          bottom: 0px;
          left: 0px;
      }
      #text{
        font-size: 17px;
        text-align: center;
      }
      .red_text{
        color: red;
      }
      h1{
        text-align: center;
        font-size:  60px;
        padding-top: 0;
      }
      .icon{
        display: block;
        margin-left: auto;
        margin-right: auto;
        padding-top: 40px;
        height: 200px;
      }
      #input{
        text-align: center;
        font-size: 16px;
      }
      .email{
        font-size: 16px;
        border-top-width: 0;
        border-left-width: 0;
        border-right-width: 0;
        border-bottom-width: 1px;
        border-bottom-color: black;
        height: 30px
      }
      .button{
        font-size: 16px;
        cursor: pointer;
      }
    </style>
  </head>
  <body style="background-color:#220036">
    <div id ="details">
      <img src="../img/cropped.png" alt="icon" class="icon">
      <h1> STUD <span class="red_text">HELP</span>  </h1>

      <div id="text">
        Please enter the email used for your account:
      </div>

      <div id="input">
        <p>
          <form action = "{{server}}/forgot-pwd"method="post">
            <input name="email" type="email" class="email" placeholder="Email" />
            <br>
            <br>
            <button type="submit" name="reset" class="button">Reset</button>
          </form>
        </p>
    </div>
  </body>
</html>
