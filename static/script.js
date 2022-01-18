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



    $('#add-more-remove-charter').click(function (e) {
        e.preventDefault();
        $('#more-here').append(
            "<p class='more-wrapper'><span> <span style='font-weight:bold'>Remove character <input type='text' name='remove_charter_from_sku[]' > from SKU  <input type='text' name='sku_to_remove_charter[]'> </span> <span style='margin-left: 10px; cursor: pointer; display: none' class='xspan'>X</span> </p>"

        )
    })

    $('#add-more-remove-sku').click(function (e) {
        e.preventDefault();
        $('#more-here-sku').append(
            "<p class='more-wrapper'><span> <span style='font-weight:bold'>Replace SKU <input type='text' name='what[]' > by  <input type='text' name='forwhat[]'> </span> <span style='margin-left: 10px; cursor: pointer; display: none' class='xspan'>X</span> </p>"
        )
    })



});