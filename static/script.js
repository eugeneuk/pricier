$( document ).ready(function() {


    $('.loadModalForm').click(function () {

        let id = $(this).data('pk')
        let sku = $(this).data('sku')
        let price = $(this).data('price')
        let msrp = $(this).data('msrp')
        let map = $(this).data('map')



        $('#id_val').val( id )
        $('#sku_val').val( sku )
        $('#price_val').val( price )
        $('#msrp_val').val( msrp )
        $('#map_val').val( map )


    })

    $("#saveModalBtn").click(function(e) {

        let id = '#l-' + $('#id_val').val()
        $(id + ' .d-sku').html( $('#sku_val').val() )
        $(id + ' .d-msrp').html( $('#msrp_val').val() )
        $(id + ' .d-price').html( $('#price_val').val() )
        $(id + ' .d-map').html( $('#map_val').val() )
        //btn



        var form = $('#saveForm');


        var url = form.attr('action');

        $.ajax({
               type: "POST",
               url: url,
               data: form.serialize(), // serializes the form's elements.
               success: function(data)
               {
                   console.log(data);
               }
             });

        $('#editModal').modal('hide');
    })



});