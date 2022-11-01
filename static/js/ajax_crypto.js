function displayCrypto(json){
    console.log(json)
    var button = (pk) => `<button onclick="deleteCrypto(${pk})" class="btn btn-outline-danger btn-sm rounded-pill">SELL</button>`
    $("#crypto-table").empty()
    for(var i = 0 ;i < json.length ; i++){
        console.log("ini fields")
        console.log(json[i].fields)
        $("#crypto-table").append("<tr><td>" + json[i].fields.kode_crypto+"</td><td>"+ json[i].fields.nama_crypto+"</td><td>"+ json[i].fields.harga_crypto+"</td><td style='color: rgb(4, 169, 4); font-weight: bold'>"+ json[i].fields.risk+"</td><td>"+button(json[i].pk)+"</td></tr>")
    }
}

function displayNote(json) {
    console.log("This will be seen")
    console.log(json)
    $("#personal-note").text(json[0].fields.note)
}

function updateCrypto() {
    $.getJSON("/crypto/json", displayCrypto);
}

function deleteCrypto(pk) {
    console.log(pk)
    $.ajax({
    url: `delete_crypto/${pk}`,
    type: 'post',
    data: { },
    success: function(){
        updateCrypto(),
        $("#sellModal").modal('show');
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
    $.getJSON("/crypto/json", displayCrypto);
    $.getJSON("/crypto/porto/njson", displayNote);
    console.log("note")
    document.getElementById("modalButton").setAttribute('onclick', '$("#formModal").modal("show")');
    $("#addTaskForm").submit(function (e) {
        e.preventDefault();
        $(".btnClick").prop('disabled', true);
        $(".btnClick").text('Processing...');
        var $form = $(this);
        var serializedData = getFormData($form);
        $.ajax({
            url: "/crypto/porto/add_note/",
            type: "POST",
            data: serializedData,
            dataType: 'text',
            success: function (response_data) {
                $(".btnClick").prop('disabled', false);
                $(".btnClick").text('Submit');
                $.getJSON("/crypto/porto/njson", displayNote);
                $("#formModal").modal('hide');
                $('#addTaskForm').each(function () {
                    this.reset();
                });
            }
        });
    });
});