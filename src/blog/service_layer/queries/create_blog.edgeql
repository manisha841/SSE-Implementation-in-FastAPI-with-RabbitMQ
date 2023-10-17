with title:=<str>$title,
    content:=<str>$content,
    author:=<str>$author,
    comments:=<str>$comments,
    select(
        insert Blog{
            title:=title,
            content:=content,
            author:=author,
            comments:=comments,
        }
    )
    {
        id,
        title,
        content,
        author,
        comments
    }