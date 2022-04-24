$(document).ready(function(){
    let body = $('body')
    body.fadeIn(400);
    $(document).on("click", "a:not([href^='#'])", function(e) {
        e.preventDefault();
        $('body').fadeOut(400);
        let self = this;
        setTimeout(function () {
            window.location.href = $(self).attr('href');
        }, 400);
    });
});