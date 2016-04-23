$(function() {

  // 100% twitter width
  if (typeof twttr !== 'undefined') {
    twttr.events.bind('loaded', function(event) {
      event.widgets.forEach(function (widget) {
        console.log("Created widget", widget.id);
        $('#'+widget.id).each(function() {
          $(this).css('max-width', '99%')
                 .css('width', '99%');

          $(this).contents()
                 .find('.EmbeddedTweet')
                 .css('max-width', '99%')
                 .css('width', '99%');
        });
      });
    });
  }

});
