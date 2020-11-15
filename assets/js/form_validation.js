$(document).ready(function() {
    $("#createIdeaForm").validate({
        rules: {
            title: {
                required: true
            },
            description: {
                required: true
            }
        },
        messages: {
            title: {
                required: "Title is required"
            },
            description: {
                required: "Description is Required"
            }
        }
    });
});