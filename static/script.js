$(document).ready(function() {
    $('#currency-form').submit(function(event) {
        event.preventDefault();

        var formData = {
            amount: $('#amount').val(),
            from_currency: $('#from-currency').val(),
            to_currency: $('#to-currency').val()
        };

        $.ajax({
            type: 'POST',
            url: '/convert',
            data: formData,
            dataType: 'json',
            encode: true
        })
        .done(function(data) {
            $('#result').html('<p>' + data.result + '</p>');
        })
        .fail(function(data) {
            console.log(data);
            $('#result').html('<p>Erro ao converter moeda. Por favor, tente novamente mais tarde.</p>');
        });
    });
});
