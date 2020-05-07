% for user in users:
    <form action = "/messages/{{username}}" method="POST">
        <input type="hidden" name="message_user" value="{{user}}" />
        <input type="submit" value="{{user}}"
    </form>