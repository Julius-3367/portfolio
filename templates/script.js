$(document).ready(function() {
    $('#loginForm').submit(function(e) {
        e.preventDefault();
        var username = $('#username').val();
        var password = $('#password').val();
        $.ajax({
            type: 'POST',
            url: '/login',
            contentType: 'application/json',
            data: JSON.stringify({username: username, password: password}),
            success: function(response) {
                $('#message').text(response.message);
                if (response.message === 'Login successful') {
                    window.location.href = '/'; // Redirect to home page or dashboard
                }
            },
            error: function(xhr, status, error) {
                $('#message').text('Error: ' + xhr.responseText);
            }
        });
    });
});

