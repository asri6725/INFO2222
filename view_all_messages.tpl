% for user in users:
    <form action = "/messages/{{user}}" method="POST">
        <input type="hidden" name="message_user" value="{{user}}" />
        <input type="submit" value="{{user}}" />
    </form>
% end

<form action="{{server}}/messages/send" method="POST">
    <input name="message_user" type="text" placeholder="recipient (username)"/>
    <input name="message" type="text" placeholder="Message" />
    <input type="Submit" value="Send" />
</form>