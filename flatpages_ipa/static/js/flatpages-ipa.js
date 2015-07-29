/* looks for trigger classes and activate the ipa behavior */

$('.editable-click').popover({html: true})

$(document).on('submit', 'form.image-uploader', function(event) {
    var $this = $(this);
    var data = new FormData(this)
    $.ajax({
        method: $this.attr('method'),
        url: $this.attr('action'),
        data: data,
        contentType: false,
        cache: false,
        processData: false,
        async: false,
        success: function(pk) {
            $.ajax({
                method: 'POST',
                url: $this.data('next-url'),
                data: $.param({value: pk, name: 'content'}),
                cache: false,
                success: function() {
                    document.location.reload();
                }
            });
        }
    });
    event.preventDefault();
})
