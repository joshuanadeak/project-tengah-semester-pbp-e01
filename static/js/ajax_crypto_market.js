function displayCrypto(json){
    console.log(json)
    var button = (pk) => `<button onclick="deleteCrypto(${pk})" class="btn btn-outline-success rounded-pill btn-sm">BUY</button>`
    $("#market-table").empty()
    for(var i = 0 ;i < json.length ; i++){
        console.log("ini fields")
        console.log(json[i].fields)
        $("#market-table").append("<tr><td>" + json[i].fields.kode_crypto+"</td><td>"+ json[i].fields.nama_crypto+"</td><td>"+ json[i].fields.harga_crypto+"</td><td style='color: rgb(4, 169, 4); font-weight: bold' >"+ json[i].fields.risk+"</td><td>"+button(json[i].pk)+"</td></tr>")
    }
}

function updateCrypto() {
    $.getJSON("/crypto/mjson", displayCrypto);
}

function deleteCrypto(pk) {
    console.log(pk)
    $.ajax({
    url: `/crypto/delete_market/${pk}`,
    type: 'post',
    data: { },
    success: function(){
        updateCrypto(),
        $("#buyModal").modal('show');
    }
    });
}

function getFormData($form) {
    var unindexed_array = $form.serializeArray();
    var indexed_array = { };
    $.map(unindexed_array, function (n) {
        indexed_array[n['name']] = n['value'];
    });
    return indexed_array;
}

$(document).ready(function () {
    $.getJSON("/crypto/mjson", displayStock);
    document.getElementById("modalButton").setAttribute('onclick', '$("#formModal").modal("show")');
    console.log("SEBELUM SUBMIT")
    $("#addTaskForm").submit(function (e) {
        e.preventDefault();
        $(".btnClick").prop('disabled', true);
        $(".btnClick").text('Processing...');
        var $form = $(this);
        var serializedData = getFormData($form);
        $.ajax({
            url: "/crypto/add/",
            type: "POST",
            data: serializedData,
            dataType: 'text',
            success: function (response_data) {
                console.log(response_data)
                $(".btnClick").prop('disabled', false);
                $(".btnClick").text('Submit');
                $.getJSON("/crypto/mjson", displayStock);
                $("#formModal").modal('hide');
                $('#addTaskForm').each(function () {
                this.reset();
                });
            }
        });
    });
});