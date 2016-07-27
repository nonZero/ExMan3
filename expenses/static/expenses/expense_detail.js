$(function () {
    console.log("LOADED");

    $("form").submit(function () {
        console.log("SUBMIT");

        var data = {
            body_markdown: $("#id_body_markdown").val()
        };

        $.post('', data).then(function (html) {
            console.log(html);
            $("#comments").prepend($(html.trim()).hide().slideDown());
            $("#id_body_markdown").val('');
        });
        return false;
    })

});