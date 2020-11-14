function get_current_amouont()
{
    $.ajax({
            type: 'GET',
            async: true,
            url: "/ajax/get_amount/",
            success: function(data) {
                if (data['response'] == "Success") 
                {
                    document.getElementById('amount').innerHTML=data['amount'];
                }
            },
            dataType: 'json',
        });
}

setInterval(get_current_amouont, 1000);