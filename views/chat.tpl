% for message in chat:
    <a>Sent By {{message[1]}}</a> <br>
    <a>{{message[3]}}</a>
    <br><br>

% end

<form action="{{server}}/messages/send" method="POST">
    <input type="hidden" name="message_user" value="{{reciever}}" />
    <input type="text" name="message" placeholder="reply" />
    <input type = "submit" value="Send" />
</form>